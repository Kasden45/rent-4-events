<template>
  <div id="app">
    <my-menu>
      <img src="./assets/logo.png">
      <router-view></router-view>
    </my-menu>

      <!--  </div>-->
<!--  <div>-->

  </div>
</template>

<script>
import MyMenu from './components/MyMenu'
// import LayoutGuest from './layouts/LayoutGuest'
export default {
  name: 'app',
  components: {
    MyMenu
  }

}
</script>

<style>
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #FFFFFF;
}
</style>
