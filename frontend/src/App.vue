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
  // data () {
  //   return {
  //     layout: `div`
  //   }
  // }
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
