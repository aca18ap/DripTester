<template>
  <div class="dashboard">
    <br />
    <AddDevice />
  </div>
</template>

<script>
import AddDevice from "@/components/AddDevice.vue";

export default {
  name: "dashboard",
  metaInfo: {
    title: "Dashboard"
  },
  components: {
    AddDevice
  },
  created() {
    this.$store.dispatch("nav/setBc", ["DripDash", "Devices", "Add Device"]);
  }
};
</script>
