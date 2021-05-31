<template>
  <b-container>
    <b-card title="Add a Device">
      <p>Set your device's endpoint to:</p>
      <pre class="endpoint"><code>{{ collectorEndpoint }}</code></pre>
      <p>Once it's connected to DripDash, it'll appear below.</p>
      <hr />
      <div
        class="alert-light alert bg-light my-0 text-center py-4"
        v-if="unregisteredDevices && unregisteredDevices.length == 0"
      >
        There are no unregistered devices.
      </div>
      <ListItem
        v-for="device in unregisteredDevices"
        v-bind:key="device.id"
        @click="addDevice(device.id)"
      >
        <div class="left">
          {{ device.id }}
        </div>
        <b-button size="sm" variant="info">Add</b-button>
      </ListItem>
    </b-card>
  </b-container>
</template>

<script>
import ListItem from "@/components/ListItem.vue";
import gql from "graphql-tag";

export default {
  components: {
    ListItem
  },
  data() {
    return {
      unregisteredDevices: []
    };
  },
  computed: {
    collectorEndpoint: function() {
      return window.location.origin + "/collect";
    }
  },
  methods: {
    addDevice: function(id) {
      this.$apollo
        .mutate({
          mutation: gql`
            mutation($deviceId: String!) {
              addDevice(id: $deviceId) {
                id
              }
            }
          `,
          variables: {
            deviceId: id
          }
        })
        .then(() => {
          this.$router.push("/");
        });
    }
  },
  apollo: {
    unregisteredDevices: {
      query: gql`
        query {
          unregisteredDevices {
            id
          }
        }
      `,
      pollInterval: 2000
    }
  }
};
</script>

<style scoped lang="scss">
.left * {
  margin-right: 1rem;
}

.endpoint {
  background: var(--light);
  padding: 0.5rem;
  border-radius: 8px;
}
</style>
