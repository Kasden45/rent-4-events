<template>

  <layout-manager v-if="this.active === 'Admin'" >
    <router-view :activeUser="active" :key="$route.fullPath"></router-view>
  </layout-manager>
    <layout-guest v-else-if="this.active === 'Gość'">
    <router-view :activeUser="active" :key="$route.fullPath"></router-view>
  </layout-guest>
    <layout-driver v-else-if="this.active === 'Kierowca'">
    <router-view :activeUser="active" :key="$route.fullPath"></router-view>
  </layout-driver>
    <layout-client v-else-if="this.active === 'Klient'">
    <router-view :activeUser="active" :key="$route.fullPath"></router-view>
  </layout-client>
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
  },
  data () {
    return {
      active: 'Gość'
    }
  },
  methods: {
    async getActive () {
      // const url = `${apiUrl}/users/?query={id,username,groups}`
      // const url = `${API_URL}/users/?query={email, username}`
      const token = await this.$auth.getTokenSilently()
      const activeRole = await this.getActiveRole(token)
      // return axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
      //     this.message = JSON.stringify(response.data.results[0])
      //     console.log("groups: " + this.message)
      // })
      console.log('Active role: ' + activeRole)
      this.active = activeRole
    }
  },
  watch: {
    async $route (to, from) {
      await this.getActive()
    }
  },
  async mounted () {
    await this.getActive()
  },
  async beforeRouteEnter () {
    await this.getActive()
  }
}
</script>

<style scoped>

</style>
