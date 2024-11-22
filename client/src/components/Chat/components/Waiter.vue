<script setup lang="ts">
import Transcript from "./Transcript.vue";
import SpeechManager from "../scripts/SpeechManager";
import { reactive } from "vue";

const state = reactive({
  conversation: [],
});

function order() {
  const speechManager = new SpeechManager();
  speechManager.speech_to_text(state.conversation);
}

function question() {
  const speechManager = new SpeechManager();
  speechManager.speech_to_text(state.conversation);
}
</script>

<template>
  <div class="waiter">
    <video muted autoplay width="400px" height="300px" loop>
      <source src="../../../assets/videos/waiter.mp4" type="video/mp4" />
      Video is not supported
    </video>
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
