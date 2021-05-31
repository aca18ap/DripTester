<template>
  <div class="login-wrap">
    <b-card class="register">
      <h2><DripDashLogo />&nbsp;DripDash</h2>
      <p>
        Welcome to DripDash, your new aquaponics dashboard. <br />
        Let's get you registered, It'll only take a moment.
      </p>
      <b-form @submit.prevent="register">
        <b-form-group>
          <b-form-input
            id="input-1"
            v-model="form.username"
            required
            placeholder="Username"
          ></b-form-input>
        </b-form-group>
        <p class="small">
          Passwords with upper and lowercase characters, numbers and symbols are
          typically more secure.
        </p>
        <b-form-group>
          <b-form-input
            id="input-2"
            v-model="form.password"
            type="password"
            required
            placeholder="Password"
          ></b-form-input>
        </b-form-group>
        <b-form-group>
          <b-form-input
            id="input-3"
            v-model="form.passwordConf"
            type="password"
            required
            placeholder="Confirm Password"
          ></b-form-input>
        </b-form-group>
        <div class="alert alert-danger" v-if="error">{{ error }}</div>
        <b-button type="submit" block class="login-btn" variant="primary">
          Register
        </b-button>
        <hr />
        <router-link class="login" to="/login"
          >Have an account? Login.</router-link
        >
      </b-form>
    </b-card>
  </div>
</template>

<script>
import DripDashLogo from "@/components/DripDashLogo.vue";
export default {
  name: "Register",
  components: {
    DripDashLogo
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
        passwordConf: ""
      },
      error: ""
    };
  },
  methods: {
    register() {
      const { username, password, passwordConf } = this.form;
      if (password !== passwordConf) {
        this.error = "Password & Password confirmation don't match.";
        return;
      }
      this.error = "";
      this.$store.dispatch("user/register", { username, password });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
.register {
  width: 28em;
  text-align: center;
}

.login {
  color: var(--primary);
}

h2 {
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  margin-bottom: 0.5em;
}

.error {
  margin: 1rem 0;
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

.small {
  font-size: 0.85em;
  color: var(--secondary);
}
</style>
