import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import store from "./store";

Vue.use(Router);
Vue.use(store);

const router = new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    {
      path: "/",
      name: "home",
      component: Home,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/add-device",
      name: "Add Device",
      component: () =>
        import(/* webpackChunkName: "add-device" */ "./views/AddDevice.vue"),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/device/:id",
      name: "device",
      component: () =>
        import(/* webpackChunkName: "device" */ "./views/Device.vue"),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/device/:id/:detail",
      name: "deviceDetail",
      component: () =>
        import(
          /* webpackChunkName: "deviceDetail" */ "./views/DeviceDetail.vue"
        ),
      meta: {
        requiresAuth: true
      }
    },
    {
      path: "/login",
      name: "login",
      // Lazy load when required
      component: () =>
        import(/* webpackChunkName: "login" */ "./views/Login.vue")
    },
    {
      path: "/register",
      name: "register",
      // Lazy load when required
      component: () =>
        import(/* webpackChunkName: "register" */ "./views/Register.vue")
    }
  ]
});

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters["user/isAuthenticated"]) {
      // We need authentication, and we have it. continue.
      return next();
    }
    // We need authentication, and we don't have it. redirect.
    return next("/login");
  }
  // No authentication flag on this route. continue.
  return next();
});

export default router;
