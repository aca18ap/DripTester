<template>
  <b-button @click="toggle" class="bc-btn" variant="outline-light">
    <div class="bc-mini">
      {{ crumbs }}
    </div>
    <div class="bc-main">{{ text }}</div>
    <div :class="iconCls"><font-awesome-icon icon="angle-down" /></div>
  </b-button>
</template>

<script>
export default {
  name: "BreadcrumbButton",
  props: {
    bc: Array
  },
  computed: {
    crumbs() {
      return this.bc.slice(0, -1).join(" › ");
    },
    text() {
      return this.bc[this.bc.length - 1];
    },
    iconCls() {
      return this.isOpen ? "bc-icn turn" : "bc-icn";
    }
  },
  data() {
    return {
      isOpen: false
    };
  },
  methods: {
    toggle() {
      this.isOpen = !this.isOpen;
      this.$emit("toggle", this.isOpen);
    }
  }
};
</script>

<style scoped lang="scss">
.bc-mini {
  padding: 0;
  margin: 0;
  font-size: 0.7em;
  color: var(--gray);
  grid-area: crumb;
}

.bc-main {
  padding: 0;
  margin: 0;
  font-size: 1.25em;
  color: var(--dark);
  grid-area: main;
}

.bc-icn {
  grid-area: icon;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  justify-content: center;
  padding-left: 8px;

  svg {
    color: var(--dark);
    transition: transform 250ms ease-in-out;
  }

  &.turn svg {
    transform: rotate(180deg);
  }
}

.bc-btn {
  display: grid;
  grid-template-areas: "crumb icon" "main icon";
  padding: 0 4px;
  text-align: left;
  min-width: 12rem;
  flex-grow: 0;
}
</style>
