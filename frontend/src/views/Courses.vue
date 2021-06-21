<template>
    <div>
        <div v-if="activeUser === 'Admin' || activeUser === 'Kierowca'" id="courses" class="container-fluid">
            <div class="row justify-content-center mt-5">
                <div class="col-11 px-5">
                    <h3>KURSY</h3>
                    <courses-table :courses-source="courses" :orders-source="orders" :vehicles-source="vehicles" :drivers-source="drivers" :active-user="$props.activeUser" :key="courses" @edit:course="editCourse" @get:courses="getCourses"  @delete:course="deleteCourse"/>
                </div>
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
import CoursesTable from '../components/CoursesTable'
import NoAccess from '../components/NoAccess'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'Courses',
  props: {
    activeUser: String
  },
  components: {
    CoursesTable,
    NoAccess
  },
  data () {
    return {
      courses: [],
      orders: [],
      drivers: [],
      vehicles: []
    }
  },
  methods: {
    async addCourse (course) {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, course, {headers: {Authorization: `Bearer ${token}`}})
      this.getCourses()
    },
    async getOrders () {
      const url = `${apiUrl}/orders/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.orders = response.data['results']
        console.log(this.$auth.getIdTokenClaims())
      })
    },
    async getCourses () {
      const url = `${apiUrl}/courses/?query={*,order{orderId,startDate,endDate,address,isTransport,status,comment},driver{userId,firstName,lastName,phoneNumber},%20vehicle{vehicleId,brand,model,licensePlate}}`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.courses = response.data['results']

        console.log(JSON.stringify(response.data['results']))
        return resp
      })
    },
    async getVehicles () {
      const url = `${apiUrl}/vehicles/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.vehicles = response.data['results']

        console.log(JSON.stringify(response.data['results']))
        return resp
      })
    },
    async getDrivers () {
      const url = `${apiUrl}/drivers/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.drivers = response.data['results']

        console.log(JSON.stringify(response.data['results']))
        return resp
      })
    },
    async editCourse (courseData) {
      try {
        console.log(courseData)
        const course = courseData.data[0]
        const index = courseData.data[1]
        console.log(courseData.data[1])
        const url = `${apiUrl}/courses/${course.courseId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.put(url, course, {headers: {Authorization: `Bearer ${token}`}})
        await this.getCourseById(course.courseId, index, courseData)
      } catch (error) {
        console.log(error)
      }
      this.getCourses()
    },
    async getCourseById (id, index, courseData) {
      try {
        const url = `${apiUrl}/courses/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.courses[index] = response.data
          courseData.done()
        })
      } catch (error) {
        console.log(error)
      }
    },
    async deleteCourse (id) {
      try {
        const url = `${apiUrl}/courses/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
        await this.getCourses()
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.getCourses()
    this.getOrders()
    this.getDrivers()
    this.getVehicles()
  }
}
</script>

<style scoped>

</style>
