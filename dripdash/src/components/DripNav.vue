<template>
  <b-navbar class="navbar" variant="white" toggleable="md">
    <b-container class="nav-cont">
      <b-navbar-brand to="/" class="logo">
        <DripDashLogo color="var(--accent)" />
      </b-navbar-brand>
      <BreadcrumbButton
        v-if="this.bc.length > 0 && $store.getters['user/isAuthenticated']"
        @toggle="switcher"
        v-bind:bc="this.bc"
        class="bc-btn"
      />

      <b-navbar-nav
        v-if="$store.getters['user/isAuthenticated']"
        class="updater"
      >
        <UpdateCandy :updating="this.updating" :updated="this.updated" />
      </b-navbar-nav>

      <b-navbar-nav class="ml-auto">
        <!-- <NavIcon icon="cog" /> -->
        <NavIcon
          v-if="$store.getters['user/isAuthenticated']"
          icon="power-off"
          @click="$store.dispatch('user/logout')"
        />
      </b-navbar-nav>
    </b-container>
  </b-navbar>
</template>

<script>
import BreadcrumbButton from "@/components/BreadcrumbButton.vue";
import DripDashLogo from "@/components/DripDashLogo.vue";
import NavIcon from "@/components/NavIcon.vue";
import UpdateCandy from "@/components/UpdateCandy.vue";

export default {
  name: "DripNav",
  props: {
    updated: [Date, Number],
    updating: Boolean
  },
  computed: {
    bc() {
      return this.$store.state.nav.bc;
    }
  },
  data() {
    return {
      isSwitching: false
    };
  },
  methods: {
    switcher(e) {
      this.isSwitching = e;
    }
  },
  components: {
    BreadcrumbButton,
    DripDashLogo,
    NavIcon,
    UpdateCandy
  }
};
</script>

<style scoped lang="scss">
.bc-btn {
  flex-grow: 1;
  margin: 0 1em;
}

.logo {
  margin-right: 0;
}

.updater {
  display: none;
}

@include sm {
  .bc-btn {
    flex-grow: 0;
    margin: 0;
  }

  .logo {
    margin-right: 1rem;
  }

  .updater {
    display: block;
  }

  .nav-cont {
    padding: 0 15px;
  }
}

.nav-cont {
  display: flex;
  flex-direction: row;
}

.navbar {
  flex-direction: column;
}
</style>
