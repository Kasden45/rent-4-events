<template>

  <layout-manager v-if="this.active === 'Admin'" >
    <router-view :key="$route.fullPath"></router-view>
  </layout-manager>
    <layout-guest v-else-if="this.active === 'Gość'">
    <router-view :key="$route.fullPath"></router-view>
  </layout-guest>
    <layout-driver v-else-if="this.active === 'Kierowca'">
    <router-view :key="$route.fullPath"></router-view>
  </layout-driver>
    <layout-client v-else-if="this.active === 'Klient'">
    <router-view :key="$route.fullPath"></router-view>
  </layout-client>
</template>

<script>
import LayoutGuest from '../layouts/LayoutGuest'
import LayoutClient from '../layouts/LayoutClient'
import LayoutManager from '../layouts/LayoutManager'
import LayoutDriver from '../layouts/LayoutDriver'
import {api_url, groups} from "../../auth_config.json";
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
      async getActive() {

          const url = `${api_url}/users/?query={id,username,groups}`
          // const url = `${API_URL}/users/?query={email, username}`
          const token = await this.$auth.getTokenSilently()
          const active_role = await this.getActiveRole(token)
          // return axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          //     this.message = JSON.stringify(response.data.results[0])
          //     console.log("groups: " + this.message)
          // })
          console.log("Active role: " + active_role)
          this.active = active_role
      }
    },
    watch:{
        async $route(to, from) {
            await this.getActive()
        }
    } ,
    async mounted() {
        await this.getActive()
    },
    async beforeRouteEnter() {
      await this.getActive()
    }
}
</script>

<style scoped>

</style>
