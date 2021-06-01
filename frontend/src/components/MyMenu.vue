<template>
  <layout-manager>
    <router-view></router-view>
  </layout-manager>
</template>

<script>
import LayoutGuest from '../layouts/LayoutGuest'
import LayoutClient from '../layouts/LayoutClient'
import LayoutManager from '../layouts/LayoutManager'
import LayoutDriver from '../layouts/LayoutDriver'
export default {
  name: 'MyMenu',
  components: {
    LayoutGuest,
    LayoutClient,
    LayoutManager,
    LayoutDriver
  }
}
</script>

<style scoped>

</style>
