<template>
  <div class="dashboard">
    <span class="spacer"></span>
    TODO: Make the detail page
  </div>
</template>

<script>
export default {
  name: "device",
  metaInfo: function() {
    return {
      title: this.$store.state.device.name
    };
  },
  computed: {
    deviceID: function() {
      return this.$route.params.id;
    },
    device: function() {
      return this.$store.state.device;
    },
    detail: function() {
      return this.$route.params.detail;
    }
  },
  created: function() {
    this.$store.dispatch("device/set", this.deviceID);
    this.$store.dispatch("device/update");
    this.$store.dispatch("nav/setBc", [
      "DripDash",
      "Device",
      this.device.name,
      this.$utils.toTitleCase(this.detail)
    ]);
  },
  components: {}
};
</script>

<style scoped lang="scss">
.spacer {
  display: block;
  height: 30px;
}
</style>
