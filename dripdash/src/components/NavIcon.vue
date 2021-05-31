<template>
  <a class="btn-icn" @click.prevent="$emit('click')">
    <font-awesome-icon :icon="icon" />
  </a>
</template>

<script>
export default {
  name: "NavIcon",
  props: {
    icon: String
  }
};
</script>

<style scoped lang="scss">
.btn-icn {
  width: 30px;
  height: 30px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  z-index: 10;
  margin: 0 2px;

  svg {
    color: var(--gray);
  }

  &:hover::before {
    width: 30px;
    height: 30px;
    left: calc(50% - 15px);
  }

  &:before {
    position: absolute;
    content: "";
    background-color: rgba(0, 0, 0, 0.035);
    width: 0;
    height: 0;
    left: 50%;
    border-radius: 50%;
    transition: all 0.2s ease-in-out;
    z-index: -1;
  }
}
</style>
