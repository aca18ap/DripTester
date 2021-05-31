<template>
  <div v-bind:class="{ expanded: this.expanded }" class="cont" @click.prevent>
    <NavIcon @click="toggle" :icon="this.mainIcon" class="icn-m" />
    <span v-bind:class="{ expanded: this.expanded }" class="renamer">
      <b-form-input
        v-model="text"
        class="renamer-input"
        placeholder="Rename"
        ref="name"
        v-on:keydown.enter.prevent="toggle"
      >
      </b-form-input>
      <NavIcon v-if="this.expanded" @click="exit" icon="times" />
    </span>
  </div>
</template>

<script>
import NavIcon from "@/components/NavIcon.vue";

export default {
  name: "Renamer",
  props: {
    startText: String
  },
  components: {
    NavIcon
  },
  computed: {
    mainIcon: function() {
      return !this.expanded ? "pencil-alt" : "save";
    }
  },
  data() {
    return {
      expanded: false,
      text: this.startText
    };
  },
  methods: {
    toggle: function() {
      this.expanded = !this.expanded;
      if (this.expanded) {
        this.$refs.name.$el.focus();
        this.$refs.name.$el.select();
      } else {
        // save
        if (this.text != this.startText) {
          this.$emit("save", this.text);
        }
      }
    },
    exit: function() {
      this.expanded = false;
      this.text = this.startText;
    }
  }
};
</script>

<style scoped lang="scss">
.renamer {
  display: inline-flex;
  flex-direction: row;
  align-items: center;
  width: 0px;
  overflow: hidden;
  transition: all 0.25s ease-in-out;

  &.expanded {
    width: 12.5em;
    font-size: 0.85em;
  }
}

.cont {
  font-size: 1em;
  height: 2.5em;
  display: flex;
  padding: 0;
  flex-direction: row;
  align-items: center;
  transition: all 0.25s ease-in-out;
  border-radius: 0.25em;
  border: 1px solid transparent;

  &.expanded {
    border-color: #ced4da;

    .icn-m {
      font-size: 0.85em;
    }
  }
}

.renamer-input {
  font-size: 1em;
  border: 0;
  width: 10em;
  background: transparent;
  padding: 0;

  &:focus,
  :active {
    outline-color: transparent !important;
    outline-style: none !important;
    outline: none !important;
    box-shadow: none;
  }
}
</style>
