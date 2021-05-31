<template>
  <span class="updatecandy">
    <template v-if="this.trueUpdating">
      Updating
      <b-spinner small class="loader" label="Loading..."></b-spinner>
    </template>
    <template v-else>
      <TimeAgo :time="this.updated" text="Updated" dynamic />
    </template>
  </span>
</template>

<script>
import TimeAgo from "@/components/TimeAgo.vue";

export default {
  name: "UpdateCandy",
  props: {
    updating: Boolean,
    updated: [Date, Number]
  },
  computed: {
    trueUpdating: function() {
      if (typeof this.updated === "number") {
        return true;
      } else {
        return this.updating;
      }
    }
  },
  components: {
    TimeAgo
  }
};
</script>

<style scoped lang="scss">
.loader {
  width: 1em;
  height: 1em;
  vertical-align: text-bottom;
  margin-left: 0.5em;
  border-width: 2px;
}

.updatecandy {
  font-size: 0.85em;
  color: var(--secondary);
  display: flex;
  align-items: center;
  margin: 0 1em;
}
</style>
