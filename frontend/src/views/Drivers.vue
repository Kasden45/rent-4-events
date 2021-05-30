<template>
    <div id="drivers" class="container">
        <div class="row justify-content-center">
            <div class="col-11">
                <drivers-table :drivers-source="drivers" @edit:driver="editDriver"/>
            </div>
        </div>
    </div>
</template>

<script>
import DriversTable from '../components/DriversTable'
import axios from 'axios'
const API_URL = 'http://localhost:8000'
export default {
  name: 'Drivers',
  components: {
    DriversTable
  },
  data () {
    return {
      drivers: []
    }
  },
  methods: {
    async getDrivers () {
      const url = `${API_URL}/drivers/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.drivers = response.data['results']
        return resp
      })
    },
    async editDriver (driver) {
      try {
        const url = `${API_URL}/drivers/${driver.userId}/`
        const token = await this.$auth.getTokenSilently()
        return axios.put(url, driver, {headers: {Authorization: `Bearer ${token}`}})
      } catch (error) {
        console.log(error)
      }
      location.reload()
    }
  },
  mounted () {
    this.getDrivers()
  }
}
</script>

<style scoped>

</style>
