<template>
    <div>
        <div v-if="activeUser === 'Kierowca'" class="row justify-content-center mt-5">
            <div class="col-11 px-5">
                <current-course-details :key="detailsKey" :order-source="order" :course-source="course" :courses-source="courses" :map-address="mapAddress" @rerender:course="forceRerender"/>
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
import CurrentCourseDetails from '../components/CurrentCourseDetails'
import NoAccess from '../components/NoAccess'
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
export default {
  name: 'CurrentCourse',
  props: {
    activeUser: String
  },
  components: { CurrentCourseDetails, NoAccess },
  data () {
    return {
      order: {},
      course: {},
      courses: [],
      currentDate: new Date().toISOString().slice(0, 10),
      mapAddress: '',
      detailsKey: 0
    }
  },
  methods: {
    async getCourses () {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        const curCourse = response.data['results'].find(course => course.status === 'W trasie')
        this.course = curCourse
        if (typeof curCourse !== 'undefined') {
          const address = curCourse.order.address.replace(' ', '+')
          this.mapAddress = `https://maps.google.com/maps?q=${address}&output=embed`
        }

        // console.log('dzisiaj', this.currentDate)
        // console.log(this.course)
        if (typeof this.course === 'undefined') {
          // console.log('puste')
          this.courses = response.data['results'].filter(course => course.courseDate === this.currentDate && course.status === 'Zaplanowany')
        }
        console.log('kurs', this.course)
        console.log('kursy', this.courses)
      })
    },
    async getOrder () {
      if (typeof this.course !== 'undefined') {
        const url = `${apiUrl}/orders/${this.course.order.orderId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.order = response.data
          // console.log(this.order)
        })
      }
    },
    forceRerender () {
      this.getCourses().then(() => {
        this.getOrder()
      })
      this.detailsKey += 1
      console.log('key', this.detailsKey)
    }
  },
  mounted () {
    this.getCourses().then(() => {
      this.getOrder()
    })
  }
}
</script>

<style scoped>

</style>
