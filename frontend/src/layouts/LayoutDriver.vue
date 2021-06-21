<template>
<div class="layout-driver">

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
                <router-link class="nav-link" to="/" v-bind:class= "[$route.matched.some(({ name }) => name === 'Home') ? {'active': true} : {}]">Home</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Oferta" v-bind:class= "[$route.matched.some(({ name }) => name === 'Offer' || name === 'ProductPreview') ? {'active': true} : {}]">Oferta</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Zamowienia" v-bind:class= "[$route.matched.some(({ name }) => name === 'Orders' || name === 'OrderPreview') ? {'active': true} : {}]">Zamówienia</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Pojazdy" v-bind:class= "[$route.matched.some(({ name }) => name === 'Vehicles') ? {'active': true} : {}]">Pojazdy</router-link>
              </li>
              <li class="nav-item">
                <router-link class="nav-link" to="/Kursy" v-bind:class= "[$route.matched.some(({ name }) => name === 'Courses') ? {'active': true} : {}]">Moje kursy</router-link>
              </li>
                <li class="nav-item">
                <router-link class="nav-link" to="/AktualnyKurs" v-bind:class= "[$route.matched.some(({ name }) => name === 'CurrentCourse') ? {'active': true} : {}]">Aktualny kurs</router-link>
              </li>
            </ul>
            <button
              class="btn btn-4 mx-2"
              v-if="!this.$auth.isAuthenticated"
              @click="login()">
              Zaloguj się
            </button>
            <button
              class="btn btn-4 mx-2"
              v-if="this.$auth.isAuthenticated"
              @click="logout()">
              Wyloguj się
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
export default {
  name: 'LayoutDriver',
  components: {MyFooter},
  methods: {
    // this method calls the AuthService login() method
    login () {
      this.$auth.loginWithRedirect()
    },
    logout () {
      this.$auth.logout()
    }
  }
}
</script>

<style scoped>
.navbar {
  position: sticky;
}

.nav-link:focus, .nav-link:hover, .active {
    border-bottom: 1px solid var(--COLOR4);
}
</style>
