<template>
    <div id="drivers" class="container">
        <div class="row justify-content-center">
            <div class="col-11">
                <driver-form :users-source="users" @add:driver="addDriver"/>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-11">
                <drivers-table :drivers-source="drivers" @edit:driver="editDriver" @delete:driver="deleteDriver"/>
            </div>
        </div>
    </div>
</template>

<script>
import DriversTable from '../components/DriversTable'
import DriverForm from '../components/DriverForm'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'Drivers',
  props: {
    activeUser: String
  },
  components: {
    DriversTable,
    DriverForm
  },
  data () {
    return {
      drivers: [],
      users: []
    }
  },
  methods: {
    async addDriver (driver) {
      const url = `${apiUrl}/drivers/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, driver, {headers: {Authorization: `Bearer ${token}`}})
      this.getDrivers()
    },
    async getUsers () {
      const url = `${apiUrl}/users/?query={id, username}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.users = response.data['results']
        console.log(this.$auth.getIdTokenClaims())
      })
    },
    async getDrivers () {
      const url = `${apiUrl}/drivers/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.drivers = response.data['results']
        return resp
      })
    },
    async editDriver (driverData) {
      try {
        console.log(driverData)
        const driver = driverData.data[0]
        const index = driverData.data[1]
        console.log(driverData.data[1])
        const url = `${apiUrl}/drivers/${driver.userId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.put(url, driver, {headers: {Authorization: `Bearer ${token}`}})
        await this.getDriverById(driver.userId, index, driverData)
      } catch (error) {
        console.log(error)
      }
    },
    async getDriverById (id, index, driverData) {
      try {
        const url = `${apiUrl}/drivers/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.drivers[index] = response.data
          driverData.done()
        })
      } catch (error) {
        console.log(error)
      }
    },
    async deleteDriver (id) {
      try {
        const url = `${apiUrl}/drivers/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
        await this.getDrivers()
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.getDrivers()
    this.getUsers()
  }
}
</script>

<style scoped>

</style>
