<template>
  <div class="transcript">
    <h3>Conversation</h3>
    <div class="conversation-box">
      <div
        v-for="message in conversation"
        :class="[
          'message',
          {
            'user-message': message.speaker === 'user',
            'waiter-message': message.speaker === 'waiter',
          },
        ]"
      >
        {{ message.text }}
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
interface Message {
  text: string;
  speaker: "user" | "waiter";
}

const props = defineProps<{
  conversation: Message[];
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
  justify-content: center;
  width: 100%;
  max-width: 600px;
  padding: 1rem;
  border: 1px solid #ccc;
  border-radius: 5px;
  background-color: #181818;
}

.message {
  padding: 0.5rem;
  margin: 0.5rem;
  border-radius: 5px;
}

.user-message {
  background-color: #00c344;
  color: white;
}

.waiter-message {
  background-color: #1d7ef5;
  color: white;
}
</style>
