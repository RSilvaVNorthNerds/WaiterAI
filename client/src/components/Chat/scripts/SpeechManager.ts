import * as SpeechSDK from "microsoft-cognitiveservices-speech-sdk";
const envVars = import.meta.env;

class SpeechManager {
  speechAPIKey: string;
  speechAPIRegion: string;

  constructor() {
    this.speechAPIKey = envVars.VITE_AZURE_SPEECH_KEY;
    this.speechAPIRegion = envVars.VITE_AZURE_SPEECH_REGION;
  }

  text_to_speech(text: string) {
    const speechConfig = SpeechSDK.SpeechConfig.fromSubscription(
      this.speechAPIKey,
      this.speechAPIRegion
    );

    const audioConfig = SpeechSDK.AudioConfig.fromDefaultSpeakerOutput();

    const speechSynthesizer = new SpeechSDK.SpeechSynthesizer(
      speechConfig,
      audioConfig
    );

    speechSynthesizer.speakTextAsync(text, (result) => {
      if (result.reason === SpeechSDK.ResultReason.SynthesizingAudioCompleted) {
        console.log("SUCCESS: Speech synthesized successfully.");
      } else {
        console.error(
          "ERROR: Speech synthesis failed. Ensure the text is valid and try again."
        );
      }
    });
  }

  speech_to_text(conversation: { text: string; speaker: "waiter" | "user" }[]) {
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
      conversation.push({
        text: question,
        speaker: "user",
      });
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
              conversation.push({
                text: data,
                speaker: "waiter",
              });
              this.text_to_speech(data);
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
