<template>
  <b-card title="Bed Status">
    <div class="beds">
      <Bed
        v-for="(bed, index) in this.$store.getters['device/getLatest']('beds')
          .field"
        v-bind:key="index"
        :bed="bed"
        :id="index + 1"
      />
    </div>
  </b-card>
</template>

<script>
import Bed from "@/components/BedStatus.vue";

export default {
  name: "BedStatusCard",
  components: {
    Bed
  }
};
</script>

<style lang="scss" scoped>
.beds {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
}
</style>
