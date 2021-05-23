<template>
  <layout-guest>
    <router-view></router-view>
  </layout-guest>
</template>

<script>
import LayoutGuest from '../layouts/LayoutGuest'
export default {
  name: 'MyMenu',
  components: {
    LayoutGuest
  }
}
</script>

<style scoped>

</style>
