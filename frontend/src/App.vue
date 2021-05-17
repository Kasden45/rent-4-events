<template>
<!--  <div id="app">-->
<!--    <img src="./assets/logo.png">-->
<!--    <router-view/>-->
<!--  </div>-->
  <div>

    <button
      class="btn btn-primary btn-margin"
      v-if="!authenticated"
      @click="login()">
      Log In
    </button>

    <button
      class="btn btn-primary btn-margin"
      @click="privateMessage()">
      Call Private
    </button>

    <button
      class="btn btn-primary btn-margin"
      v-if="authenticated"
      @click="logout()">
      Log Out
    </button>

    {{ message }}
    <br>
  </div>
</template>

<script>
import AuthService from './auth/AuthService'
import axios from 'axios'
import HelloWorld from './components/HelloWorld'

const API_URL = 'http://localhost:8000'
const auth = new AuthService()
export default {
  name: 'app',
  components: {
    HelloWorld
  },
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: 'a'
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/rent-rest/api/private-scoped`
      // const url = `${API_URL}/users/?query={email, username}`
      return axios.get(url, {headers: {Authorization: `Bearer ${auth.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = JSON.stringify(response.data)
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
