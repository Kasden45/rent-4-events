// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/fontawesome'
import App from './App'
import router from './router'
import {domain, clientId, audience, api_key, api_url, groups} from '../auth_config.json'
import { Auth0Plugin } from './auth'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import axios from "axios";
// import $ from 'jquery'

Vue.use(Auth0Plugin, {
  domain,
  clientId,
  audience,
  onRedirectCallback: appState => {
    router.push(
      appState && appState.targetUrl
        ? appState.targetUrl
        : window.location.pathname
    )
  }
})

Vue.config.productionTip = false
Vue.mixin({
  methods: {
    getUsersWithRole: function (role_id) {
      axios.get(`https://${domain}/api/v2/roles/${role_id}/users`, {headers: {Authorization: `Bearer ${api_key}`}}).then((response) => {
        console.log("Users with role" + JSON.stringify(response.data))
      })
      },
      getUsersRole: function (user_id) {
        //
        axios.get(`https://${domain}/api/v2/roles/${role_id}/users`, {headers: {Authorization: `Bearer ${api_key}`}}).then((response) => {
        console.log("Users with role" + JSON.stringify(response.data))
      })
      },
      getUsersDjangoRoles: async function (token) {
        const url = `${api_url}/users/?query={id, username, groups}`
          console.log("Url i token: " + url + " " + JSON.stringify(token))
          const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {

              return response.data['results'][0].groups
          })
          console.log("response get roles: " + JSON.stringify(resp))
          return resp
      },
      getActiveRole: async function (token) {
        const roles_array = await this.getUsersDjangoRoles(token)
          console.log("array" + roles_array)
        if (roles_array.includes(groups.Admin) || roles_array == groups.Admin) {
            return "Admin"
        }
        else if (roles_array.includes(groups.Kierowca) || roles_array == groups.Kierowca) {
            return "Kierowca"
        }
        else if (roles_array.includes(groups.Klient) || roles_array == groups.Klient) {
            return "Klient"
        }
        else return "Gość"
      }
    },
})
// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
