<template>
<div class="layout-manager">

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
              <li class="nav-item">
                <router-link class="nav-link" to="/Zamowienia">Zamówienia</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/Kadra">Kadra</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/Pojazdy">Pojazdy</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/Kursy">Kursy</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/Asortyment">Asortyment</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/Raporty">Raporty</router-link>
              </li>
            </ul>
            <button
              class="btn btn-4 mx-2"
              id="idk"
              @click="getActive()">
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
    <slot/>
    <my-footer/>
  </div>
</template>

<script>
import MyFooter from '../components/MyFooter'
import authRoles from '../../auth_config.json'
// const API_URL = 'http://localhost:8000'

// const auth = new AuthService()
export default {
  name: 'LayoutManager',
  components: {MyFooter},
  data () {
    return {
      message: 'a',
      roles: authRoles,
      user_token: this.$auth.getTokenSilently()
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
    // privateMessage () {
    //   const url = `${apiUrl}/api/private-scoped`
    //   // const url = `${API_URL}/users/?query={email, username}`
    //
    //   return axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
    //     console.log(response.data)
    //     this.message = JSON.stringify(response.data)
    //   })
    // },
    async getActive () {
      // const url = `${apiUrl}/users/?query={id,username,groups}`
      // const url = `${API_URL}/users/?query={email, username}`
      const token = await this.$auth.getTokenSilently()
      var activeRole = await this.getActiveRole(token)
      // return axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
      //     this.message = JSON.stringify(response.data.results[0])
      //     console.log("groups: " + this.message)
      // })
      console.log('Active role: ' + activeRole)
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
