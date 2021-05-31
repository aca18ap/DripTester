<template>
  <div class="card">
    <div class="card-body">
      <div class="header">
        <h4 class="card-title">{{ group.name }}</h4>
        <span class="controls">
          <NavIcon
            icon="microchip"
            class="devices"
            @click="$bvModal.show(`${group.id}-devices-modal`)"
          />
          <NavIcon
            icon="users"
            class="members"
            @click="$bvModal.show(`${group.id}-members-modal`)"
          />
        </span>
      </div>
      <div
        class="alert-light alert bg-light my-0 text-center py-4"
        v-if="group.devices && group.devices.length == 0"
      >
        No devices in this group.
      </div>
      <DeviceListItem
        v-for="device in group.devices"
        v-bind:key="device.id"
        :device="device"
        :detailed="false"
      />
    </div>


    <b-modal :id="`${group.id}-members-modal`" :title="`${group.name} - Members`">
      
      <ListItem
        v-for="member in group.members"
        v-bind:key="member.id"
      >
        {{ member.username }}
      </ListItem>

      <template v-slot:modal-footer>
        <b-form class="w-100 d-flex flex-nowrap" inline>
          <b-input-group class="mr-3 flex-grow-1">
            <b-form-input placeholder="Username" v-model="username"></b-form-input>
            <b-input-group-append>
              <b-button variant="primary" @click="addUser">Add User</b-button>
            </b-input-group-append>
          </b-input-group>
          <b-button class="flex-shrink-0" @click="leave" variant="outline-danger">Leave Group</b-button>
        </b-form>
      </template>
    </b-modal>


    <b-modal :id="`${group.id}-devices-modal`" :title="`${group.name} - Devices`">
      <div
        class="alert-light alert bg-light my-0 text-center py-4"
        v-if="group.devices && group.devices.length == 0"
      >
        No devices in this group.
      </div>
      <ListItem
        v-for="device in group.devices"
        v-bind:key="device.id"
        class="d-flex justify-content-between"
      >
        {{ device.name || device.id }}
        <NavIcon 
          icon="trash-alt"
          @click="removeDevice(device.id)"
        />
      </ListItem>

      <template v-slot:modal-footer>
        <b-input-group>
          <b-form-select v-model="selectedDevice" :options="myDevices"></b-form-select>
          <b-input-group-append>
            <b-button variant="primary" @click="addDevice">Add Device</b-button>
          </b-input-group-append>
        </b-input-group>
      </template>
    </b-modal>
  </div>
</template>

<script>
import NavIcon from "@/components/NavIcon.vue";
import DeviceListItem from "@/components/DeviceListItem.vue";
import ListItem from "@/components/ListItem.vue";
import gql from "graphql-tag";

export default {
  props: {
    group: Object
  },
  components: {
    NavIcon,
    DeviceListItem,
    ListItem
  },
  methods: {
    addUser: function() {
      this.$apollo.mutate({
        mutation: gql`
          mutation($username: String!, $groupId: Int!) {
            addUserToGroup(username: $username, groupId: $groupId) {
              id
            }
          }
        `,
        variables: {
          username: this.username,
          groupId: this.group.id
        }
      }).then(() => {
        this.$bvModal.hide(`${this.group.id}-members-modal`);
        this.username = '';
      })
    },
    leave: function() {
      this.$apollo.mutate({
        mutation: gql`
          mutation($id: Int!) {
            leaveGroup(id: $id) {
              id
            }
          }
        `,
        variables: {
          id: this.group.id
        }
      }).then(() => {
        this.$bvModal.hide(`${this.group.id}-members-modal`);
        this.username = '';
      })
    },
    addDevice: function() {
      if (!this.selectedDevice) return;
      this.$apollo.mutate({
        mutation: gql`
          mutation($deviceId: String!, $groupId: Int!) {
            addDeviceToGroup(deviceId: $deviceId, groupId: $groupId) {
              id
            }
          }
        `,
        variables: {
          deviceId: this.selectedDevice,
          groupId: this.group.id
        }
      }).then(() => {
        this.$bvModal.hide(`${this.group.id}-devices-modal`);
      })
    },
    removeDevice: function(deviceId) {
      this.$apollo.mutate({
        mutation: gql`
          mutation($deviceId: String!, $groupId: Int!) {
            removeDeviceFromGroup(deviceId: $deviceId, groupId: $groupId) {
              id
            }
          }
        `,
        variables: {
          deviceId: deviceId,
          groupId: this.group.id
        }
      }).then(() => {
        this.$bvModal.hide(`${this.group.id}-devices-modal`);
      })
    }
  },
  data() {
    return {
      selectedDevice: '',
      self: {
        devices: []
      },
      username: ''
    }
  },
  computed: {
    myDevices() {
      return this.self.devices.map((device) => ({ value: device.id, text: device.id }))
    }
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
            }
          }
        }
      `,
      pollInterval: 5000
    }
  }
}
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

  .controls {
    display: flex;
  }
}

.btn.btn-primary {
  background-color: var(--accent) !important;
  border-color: var(--accent) !important;

  &:hover {
    background-color: var(--accent-darker) !important;
    border-color: var(--accent-darker) !important;
  }
}
</style>