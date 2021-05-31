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
        // console.log(response.data['results'])
        return resp
      })
    },
    async editDriver (driverData) {
      try {
        console.log(driverData)
        const driver = driverData.data[0]
        const index = driverData.data[1]
        console.log(driverData.data[1])
        const url = `${API_URL}/drivers/${driver.userId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.put(url, driver, {headers: {Authorization: `Bearer ${token}`}})
        await this.getDriverById(driver.userId, index, driverData)
      } catch (error) {
        console.log(error)
      }
    },
    async getDriverById (id, index, driverData) {
      try {
        const url = `${API_URL}/drivers/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.drivers[index] = response.data
          driverData.done()
        })
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.getDrivers()
  }
}
</script>

<style scoped>

</style>
