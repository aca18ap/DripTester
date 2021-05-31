import Vue from "vue";

const utils = {
  parseObjectArray(obj, arr) {
    if (!Array.isArray(arr) || arr.length < 1) {
      return obj;
    }
    if (arr.length > 64) {
      throw "Object accessor array too long.";
    }
    let accessor = arr.shift();
    obj = obj[accessor];
    return this.parseObjectArray(obj, arr);
  },

  accessValue(obj, field) {
    if (Array.isArray(field)) {
      // avoid immuting field by cloning with ...spread.
      var fnew = [...field];
      return this.parseObjectArray(obj, fnew);
    }
    return obj[field];
  },

  toTitleCase(str) {
    return str.replace(/\w\S*/g, function(txt) {
      return txt.charAt(0).toUpperCase() + txt.substr(1).toLowerCase();
    });
  }
};

const plugin = {
  install() {
    Vue.utils = utils;
    Vue.prototype.$utils = utils;
  }
};

Vue.use(plugin);
