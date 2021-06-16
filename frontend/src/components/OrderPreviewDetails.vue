<template>
    <div id="order-preview-details">
        <div class="row">
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Początek wypożyczenia:</span>
                <span>{{this.orderSource.startDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Koniec wypożyczenia:</span>
                <span>{{this.orderSource.endDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Adres:</span>
                <span>{{this.orderSource.address}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Transport:</span>
                <font-awesome-icon v-if="orderSource.isTransport" icon="check"></font-awesome-icon>
                <font-awesome-icon v-if="!orderSource.isTransport" icon="times"></font-awesome-icon>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Status:</span>
                <span>{{this.orderSource.status}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Koszt całkowity:</span>
                <span>{{this.orderSource.totalCost}}</span>
            </div>
            <div class="col-sm-6 col-12" v-if="activeUser === 'Klient' || !statusArray.includes(orderSource.status)">
                <span class="fw-bolder">Komentarz:</span>
                <p>{{this.orderSource.comment}}</p>
            </div>
        </div>
        <div class="row mt-md-4" v-if="activeUser === 'Admin' && statusArray.includes(orderSource.status)">
            <div class="col-md-8 col-sm-12 col-12">
                <div class="form-group">
                    <label  class="fw-bolder" for="comment">Komentarz:</label>
                    <textarea class="form-control" id="comment" :value="this.orderSource.comment" rows="4"></textarea>
                </div>
            </div>
            <div class="col-md-4 col-12 my-auto">
                <button class="btn btn-2 my-1 mx-auto btn-width d-block" v-if="orderSource.isTransport && orderSource.status !== 'Do realizacji'" data-bs-toggle="modal" data-bs-target="#coursesModal">Zaakceptuj</button>
                <button class="btn btn-2 my-1 mx-auto btn-width d-block" v-if="!orderSource.isTransport && orderSource.status !== 'Do realizacji'" @click="changeStatus('Do realizacji')">Zaakceptuj</button>
                <button class="btn btn-3 my-1 mx-auto btn-width d-block" v-if="orderSource.status !== 'W trakcie negocjacji'" @click="changeStatus('W trakcie negocjacji')">Zaproponuj zmiany</button>
                <button class="btn btn-4 my-1 mx-auto btn-width d-block" v-if="orderSource.status !== 'Odrzucone'" @click="changeStatus('Odrzucone')">Odrzuć</button>
            </div>
        </div>
        <div class="modal fade" id="coursesModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" >
            <div class="modal-dialog modal-lg modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header mx-3">
                        <h5 class="modal-title" id="exampleModalLabel">Dodaj kursy do zamówienia</h5>
                        <button  class="btn btn-sm btn-4" id="btn-close" data-bs-dismiss="modal" aria-label="Close">
                          <font-awesome-icon icon="times" size="lg"/>
                        </button>
                    </div>
                    <div class="modal-body mx-3">
                        <div class="row">
                            <div class="col-6">
                                <p class="fw-bolder font">DOSTAWA</p>
                            </div>
                            <div class="col-6">
                                <p class="fw-bolder font">ODBIÓR</p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <label class="form-check-label" for="vehicleTo">Samochód:</label>
                                <select class="form-select" id="vehicleTo" aria-label="Default select example">
                                    <option v-for="vehicle in vehicles" :value="vehicle.vehicleId" :key="vehicle.vehicleId">{{ vehicle.brand }} {{ vehicle.model }} {{ vehicle.licensePlate }}</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="form-check-label" for="vehicleFrom">Samochód:</label>
                                <select class="form-select" id="vehicleFrom" aria-label="Default select example">
                                    <option v-for="vehicle in vehicles" :value="vehicle.vehicleId" :key="vehicle.vehicleId">{{ vehicle.brand }} {{ vehicle.model }} {{ vehicle.licensePlate }}</option>
                                </select>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <label class="form-check-label" for="driverTo">Kierowca:</label>
                                <select class="form-select" id="driverTo" aria-label="Default select example">
                                    <option v-for="driver in drivers" :value="driver.userId" :key="driver.userId">{{ driver.firstName }} {{ driver.lastName }}</option>
                                </select>
                            </div>
                            <div class="col-6">
                                <label class="form-check-label" for="driverFrom">Kierowca:</label>
                                <select class="form-select" id="driverFrom" aria-label="Default select example">
                                    <option v-for="driver in drivers" :value="driver.userId" :key="driver.userId">{{ driver.firstName }} {{ driver.lastName }}</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="modal-footer m-3">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Zamknij</button>
                        <button type="button" class="btn btn-4" @click="addCourses">Dodaj kursy</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
import $ from 'jquery'
export default {
  name: 'OrderPreviewDetails',
  props: {
    orderSource: Object,
    activeUser: String
  },
  data () {
    return {
      statusArray: ['W trakcie negocjacji', 'Oczekujące', 'Odrzucone', 'Do realizacji'],
      vehicles: [],
      drivers: []
    }
  },
  methods: {
    async changeStatus (status) {
      const comment = $('#comment').val()
      const url = `${apiUrl}/orders/${this.$route.params.orderId}/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        status: status,
        comment: comment,
        isEdited: false
      }
      await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      await this.$router.push({name: 'Orders'})
    },
    async getVehicles () {
      const url = `${apiUrl}/vehicles/?query={vehicleId, brand, model, licensePlate}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.vehicles = response.data['results']
        console.log(JSON.stringify(this.vehicles))
      })
    },
    async getDrivers () {
      const url = `${apiUrl}/drivers/?query={userId, firstName, lastName}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.drivers = response.data['results']
        console.log(JSON.stringify(this.drivers))
      })
    },
    async addCourses () {
      const vehicleTo = $('#vehicleTo option').filter(':selected').val()
      const vehicleFrom = $('#vehicleFrom option').filter(':selected').val()
      const driverTo = $('#driverTo option').filter(':selected').val()
      const driverFrom = $('#driverFrom option').filter(':selected').val()
      console.log(vehicleTo)
      console.log(vehicleFrom)
      console.log(driverTo)
      console.log(driverFrom)
      const courseTo = {
        order: this.orderSource.orderId,
        driver: driverTo,
        vehicle: vehicleTo,
        courseDate: this.orderSource.startDate,
        type: 'Dostawa',
        status: 'Zaplanowany'
      }
      const courseFrom = {
        order: this.orderSource.orderId,
        driver: driverFrom,
        vehicle: vehicleFrom,
        courseDate: this.orderSource.endDate,
        type: 'Odbiór',
        status: 'Zaplanowany'
      }
      console.log(JSON.stringify(courseTo))
      console.log(JSON.stringify(courseFrom))
      await this.addCourse(courseTo)
      await this.addCourse(courseFrom)
      await this.changeStatus('Do realizacji')
    },
    async addCourse (course) {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      $('#btn-close').click()
      await axios.post(url, course, {headers: {Authorization: `Bearer ${token}`}})
    }
  },
  mounted () {
    setTimeout(() => {
      if (this.orderSource.isTransport) {
        this.getVehicles()
        this.getDrivers()
      }
    }, 500)
  }
}
</script>

<style scoped>
.btn-width {
    width: 160px;
}

.font {
    font-size: 150%;
}
</style>
