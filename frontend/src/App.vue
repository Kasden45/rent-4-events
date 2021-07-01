<template>
  <div id="app">
    <my-menu>
      <img src="./assets/logo.png">
      <router-view></router-view>
    </my-menu>

  </div>
</template>

<script>
import MyMenu from './components/MyMenu'
export default {
  name: 'app',
  components: {
    MyMenu
  }
}
</script>

<style>
@import "./assets/colors.css";
#app {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: var(--COLOR1)!important;
}

.btn-1, .btn-outline-1:hover, .btn-1:focus {
    color: #fff!important;
    background-color: var(--COLOR1)!important;
    border-color: var(--COLOR1)!important;
}

.btn-1:hover, .btn-outline-1:focus, .btn-outline-1 {
    color: var(--COLOR1)!important;
    border-color: var(--COLOR1)!important;
    background-color: #FFFFFF!important;
}

.btn-2, .btn-outline-2:hover, .btn-2:focus {
    color: #fff!important;
    background-color: var(--COLOR2)!important;
    border-color: var(--COLOR2)!important;
}

.btn-2:hover, .btn-outline-2:focus, .btn-outline-2 {
    color: var(--COLOR2)!important;
    border-color: var(--COLOR2)!important;
    background-color: #FFFFFF!important;
}

.btn-3, .btn-outline-3:hover, .btn-3:focus {
    color: #fff!important;
    background-color: var(--COLOR3)!important;
    border-color: var(--COLOR3)!important;
}

.btn-3:hover, .btn-outline-3:focus, .btn-outline-3{
    color: var(--COLOR3)!important;
    border-color: var(--COLOR3)!important;
    background-color: #FFFFFF!important;
}

.btn-4, .btn-outline-4:hover, .btn-4:focus {
    color: #fff!important;
    background-color: var(--COLOR4)!important;
    border-color: var(--COLOR4)!important;
}

.btn-4:hover, .btn-outline-4:focus, .btn-outline-4 {
    color: var(--COLOR4)!important;
    border-color: var(--COLOR4)!important;
    background-color: #FFFFFF!important;
}

.btn {
    border-radius: 0!important;
}

</style>
