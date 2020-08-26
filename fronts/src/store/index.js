import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const store = new Vuex.Store({
  state: {
    backendUrl: "http://127.0.0.1:8000/",
    userUrl: "http://127.0.0.1:8000/api/user/now-user/"
  },
  mutations: {},
  actions: {},
  modules: {},
  getters: {
    getServerUrl: state => {
        return state.backendUrl
    },
    getUserUrl: state => {
        return state.userUrl
    }
  }
})

export default store
