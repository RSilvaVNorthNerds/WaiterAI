import * as SpeechSDK from "microsoft-cognitiveservices-speech-sdk";
const envVars = import.meta.env;

class SpeechManager {
  speechAPIKey: string;
  speechAPIRegion: string;
  recognizer: SpeechSDK.SpeechRecognizer;
  speechSynthesizer: SpeechSDK.SpeechSynthesizer;

  constructor() {
    this.speechAPIKey = envVars.VITE_AZURE_SPEECH_KEY;
    this.speechAPIRegion = envVars.VITE_AZURE_SPEECH_REGION;

    const speechConfig = SpeechSDK.SpeechConfig.fromSubscription(
      this.speechAPIKey,
      this.speechAPIRegion
    );

    speechConfig.speechRecognitionLanguage = "en-US";

    const audioConfig = SpeechSDK.AudioConfig.fromDefaultMicrophoneInput();
    const recognizer = new SpeechSDK.SpeechRecognizer(
      speechConfig,
      audioConfig
    );

    const speakerConfig = SpeechSDK.AudioConfig.fromDefaultSpeakerOutput();
    const speechSynthesizer = new SpeechSDK.SpeechSynthesizer(
      speechConfig,
      speakerConfig
    );

    this.recognizer = recognizer;
    this.speechSynthesizer = speechSynthesizer;
  }

  text_to_speech(text: string) {
    this.speechSynthesizer.speakTextAsync(text, (result) => {
      if (result.reason === SpeechSDK.ResultReason.SynthesizingAudioCompleted) {
        console.log("SUCCESS: Speech synthesized successfully.");
      } else {
        console.error(
          "ERROR: Speech synthesis failed. Ensure the text is valid and try again."
        );
      }
    });
  }

  speech_to_text(
    conversation: { text: string; speaker: "waiter" | "user" }[],
    listening: (listening: boolean) => void
  ) {
    this.recognizer.startContinuousRecognitionAsync(() => {
      console.log("Recognizer is actively listening...");
      listening(true);
    });

    this.recognizer.recognized = (s, e) => {
      // Ignore empty results
      if (!e.result.text.trim()) {
        console.warn("Ignoring empty result.");
        return;
      }

      this.recognizer.stopContinuousRecognitionAsync(
        () => {
          console.log("Recognizer stopped.");
          listening(false);
        },
        (err) => {
          console.error(`Error stopping recognizer: ${err}`);
        }
      );

      const question = e.result.text;
      conversation.push({
        text: question,
        speaker: "user",
      });

      if (e.result.reason === SpeechSDK.ResultReason.RecognizedSpeech) {
        fetch(`${envVars.VITE_WAITER_SERVICE_URL}/submit_waiter_request`, {
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
    };

    this.recognizer.canceled = (s, e) => {
      console.error(`Recognition canceled: ${e.errorDetails}`);
    };

    this.recognizer.sessionStopped = (s, e) => {
      console.log("Session stopped.");
      this.recognizer.stopContinuousRecognitionAsync();
    };
  }
}

export default SpeechManager;
