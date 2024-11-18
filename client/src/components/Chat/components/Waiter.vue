<script setup lang="ts">
import Transcript from "./Transcript.vue";
import SpeechManager from "../scripts/SpeechManager";

function listen() {
  const speechManager = new SpeechManager();
  speechManager.speech_to_text();
}

function order() {
  const speechManager = new SpeechManager();
  speechManager.speech_to_text();
}

function question() {
  const speechManager = new SpeechManager();
  const question = speechManager.speech_to_text();

  // Send the question to the server
  fetch("", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ question }),
  }).then((response) => {
    if (response.ok) {
      response.json().then((data) => {
        console.log(data);
      });
    }
  });
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
    <button @click="listen" class="waiter-action-btn">Listen</button>
    <button class="waiter-action-btn">Order</button>
    <button class="waiter-action-btn">Question</button>
  </div>
  <Transcript />
</template>
