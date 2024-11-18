<script setup lang="ts">
import Transcript from "./Transcript.vue";
</script>

<template>
  <div class="waiter">
    <video muted autoplay width="400px" height="300px" loop>
      <source src="../../../assets/videos/waiter.mp4" type="video/mp4" />
      Video is not supported
    </video>
  </div>
  <div class="waiter-controls">
    <button class="waiter-action-btn">Listen</button>
    <button class="waiter-action-btn">Order</button>
    <button class="waiter-action-btn">Question</button>
  </div>
  <Transcript />
</template>
