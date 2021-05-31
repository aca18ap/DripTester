const state = {
  apiInterval: 5,
  uiInterval: 1,
  chartColors: ["#0db8b0", "#0468c4", "#04C44E", "#04A3CF", "#04CF8B"]
};

const getters = {
  apiIntervalms: state => state.apiInterval * 1000,
  uiIntervalms: state => state.uiInterval * 1000
};

const actions = {};

const mutations = {};

const settings = {
  namespaced: true,
  state: state,
  getters: getters,
  actions: actions,
  mutations: mutations
};

export default settings;
