const state = {
  bc: []
};

const getters = {};

const actions = {
  setBc: ({ commit }, bc) => {
    commit("setBreadcrumbs", bc);
  }
};

const mutations = {
  setBreadcrumbs: (state, bc) => {
    state.bc = bc;
  }
};

const nav = {
  namespaced: true,
  state: state,
  getters: getters,
  actions: actions,
  mutations: mutations
};

export default nav;
