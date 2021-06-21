<template>
<div class="container">
    <div class="row mt-3 mb-5 justify-content-center">
        <div class="col-6 text-center">
            <button class="btn btn-4 mx-3" @click="getTopClients">KLIENCI</button>
            <button class="btn btn-4 mx-3" @click="getTopProducts">PRODUKTY</button>
            <button class="btn btn-4 mx-3" @click="getTopDrivers">KIEROWCY</button>
        </div>
    </div>
    <div class="row mt-5">
        <h1 class="ms-4">{{title}}</h1>
    </div>
    <chart v-if="loaded" :chartData="chartData" :options="options"/>
</div>
</template>

<script>
import Chart from '../components/Chart'
import LineChart from '../components/LineChart'
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
export default {
  name: 'Reports',
  components: { LineChart, Chart },
  data () {
    return {
      loaded: false,
      chartData: {
        labels: [],
        datasets: []
      },
      title: ''
    }
  },
  methods: {
    async getTopClients () {
      this.loaded = false
      const url = `${apiUrl}/orders/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        let users = {}
        let values = []
        let labels = []
        response.data['results'].forEach((order) => {
          if (users.hasOwnProperty(order.client.userId)) {
            users[order.client.userId].count += 1
          } else {
            users[order.client.userId] = {
              firstName: order.client.firstName,
              lastName: order.client.lastName,
              count: 1
            }
          }
        })
        console.log(users)
        var sortedUsers = Object.entries(users).sort(function (a, b) {
          return b[1].count - a[1].count
        }).slice(0, 10)
        console.log('new:', sortedUsers)
        sortedUsers.forEach((user) => {
          labels.push(user[1].firstName + ' ' + user[1].lastName)
          values.push(user[1].count)
        })
        values.push(0)
        this.chartData.labels = labels

        this.chartData.datasets = [{
          label: 'Liczba zamówień klientów',
          backgroundColor: ['#38656C', '#D88C88', '#212529', '#38656C', '#D88C88', '#212529', '#38656C', '#D88C88', '#212529', '#38656C'],
          data: values
        }]
        this.options = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            yAxes: [{
              ticks: {
                min: 0,
                max: Math.ceil(Math.max.apply(Math, values) * 1.05),
                stepSize: 1,
                reverse: false,
                beginAtZero: true
              }
            }]
          },
          legend: {
            display: false
          }
        }
        this.loaded = true
        this.title = 'Klienci z największą liczbą zamówień'
      })
    },
    async getTopProducts () {
      this.loaded = false
      const url = `${apiUrl}/orders/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        let products = {}
        let values = []
        let labels = []
        response.data['results'].forEach((order) => {
          order.positions.forEach((position) => {
            if (products.hasOwnProperty(position.product.prodId)) {
              products[position.product.prodId].count += 1
            } else {
              products[position.product.prodId] = {
                prodName: position.product.prodName,
                count: 1
              }
            }
          })
        })
        console.log(products)
        var sortedProducts = Object.entries(products).sort(function (a, b) {
          return b[1].count - a[1].count
        }).slice(0, 10)
        console.log('new:', sortedProducts)
        sortedProducts.forEach((prod) => {
          labels.push(prod[1].prodName)
          values.push(prod[1].count)
        })
        values.push(0)
        this.chartData.labels = labels

        this.chartData.datasets = [{
          label: 'Najczęściej zamawiane produkty',
          backgroundColor: ['#38656C', '#D88C88', '#212529', '#38656C', '#D88C88', '#212529', '#38656C', '#D88C88', '#212529', '#38656C'],
          data: values
        }]
        // console.log('chart', JSON.stringify(this.chartData))
        this.options = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            yAxes: [{
              ticks: {
                min: 0,
                max: Math.ceil(Math.max.apply(Math, values) * 1.05),
                stepSize: 1,
                reverse: false,
                beginAtZero: true
              }
            }]
          },
          legend: {
            display: false
          }
        }
        this.loaded = true
        this.title = 'Najczęściej zamawiane produkty'
      })
    },
    async getTopDrivers () {
      this.loaded = false
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        let drivers = {}
        let plannedCourses = []
        let doneCourses = []
        let labels = []
        response.data['results'].forEach((course) => {
          if (drivers.hasOwnProperty(course.driver.userId)) {
            if (course.status === 'Zaplanowany') {
              drivers[course.driver.userId].countPlanned += 1
              drivers[course.driver.userId].count += 1
            } else if (course.status === 'Zrealizowany') {
              drivers[course.driver.userId].countDone += 1
              drivers[course.driver.userId].count += 1
            }
          } else if (course.status === 'Zaplanowany' || course.status === 'Zrealizowany') {
            drivers[course.driver.userId] = {
              firstName: course.driver.firstName,
              lastName: course.driver.lastName,
              countPlanned: course.status === 'Zaplanowany' ? 1 : 0,
              countDone: course.status === 'Zrealizowany' ? 1 : 0,
              count: 1
            }
          }
        })
        console.log(drivers)
        var sortedDrivers = Object.entries(drivers).sort(function (a, b) {
          return b[1].count - a[1].count
        }).slice(0, 10)
        console.log('new:', sortedDrivers)
        sortedDrivers.forEach((driver) => {
          labels.push(driver[1].firstName + ' ' + driver[1].lastName)
          plannedCourses.push(driver[1].countPlanned)
          doneCourses.push(driver[1].countDone)
        })
        plannedCourses.push(0)
        doneCourses.push(0)
        this.chartData.labels = labels
        const concatCourses = plannedCourses.concat(doneCourses)

        this.chartData.datasets = [
          {
            label: 'Liczba zaplanowanych kursów',
            backgroundColor: '#38656C',
            data: plannedCourses
          },
          {
            label: 'Liczba zrealizowanych kursów',
            backgroundColor: '#D88C88',
            data: doneCourses
          }

        ]
        // console.log('chart', JSON.stringify(this.chartData))
        this.options = {
          responsive: true,
          maintainAspectRatio: false,
          scales: {
            yAxes: [{
              ticks: {
                min: 0,
                max: Math.ceil(Math.max.apply(Math, concatCourses) * 1.05),
                stepSize: 1,
                reverse: false,
                beginAtZero: true
              }
            }]
          }
        }
        this.loaded = true
        this.title = 'Kierowcy z największą liczbą kursów'
      })
    }
  },
  mounted () {
    this.getTopProducts()
  }
}
</script>

<style scoped>

</style>
