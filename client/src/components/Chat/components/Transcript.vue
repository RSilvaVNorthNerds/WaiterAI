<template>
  <div class="transcript">
    <h3>Transcript</h3>
    <div class="conversation-box">
      <div class="user">
        <div
          v-for="message in conversation.user"
          :key="message.id"
          class="message user-message"
        >
          {{ message.text }}
        </div>
      </div>
      <div class="waiter">
        <div
          v-for="message in conversation.waiter"
          :key="message.id"
          class="message waiter-message"
        >
          {{ message.text }}
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Message {
  id: string;
  text: string;
}

const props = defineProps<{
  conversation: {
    user: Message[];
    waiter: Message[];
  };
}>();
</script>

<style scoped>
.transcript {
  width: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.conversation-box {
  display: flex;
  flex-direction: column;
  width: 100%;
  max-width: 600px;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #181818;
}
</style>
