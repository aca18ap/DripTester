<template>
  <ListItem :to="{ name: 'device', params: { id: device.id } }">
    <div class="left">
      <TriStateIcon :status="device.status" class="tristate" />
      <span class="d-name">{{ device.name || device.id }}</span>
      <span v-if="device.name" class="d-id small"> ({{ device.id }}) </span>
    </div>
    <div class="right">
      <TimeAgo
        class="online small"
        :time="timestamp"
        text="Online"
        :dynamic="true"
      />
      <Renamer
        class="rname-sa"
        v-if="detailed"
        :startText="device.name || device.id"
        @save="rename"
      />
      <NavIcon icon="trash-alt" @click="remove" v-if="detailed" />
      <!-- TODO add renamer to dropdown under sm breakpoint -->
    </div>
  </ListItem>
</template>

<script>
import NavIcon from "@/components/NavIcon.vue";
import TriStateIcon from "@/components/StateIcon.vue";
import TimeAgo from "@/components/TimeAgo.vue";
import Renamer from "@/components/Renamer.vue";
import ListItem from "@/components/ListItem.vue";
import gql from "graphql-tag";

export default {
  name: "DeviceListItem",
  components: {
    ListItem,
    NavIcon,
    TriStateIcon,
    TimeAgo,
    Renamer
  },
  props: {
    device: Object,
    detailed: {
      type: Boolean,
      required: false,
      default: true
    }
  },
  data: function() {
    return {
      timestamp: new Date(this.device.latest.timestamp)
    };
  },
  watch: {
    device: {
      deep: true,
      handler(device) {
        this.timestamp = new Date(device.latest.timestamp);
      }
    }
  },
  methods: {
    rename: function(name) {
      this.$apollo.mutate({
        mutation: gql`
          mutation($id: String!, $name: String!) {
            renameDevice(id: $id, name: $name) {
              id
              name
            }
          }
        `,
        variables: {
          id: this.device.id,
          name: name
        }
      });
    },
    remove: function() {
      this.$apollo.mutate({
        mutation: gql`
          mutation($id: String!) {
            removeDevice(id: $id)
          }
        `,

        variables: {
          id: this.device.id
        }
      });
    }
  }
};
</script>

<style scoped lang="scss">
.d-id {
  display: none;

  @include md {
    display: inline;
  }
}

.small {
  font-size: 0.85em;
  margin: 0 0.5em;
  color: var(--secondary);
}

.rname-sa {
  display: none;

  @include sm {
    display: flex;
  }
}

.right,
.left {
  display: flex;
  flex-direction: row;
  align-items: center;
}

.left {
  color: var(--dark);
}

.tristate {
  margin-right: 1rem;
}
</style>
