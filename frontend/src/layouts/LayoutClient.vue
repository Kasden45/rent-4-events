<template>
<div class="layout-client">

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
              <li class="nav-item">
                <router-link class="nav-link" to="/Zamowienia">Zamówienia</router-link>
              </li>
            </ul>
            <button
              class="btn btn-primary btn-margin"
              id="idk">
              Call Private
            </button>
            <button
              class="btn btn-primary btn-margin"
              v-if="!this.$auth.isAuthenticated"
              @click="login()">
              Log In
            </button>
            <button
              class="btn btn-primary btn-margin"
              v-if="this.$auth.isAuthenticated"
              @click="logout()">
              Log Out
            </button>
            <!-- Left links -->
          </div>
          <!-- Collapsible wrapper -->
        </div>
        <!-- Container wrapper -->
      </nav>
    <slot/>
    <my-footer/>
  </div>
</template>

<script>
import axios from 'axios'
import MyFooter from '../components/MyFooter'
// import $ from 'jquery'
import { CollapseTransition } from '@ivanv/vue-collapse-transition'

const API_URL = 'http://localhost:8000'

// const auth = new AuthService()
export default {
  name: 'LayoutClient',
  components: {MyFooter, CollapseTransition},
  data () {
    return {
      message: 'a',
      isOpen: true
    }
  },
  methods: {
    // this method calls the AuthService login() method
    login () {
      this.$auth.loginWithRedirect()
    },
    logout () {
      this.$auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/rent-rest/api/private-scoped`
      // const url = `${API_URL}/users/?query={email, username}`
      return axios.get(url, {headers: {Authorization: `Bearer ${this.$auth.getTokenSilently()}`}}).then((response) => {
        console.log(response.data)
        this.message = JSON.stringify(response.data)
      })
    }
  }
}
</script>

<style scoped>
.navbar {
  position: sticky;
}
</style>
