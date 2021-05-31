<template>
  <div class="login-wrap">
    <b-card class="login">
      <h2><DripDashLogo />&nbsp;DripDash</h2>
      <b-form @submit.prevent="login">
        <b-form-group>
          <b-form-input
            id="input-1"
            v-model="form.username"
            required
            placeholder="Username"
          ></b-form-input>
        </b-form-group>
        <b-form-group>
          <b-form-input
            id="input-2"
            v-model="form.password"
            type="password"
            required
            placeholder="Password"
          ></b-form-input>
        </b-form-group>
        <b-button type="submit" block class="login-btn" variant="primary">
          Login
        </b-button>
        <hr />
        <router-link class="register" to="/register"
          >No account? Sign Up.</router-link
        >
      </b-form>
    </b-card>
  </div>
</template>

<script>
import DripDashLogo from "@/components/DripDashLogo.vue";

export default {
  name: "Login",
  components: {
    DripDashLogo
  },
  data() {
    return {
      form: {
        username: "",
        password: ""
      }
    };
  },
  methods: {
    async login() {
      const { username, password } = this.form;
      this.$store.dispatch("user/login", { username, password });
    }
  }
};
</script>

<style scoped lang="scss">
.login {
  width: 20em;
  text-align: center;
}

.register {
  color: var(--primary);
}

h2 {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5em;
}

.login-btn {
  background-color: var(--accent) !important;
  border-color: var(--accent) !important;

  &:hover {
    background-color: var(--accent-darker) !important;
    border-color: var(--accent-darker) !important;
  }
}

.login-wrap {
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
