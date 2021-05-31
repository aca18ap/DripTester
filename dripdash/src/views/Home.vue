<template>
  <div class="dashboard">
    <DeviceList />
    <Groups />
  </div>
</template>

<script>
import DeviceList from "@/components/DeviceList.vue";
import Groups from "@/components/Groups.vue"

export default {
  name: "dashboard",
  metaInfo: {
    title: "Dashboard"
  },
  components: {
    DeviceList,
    Groups
  },
  created() {
    this.$store.dispatch("nav/setBc", ["DripDash", "Home", "Summary"]);
  }
};
</script>

<style scoped lang="scss">
.dashboard {
  display: grid;
  grid-template-columns: 1fr;
  gap: 1rem;
  padding: 1rem 0;
}
</style>
