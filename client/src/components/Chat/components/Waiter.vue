<script setup lang="ts">
import Transcript from "./Transcript.vue";
import SpeechManager from "../scripts/SpeechManager";
import { reactive, ref } from "vue";

const state = reactive({
  conversation: [],
});

const isListening = ref(false);
const isLoading = ref(false);

const handleListening = (listening: boolean) => {
  if (listening) {
    handleLoading(false);
  }

  isListening.value = listening;
};

const handleLoading = (loading: boolean) => {
  isLoading.value = loading;
};

function order() {
  handleLoading(true);
  const speechManager = new SpeechManager();
  speechManager.speech_to_text(state.conversation, handleListening);
}

function question() {
  handleLoading(true);
  const speechManager = new SpeechManager();
  speechManager.speech_to_text(state.conversation, handleListening);
}

// function tts() {
//   const speechManager = new SpeechManager();
//   speechManager.text_to_speech("Hello, how can I help you?");
// }
</script>

<template>
  <div class="waiter">
    <div v-if="isListening">
      <h2>Listening for your request...</h2>
    </div>
    <div v-if="!isListening">
      <h2>Welcome to Mama Bistro! How can I help you?</h2>
    </div>
    <div v-if="isLoading">
      <h2>Loading...</h2>
    </div>
  </div>
  <div class="waiter-controls">
    <button @click="order" class="waiter-action-btn">
      <span class="material-symbols-outlined"> restaurant </span>
      Order
    </button>
    <button @click="question" class="waiter-action-btn">
      <span class="material-symbols-outlined"> help </span>
      Question
    </button>
    <!-- <button @click="tts" class="waiter-action-btn">
      <span class="material-symbols-outlined"> mic </span>
      Speak
    </button> -->
  </div>
  <Transcript :conversation="state.conversation" />
</template>

<style scoped>
.waiter-controls {
  display: flex;
  justify-content: center;
  align-items: center;
}

.waiter-action-btn {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  margin: 0px 10px;
}
</style>
