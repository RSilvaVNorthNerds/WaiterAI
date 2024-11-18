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
      if (result.reason === SpeechSDK.ResultReason.RecognizedSpeech) {
        console.error(`RECOGNIZED: Text=${result.text}`);
        return result.text;
      } else {
        console.error(
          "ERROR: Speech was cancelled or could not be recognized. Ensure your microphone is working properly."
        );
      }
    });
  }
}

export default SpeechManager;
