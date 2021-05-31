<template>
  <div class="home">
    <b-container>
      <Register />
    </b-container>
  </div>
</template>

<script>
// @ is an alias to /src
import Register from "@/components/Register.vue";

export default {
  name: "home",
  metaInfo: {
    title: "Register"
  },
  components: {
    Register
  }
};
</script>

<style scoped lang="scss">
.home {
  margin: 1rem;
}
</style>
