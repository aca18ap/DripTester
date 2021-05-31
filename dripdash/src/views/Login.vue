<template>
  <div class="home">
    <b-container>
      <Login />
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Login from "@/components/Login.vue";

export default {
  name: "home",
  metaInfo: {
    title: "Login"
  },
  components: {
    Login
  }
};
</script>

<style scoped lang="scss">
.home {
  margin: 1rem;
}
</style>
