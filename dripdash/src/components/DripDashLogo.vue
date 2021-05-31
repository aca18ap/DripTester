<template>
  <svg
    :style="style"
    version="1.1"
    id="dd-logo"
    x="0px"
    y="0px"
    viewBox="0 0 63.8 63.8"
    xml:space="preserve"
  >
    <path
      d="M38.8,28.9h13c-0.9-2.1-2-4-3.4-5.7l-18-22.4c-0.8-1-2.3-1-3.1,0l-18,22.4c-3.4,4.3-5.5,9.7-5.5,15.6
  	c0,14.3,12.1,25.9,26.6,24.9C42.5,63,52.5,53.3,53.7,41.3c0.1-1.5,0.1-2.9,0-4.4H38.8V28.9z"
    />
    <path d="M63.8,28.9h-12c1.1,2.5,1.8,5.2,2,8h10.1V28.9z" />
  </svg>
</template>

<script>
export default {
  name: "BreadcrumbButton",
  props: {
    color: String
  },
  computed: {
    style() {
      return "fill: " + (this.color || "var(--accent);");
    }
  }
};
</script>

<style scoped lang="scss">
svg {
  width: 40px;
  height: 40px;
}
</style>
