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
  color: var(--COLOR1);
}

.btn-1, .btn-outline-1:hover {
    color: #fff;
    background-color: var(--COLOR1);
    border-color: var(--COLOR1);
}

.btn-1:hover, .btn-outline-1 {
    color: var(--COLOR1);
    border-color: var(--COLOR1);
    background-color: #FFFFFF;
}

.btn-2, .btn-outline-2:hover {
    color: #fff;
    background-color: var(--COLOR2);
    border-color: var(--COLOR2);
}

.btn-2:hover, .btn-outline-2 {
    color: var(--COLOR2);
    border-color: var(--COLOR2);
    background-color: #FFFFFF;
}

.btn-3, .btn-outline-3:hover {
    color: #fff;
    background-color: var(--COLOR3);
    border-color: var(--COLOR3);
}

.btn-3:hover, .btn-outline-3{
    color: var(--COLOR3);
    border-color: var(--COLOR3);
    background-color: #FFFFFF;
}

.btn-4, .btn-outline-4:hover {
    color: #fff;
    background-color: var(--COLOR4);
    border-color: var(--COLOR4);
}

.btn-4:hover, .btn-outline-4 {
    color: var(--COLOR4);
    border-color: var(--COLOR4);
    background-color: #FFFFFF;
}

.btn {
    border-radius: 0;
}
</style>
