<template>
  <layout-client>
    <router-view></router-view>
  </layout-client>
</template>

<script>
import LayoutGuest from '../layouts/LayoutGuest'
import LayoutClient from '../layouts/LayoutClient'
export default {
  name: 'MyMenu',
  components: {
    LayoutGuest,
    LayoutClient
  }
}
</script>

<style scoped>

</style>
