<template>
  <div class="layout-guest">

        <!-- Navbar -->
      <nav class="navbar navbar-expand-lg navbar-dark bg-dark fixed-top">
        <!-- Container wrapper -->
        <div class="container-fluid">
          <!-- Navbar brand -->
          <a class="navbar-brand" href="#">
            <img src="../logo/logo_transparent_cropped.png" alt="Logo" width="150px" height="auto">
          </a>

          <!-- Toggle button -->
          <button
            class="navbar-toggler"
            type="button"
            data-mdb-toggle="collapse"
            data-mdb-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <i class="fas fa-bars"></i>
          </button>

          <!-- Collapsible wrapper -->
          <div class="collapse navbar-collapse" id="navbarSupportedContent">
            <!-- Left links -->
            <ul class="navbar-nav me-auto">
              <li class="nav-item">
                <router-link class="nav-link" to="/">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Oferta">Oferta</router-link>
              </li>
            </ul>
            <button
              class="btn btn-primary btn-margin"
              @click="privateMessage()">
              Call Private
            </button>
            <button
              class="btn btn-primary btn-margin"
              v-if="!authenticated"
              @click="login()">
              Log In
            </button>
            <button
              class="btn btn-primary btn-margin"
              v-if="authenticated"
              @click="logout()">
              Log Out
            </button>
            <!-- Left links -->
          </div>
          <!-- Collapsible wrapper -->
        </div>
        <!-- Container wrapper -->
      </nav>
      <!-- Navbar -->
    {{ message }}
    <br>
    <slot/>
    <my-footer/>
  </div>
</template>

<script>
import AuthService from '../auth/AuthService'
import axios from 'axios'
import MyFooter from '../components/MyFooter'

const API_URL = 'http://localhost:8000'
const auth = new AuthService()
export default {
  name: 'LayoutGuest',
  components: {MyFooter},
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

<style scoped>

</style>
