import router from "../router";
import { apolloClient } from "../plugins/apollo";
import gql from "graphql-tag";
import jwt from "jsonwebtoken";

const state = {
  token: localStorage.getItem("user-token") || "",
  status: "",
  refreshTimeout: ""
};

const getters = {
  isAuthenticated: state => {
    if (!state.token) return false;
    const body = jwt.decode(state.token);
    return body.exp * 1000 - Date.now() > 0;
  }
};

const actions = {
  // Request an auth token
  login: ({ commit }, user) => {
    return new Promise((res, rej) => {
      // Set the state to authenticated whilst we wait for a response.
      commit("loading");

      apolloClient
        .mutate({
          mutation: gql`
            mutation($username: String!, $password: String!) {
              login(username: $username, password: $password)
            }
          `,

          variables: {
            username: user.username,
            password: user.password
          }
        })
        .then(pl => {
          const token = pl.data.login;
          if (!token) {
            localStorage.removeItem("user-token");
            return rej("Invalid credentials.");
          }

          // Note: decoding does not verify the content signature.
          // As we trust the server, we do not need to verify the sig.
          const body = jwt.decode(token);

          // Schedule a token refresh for 30s before expiry
          // const tillRefresh = new Date(body.exp * 1000) - Date.now() - 30000;
          // const refreshTimeout = setTimeout(() => {
          //   // TODO: add refresh
          // }, tillRefresh);

          // Save the auth token, and log in!
          localStorage.setItem("user-token", token);
          commit("login", token);

          // Reset the GraphQL store, as the data available will change.
          apolloClient.resetStore();

          router.push({ path: "/" });
          res(body.id);
        });
    });
  },

  refresh: ({ commit, dispatch }) => {
    return new Promise((res, rej) => {
      // Set the state to refreshing.
      commit("loading");
      apolloClient
        .mutate({
          mutation: gql`
            mutation {
              refresh
            }
          `
        })
        .then(pl => {
          const token = pl.data.refresh;
          if (!token) {
            localStorage.removeItem("user-token");
            dispatch("logout");
            return rej("Couldn't refresh token.");
          }

          localStorage.setItem("user-token", token);
          commit("login", token);

          res("Token refreshed.");
        });
    });
  },

  logout: ({ commit }) => {
    return new Promise(resolve => {
      commit("logout");
      localStorage.removeItem("user-token"); // clear your user's token from localstorage
      // dispatch("device/reset", {}, { root: true });
      // dispatch("nav/setBc", [], { root: true });
      router.push({ path: "/login" });
      resolve();
    });
  },

  register: ({ commit, dispatch }, { username, password }) => {
    return new Promise((res, rej) => {
      commit("loading");

      apolloClient
        .mutate({
          mutation: gql`
            mutation($username: String!, $password: String!) {
              register(username: $username, password: $password)
            }
          `,

          variables: {
            username,
            password
          }
        })
        .then(pl => {
          if (!pl.data.register) return rej("Unable to create user.");

          res(dispatch("login", { username, password }));
        });
    });
  }

  // register: ({ commit, dispatch }, user) => {
  //   if (user.password != user.passwordConf) {
  //     commit("error");
  //     return;
  //   } else {
  //     return new Promise((resolve, reject) => {
  //       axios({ url: "/api/auth/create", data: user, method: "POST" })
  //         .then(resp => {
  //           // account created, complete log-in.
  //           dispatch("user/request", user);
  //           resolve(resp);
  //         })
  //         .catch(err => {
  //           commit("error", err);
  //           reject(err);
  //         });
  //     });
  //   }
  // }
};

const mutations = {
  loading: state => {
    state.status = "loading";
    clearTimeout(state.refreshTimeout);
  },
  login: (state, token) => {
    state.status = "authenticated";
    state.token = token;
  },
  logout: state => {
    state.token = "";
  },
  refresh: state => {
    clearTimeout(state.refreshTimeout);
    state.status = "refreshing";
  },
  nextRefresh: (state, timeout) => {
    state.refreshTimeout = timeout;
  }
};

const user = {
  namespaced: true,
  state: state,
  getters: getters,
  actions: actions,
  mutations: mutations
};

export default user;
