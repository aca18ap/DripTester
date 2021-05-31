<template>
  <b-card title="At a Glance">
    <div
      class="glance"
      v-for="(glance, idx) in glances"
      v-bind:key="idx"
    >
      <Glance :title="glance.title" :text="glance.text" :state="glance.status" />
    </div>
  </b-card>
</template>

<script>
import Glance from "@/components/glances/Glance.vue";

export default {
  name: "AtAGlanceCard",
  components: {
    Glance
  },
  props: {
    glances: Array
  }
};
</script>

<style lang="scss" scoped>
.glance {
  padding-bottom: 0.5em;
}
</style>
