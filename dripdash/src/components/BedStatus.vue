<template>
  <div class="bed">
    <div class="id">
      {{ this.id }}
    </div>
    <div class="indicator" :data-state="this.bed.state">
      <font-awesome-icon v-if="this.fill" class="icon" icon="arrow-up" />
      <font-awesome-icon v-if="this.drain" class="icon" icon="arrow-down" />
    </div>
    <span class="state">{{ this.textState }}</span>
  </div>
</template>

<script>
export default {
  name: "BedStatus",
  props: {
    bed: Object,
    id: Number
  },
  computed: {
    textState() {
      switch (this.bed.state) {
        case 0:
          return "Flooding";
        case 1:
          return "Flooded";
        case 2:
          return "Draining";
        case 3:
          return "Drained";
        default:
          return "Unknown";
      }
    },
    fill() {
      return this.bed.state == 0;
    },
    drain() {
      return this.bed.state == 2;
    }
  }
};
</script>

<style lang="scss" scoped>
.bed {
  display: flex;
  position: relative;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  padding: 0 1em;
}

.id {
  position: absolute;
  top: 0;
  left: 0;
  display: flex;
  width: 2em;
  height: 2em;
  align-items: center;
  justify-content: center;
  border: 4px solid #dfdfdf;
  border-radius: 50%;
}

.indicator {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 10em;
  height: 10em;
  border-radius: 100%;
  border: 4px solid #dfdfdf;

  &[data-state="0"] {
    background: linear-gradient(to top, var(--accent) 75%, white 80%);
    color: #fff;
  }

  &[data-state="1"] {
    background: linear-gradient(to top, var(--accent) 75%, white 80%);
  }

  &[data-state="2"] {
    background: linear-gradient(to top, var(--accent) 20%, white 25%);
    color: var(--accent);
  }

  &[data-state="3"] {
    background: linear-gradient(to top, var(--accent) 20%, white 25%);
  }

  &[data-state="4"] {
    background: linear-gradient(to top, var(--accent) 45%, white 50%);
  }
}

.icon {
  font-size: 2em;
}
</style>
