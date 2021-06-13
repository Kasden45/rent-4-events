// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/fontawesome'
import App from './App'
import router from './router'
import {domain, clientId, audience, apiUrl, groups} from '../auth_config.json'
import { Auth0Plugin } from './auth'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
import axios from 'axios'
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
    getUsersDjangoRoles: async function (token) {
      const url = `${apiUrl}/users/?query={id, username, groups}`
      console.log('Url i token: ' + url + ' ' + JSON.stringify(token))
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        // return response.data['results'].find(elem => elem.id === ).groups
        return response.data['results'][0].groups
      })
      console.log('response get roles: ' + JSON.stringify(resp))
      return resp
    },
    getActiveRole: async function (token) {
      const rolesArray = await this.getUsersDjangoRoles(token)
      console.log('array' + rolesArray)
      // eslint-disable-next-line eqeqeq
      if (rolesArray.includes(groups.Admin) || rolesArray == groups.Admin) {
        return 'Admin'
        // eslint-disable-next-line eqeqeq
      } else if (rolesArray.includes(groups.Kierowca) || rolesArray == groups.Kierowca) {
        return 'Kierowca'
        // eslint-disable-next-line eqeqeq
      } else if (rolesArray.includes(groups.Klient) || rolesArray == groups.Klient) {
        return 'Klient'
      } else return 'Gość'
    }
  }
})
// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
