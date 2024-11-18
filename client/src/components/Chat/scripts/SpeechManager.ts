import * as SpeechSDK from "microsoft-cognitiveservices-speech-sdk";
const envVars = import.meta.env;

class SpeechManager {
  speechAPIKey: string;
  speechAPIRegion: string;

  constructor() {
    this.speechAPIKey = envVars.VITE_AZURE_SPEECH_KEY;
    this.speechAPIRegion = envVars.VITE_AZURE_SPEECH_REGION;
  }

  speech_to_text() {
    const speechConfig = SpeechSDK.SpeechConfig.fromSubscription(
      this.speechAPIKey,
      this.speechAPIRegion
    );

    speechConfig.speechRecognitionLanguage = "en-US";

    console.error("LISTENING...");
    const audioConfig = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    const recognizer = new SpeechSDK.SpeechRecognizer(
      speechConfig,
      audioConfig
    );

    recognizer.recognizeOnceAsync((result) => {
      const question = result.text;
      if (result.reason === SpeechSDK.ResultReason.RecognizedSpeech) {
        // Send the question to the server
        fetch("http://localhost:8000/submit_waiter_request", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ prompt: question }),
        }).then((response) => {
          if (response.ok) {
            response.json().then((data) => {
              console.log(data);
            });
          }
        });
      } else {
        console.error(
          "ERROR: Speech was cancelled or could not be recognized. Ensure your microphone is working properly."
        );
      }
    });
  }
}

export default SpeechManager;
