// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import './plugins/fontawesome'
import App from './App'
import router from './router'
import { domain, clientId, audience } from '../auth_config.json'
import { Auth0Plugin } from './auth'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap'
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

// eslint-disable-next-line no-new
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
