<template>
  <div class="glance">
    <div class="title">
      <span>{{ title }}</span>
      <StateIcon :status="state" class="icon" />
    </div>
    <p v-if="showText" class="text">{{ text }}</p>
  </div>
</template>

<script>
import StateIcon from "@/components/StateIcon.vue";

export default {
  name: "Glance",
  props: {
    title: String,
    text: {
      required: false,
      type: String,
      default: ""
    },
    state: String
  },
  components: {
    StateIcon
  },
  computed: {
    showText() {
      return this.text && (this.text.length > 0);
    }
  }
};
</script>

<style lang="scss" scoped>
.title {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  font-size: 1.1em;
}

.text {
  font-size: 0.85em;
  color: var(--secondary);
  margin-bottom: 0;
}
</style>
