<template>
  <div id="app">
    <DripNav :updating="updating" :updated="updated" />
    <router-view />
  </div>
</template>

<script>
import DripNav from "@/components/DripNav.vue";
import gql from "graphql-tag";

export default {
  name: "dripdash",
  components: {
    DripNav
  },
  metaInfo: {
    title: "Home",
    titleTemplate: "%s :: DripDash"
  },
  data() {
    return {
      fetchCount: 0,
      updated: new Date()
    };
  },

  computed: {
    updating: function() {
      return !!this.fetchCount;
    }
  },

  created: function() {
    document.addEventListener("apollo-status", e => {
      if (e.detail == "fetching") this.fetchCount += 1;
      if (e.detail == "fetched") {
        this.fetchCount -= 1;
        this.updated = new Date();
      }
    });
  },

  mounted: function() {
    // if we still have a current (in-date) token, check it's valid.
    if (this.$store.getters["user/isAuthenticated"]) {
      this.$apollo
        .query({
          query: gql`
            query {
              self {
                id
              }
            }
          `
        })
        .then(pl => {
          if (pl.data.self) {
            // The token was accepted by the server. Refresh to get newer token.
            this.$store.dispatch("user/refresh");
          } else {
            // The token was invalidated by the server. Require log-in.
            this.$store.dispatch("user/logout");
          }
        });
    }
  }
};
</script>

<style lang="scss">
// unscoped styles to modify html, body.
body {
  min-height: 100%;
  background-color: var(--light);
}

html {
  height: 100%;
}

:root {
  --accent: #0db8b0;
  --accent-darker: #009f97;
}
</style>
