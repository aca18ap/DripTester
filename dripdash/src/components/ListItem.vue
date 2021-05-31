<template>
  <component
    @click="$emit('click')"
    class="list-item"
    :to="to"
    :is="to ? 'router-link' : 'li'"
  >
    <slot />
  </component>
</template>

<script>
export default {
  name: "ListItem",
  props: {
    to: [Object, String]
  }
};
</script>

<style scoped lang="scss">
.list-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  text-decoration: none;
  border-radius: 0.5em;
  transition: all 0.15s ease-in-out;
  padding: 0.5em;
  cursor: pointer;
  margin: 0 -0.5em;

  &:hover {
    background: var(--light);
  }
}
</style>
