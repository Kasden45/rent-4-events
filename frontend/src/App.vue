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
  color: #000000;
}

.btn-1 {
    color: #fff;
    background-color: var(--COLOR1);
    border-color: var(--COLOR1);
}

.btn-2 {
    color: #fff;
    background-color: var(--COLOR2);
    border-color: var(--COLOR2);
}

.btn-3 {
    color: #fff;
    background-color: var(--COLOR3);
    border-color: var(--COLOR3);
}

.btn-4 {
    color: #fff;
    background-color: var(--COLOR4);
    border-color: var(--COLOR4);
}

.btn {
    border-radius: 0px;
}
</style>
