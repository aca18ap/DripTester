<template>
  <b-container>
    <div class="card">
      <div class="card-body">
        <div class="header">
          <h4 class="card-title">Your Devices</h4>
          <NavIcon
            icon="plus"
            class="add"
            @click="$router.push('/add-device')"
          />
        </div>
        <div
          class="alert-light alert bg-light my-0 text-center py-4"
          v-if="self.devices && self.devices.length == 0"
        >
          You don't own any devices. Click '+' to add one.
        </div>
        <DeviceListItem
          v-for="device in self.devices"
          v-bind:key="device.id"
          :device="device"
        />
      </div>
    </div>
  </b-container>
</template>

<script>
import DeviceListItem from "@/components/DeviceListItem.vue";
import NavIcon from "@/components/NavIcon.vue";
import gql from "graphql-tag";

export default {
  name: "DeviceList",
  components: {
    DeviceListItem,
    NavIcon
  },
  data() {
    return {
      refreshInterval: "",
      self: {}
    };
  },
  apollo: {
    self: {
      query: gql`
        query {
          self {
            id
            devices {
              id
              name
              latest {
                timestamp
              }
              status
            }
          }
        }
      `,
      pollInterval: 2000,
      notifyOnNetworkStatusChange: true,
      deep: true
    }
  }
};
</script>

<style lang="scss" scoped>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1rem;

  h4 {
    margin: 0;
  }

  .add {
    font-size: 1.25em;
  }
}
</style>
