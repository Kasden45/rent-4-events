<template>
    <div id="vehicles" class="container-fluid">
        <div v-if="activeUser === 'Admin' || activeUser === 'Kierowca'" class="row justify-content-center mt-5">
            <div class="col-11 px-5">
                <h3>POJAZDY</h3>
            </div>
        </div>
        <div v-if="activeUser === 'Admin'" class="row mw-100 justify-content-center">
            <div class="col-11 px-5">
                <vehicle-form @add:vehicle="addVehicle"/>
            </div>
        </div>
        <div v-if="activeUser === 'Admin' || activeUser === 'Kierowca'" class="row justify-content-center">
            <div class="col-11 align-content-center px-5">
                <vehicles-table :vehicles-source="vehicles" :active-user="$props.activeUser" :key="vehicles" @edit:vehicle="editVehicle" @get:vehicles="getVehicles" @delete:vehicle="deleteVehicle"/>
            </div>
        </div>
        <div v-else class="row justify-content-center">
            <div class="col-11 align-content-center px-5">
                <no-access/>
            </div>
        </div>
    </div>
</template>

<script>
import VehiclesTable from '../components/VehiclesTable'
import VehicleForm from '../components/VehicleForm'
import NoAccess from '../components/NoAccess'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'Vehicles',
  props: {
    activeUser: String
  },
  components: {
    NoAccess,
    VehiclesTable,
    VehicleForm
  },
  data () {
    return {
      vehicles: []
    }
  },
  methods: {
    async addVehicle (vehicle) {
      const url = `${apiUrl}/vehicles/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, vehicle, {headers: {Authorization: `Bearer ${token}`}})
      this.getVehicles()
    },
    async getUsers () {
      const url = `${apiUrl}/users/?query={id, username}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.users = response.data['results']
        console.log(this.$auth.getIdTokenClaims())
      })
    },
    async getVehicles () {
      const url = `${apiUrl}/vehicles/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.vehicles = response.data['results']
        return resp
      })
    },
    async editVehicle (vehicleData) {
      try {
        console.log(vehicleData)
        const vehicle = vehicleData.data[0]
        const index = vehicleData.data[1]
        console.log(vehicleData.data[1])
        const url = `${apiUrl}/vehicles/${vehicle.vehicleId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.put(url, vehicle, {headers: {Authorization: `Bearer ${token}`}})
        await this.getVehicleById(vehicle.vehicleId, index, vehicleData)
      } catch (error) {
        console.log(error)
      }
    },
    async getVehicleById (id, index, vehicleData) {
      try {
        const url = `${apiUrl}/vehicles/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.vehicles[index] = response.data
          vehicleData.done()
        })
      } catch (error) {
        console.log(error)
      }
    },
    async deleteVehicle (id) {
      try {
        const url = `${apiUrl}/vehicles/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
        await this.getVehicles()
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.getVehicles()
    // this.getUsers()
  }
}
</script>

<style scoped>

</style>
