<template>
  <a class="btn-icn">
    <font-awesome-icon v-if="isOK" class="state-icon ok" icon="check-circle" />
    <font-awesome-icon v-if="isKO" class="state-icon ko" icon="times-circle" />
    <font-awesome-icon
      v-if="isWarn"
      class="state-icon warn"
      icon="exclamation-circle"
    />
    <font-awesome-icon
      v-if="!isKO && !isOK && !isWarn"
      class="state-icon unknown"
      :icon="['far', 'question-circle']"
    />
  </a>
</template>

<script>
export default {
  name: "StateIcon",
  props: {
    status: String
  },
  computed: {
    isOK: function() {
      return this.status == "OK";
    },
    isKO: function() {
      return this.status == "KO";
    },
    isWarn: function() {
      return this.status == "WARN";
    }
  }
};
</script>

<style scoped lang="scss">
.state-icon {
  width: 1.5em;
  height: 1.5em;
  vertical-align: bottom;
}

.ok {
  color: var(--success);
}

.unknown {
  color: var(--secondary);
}

.warn {
  color: var(--warning);
}

.ko {
  color: var(--danger);
}
</style>
