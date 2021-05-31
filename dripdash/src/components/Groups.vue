<template>
  <b-container>
    <div class="heading">
      <h2>Groups</h2>
      <NavIcon
        icon="plus"
        class="add"
        @click="$bvModal.show('create-group-modal')"
      />
    </div>
    <div
      class="alert-light alert bg-light my-0 text-center py-4"
      v-if="self.groups && self.groups.length == 0"
    >
      You're not in any groups. Click '+' to create a group,
      or ask a group owner to add you.
    </div>
    <div class="groups"
      v-for="group in self.groups"
      v-bind:key="group.id"
    >
      <Group :group="group"/> 
    </div>

    <b-modal id="create-group-modal" title="Create a Group">
      <p>
        Creating a group allows you to share devices with other users, or
        group your devices together.
      </p>
      <b-form>
        <b-input placeholder="Group Name" v-model="createGroupName" />
      </b-form>

      <template v-slot:modal-footer>
        <b-button variant="primary" @click="createGroup">Create Group</b-button>
      </template>
    </b-modal>
  </b-container>
</template>

<script>
import NavIcon from "@/components/NavIcon.vue";
import Group from "@/components/Group.vue"
import gql from "graphql-tag";

export default {
  components: {
    NavIcon,
    Group
  },
  data() {
    return {
      self: {
        groups: []
      },
      createGroupName: ''
    }
  },
  methods: {
    createGroup: function() {
      this.$apollo.mutate({
        mutation: gql`
          mutation($name: String!) {
            createGroup(name: $name) {
              id
            }
          }
        `,
        variables: {
          name: this.createGroupName
        }
      }).then(() => {
        this.$bvModal.hide(`create-group-modal`);
        this.createGroupName = '';
      })
    }
  },
  apollo: {
    self: {
      query: gql`
        query {
          self {
            id
            groups {
              id
              name
              members {
                id
                username
              }
              devices {
                id
                name
                owner {
                  id
                }
                latest {
                  timestamp
                }
                status
              }
            }
          }
        }
      `,
      deep: true,
      pollInterval: 2000
    }
  }
}
</script>

<style scoped lang="scss">
.heading {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;

  h2 {
    margin: 0;
  }

  .add{
    font-size: 1.25rem;
  }
}

.alert {
  margin-top: 1rem !important;
  border: 1px solid rgba(0, 0, 0, .125);
}

.groups {
    display: grid;
    gap: 1rem;
    padding: 1rem 0;
    grid-template-columns: 1fr;

    @include lg {
      grid-template-columns: repeat(2, 1fr);
    }
  }
</style>