<template lang="html">
  <b-container :class="classes" title="Quick Switch">
    <div class="wrap">
      <div class="col">
        <router-link
          v-for="device in $store.state.devices.list"
          v-bind:id="device.progName"
          v-bind:key="device.progName"
          :to="{ name: 'device', params: { id: device.progName } }"
          :class="getDeviceClass(device)"
        >
          {{ device.name }}
        </router-link>
      </div>
      <div v-if="$store.state.device.progName != ''" :class="getAttribClass()">
        <router-link
          v-for="(attrib, idx) in $store.state.device.fields"
          v-bind:key="idx"
          :to="{
            name: 'deviceDetail',
            params: { device: $store.state.device.progName, detail: attrib.lnk }
          }"
        >
          {{ attrib.title }}
        </router-link>
      </div>
    </div>
  </b-container>
</template>

<script>
export default {
  name: "QuickSwitch",
  props: {
    active: Boolean
  },
  computed: {
    classes() {
      return this.active ? "switcher active" : "switcher";
    }
  },
  created: function() {
    if (this.$store.getters["auth/isAuthenticated"]) {
      this.$store.dispatch("devices/update");
    }
  },
  methods: {
    getDeviceClass(device) {
      const currentDevice = this.$store.state.device;
      return device.progName == currentDevice.progName ? "active" : "";
    },
    getAttribClass() {
      const currentDevice = this.$store.state.device;
      return currentDevice.progName == "" ? "col hide" : "col";
    }
  }
};
</script>

<style lang="scss" scoped>
.switcher {
  box-sizing: border-box;
  max-height: 0;
  overflow: hidden;
  transition: max-height 250ms ease-in-out;
  display: flex;

  &.active {
    max-height: 20em;
  }
}

.wrap {
  width: 100%;
  height: 100%;
  margin: 1em 0;
  display: flex;
  flex-direction: row;
  border: 1px solid var(--light);
  border-radius: 4px;
  overflow: hidden;
}

.col {
  border-right: 1px solid var(--light);
  padding: 0;
  flex: 1 1;
  transition: flex 250ms ease-in-out;

  &.hide {
    flex: 0 1 0px;
    overflow: hidden;
  }
}

a {
  display: block;
  text-decoration: none;
  padding: 0.5em;
  color: var(--dark);

  &.active {
    background: var(--accent);
    color: var(--white);
  }

  &:not(.active):hover {
    background: var(--light);
  }
}
</style>
