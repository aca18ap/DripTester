import Vue from "vue";
import "./plugins/bootstrap-vue";
import "./plugins/font-awesome-vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import "./plugins/utils";
import VueMeta from "vue-meta";
import apolloProvider from "./plugins/apollo";

Vue.config.productionTip = false;
Vue.use(VueMeta);

window._dripdash = new Vue({
  router,
  store,
  apolloProvider,
  render: h => h(App)
}).$mount("#app");
