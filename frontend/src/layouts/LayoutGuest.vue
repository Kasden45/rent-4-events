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
            data-bs-toggle="collapse"
            data-bs-target="#navbarSupportedContent"
            aria-controls="navbarSupportedContent"
            aria-expanded="false"
            aria-label="Toggle navigation"
          >
            <font-awesome-icon icon="bars"></font-awesome-icon>
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

<!--            <div v-if="!$auth.loading">-->
<!--              &lt;!&ndash; show login when not authenticated &ndash;&gt;-->
<!--              <button v-if="!$auth.isAuthenticated" @click="login">Log in</button>-->
<!--              &lt;!&ndash; show logout when authenticated &ndash;&gt;-->
<!--              <button v-if="$auth.isAuthenticated" @click="logout">Log out</button>-->
<!--            </div>-->

            <button
              class="btn btn-4 mx-2"
              @click="privateMessage()">
              Call Private
            </button>
            <button
              class="btn btn-4 mx-2"
              v-if="!this.$auth.isAuthenticated"
              @click="login()">
              Log In
            </button>
            <button
              class="btn btn-4 mx-2"
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
    <br>
    <slot/>
    <my-footer/>
  </div>
</template>

<script>
// import AuthService from '../auth/AuthService'
import axios from 'axios'
import MyFooter from '../components/MyFooter'

import { apiUrl } from '../../auth_config.json'
// const auth = new AuthService()
export default {
  name: 'LayoutGuest',
  components: {MyFooter},
  methods: {
    // this method calls the AuthService login() method
    login () {
      this.$auth.loginWithRedirect()
    },
    logout () {
      this.$auth.logout()
    },
    privateMessage () {
      const url = `${apiUrl}/rent-rest/api/private-scoped`
      // const url = `${API_URL}/users/?query={email, username}`
      return axios.get(url, {headers: {Authorization: `Bearer ${this.$auth.getTokenSilently()}`}}).then((response) => {
        console.log(response.data)
        this.message = JSON.stringify(response.data)
      })
    },
    mounted () {
      this.$emit('edit:order', this.editedOrder)
    }
  }
}
</script>

<style scoped>
.navbar {
  position: sticky;
}

.nav-link:focus, .nav-link:hover {
    border-bottom: 1px solid var(--COLOR4);
}
</style>
