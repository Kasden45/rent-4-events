<template>
    <div class="row">
        <div class="col-11">
            <current-course-details :order-source="order" :course-source="course" :courses-source="courses"/>
        </div>

    </div>
</template>

<script>
import CurrentCourseDetails from '../components/CurrentCourseDetails'
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
// import $ from 'jquery'
export default {
  name: 'CurrentCourse',
  components: {CurrentCourseDetails},
  data () {
    return {
      order: {},
      course: {},
      courses: [],
      currentDate: new Date().toISOString().slice(0, 10)
    }
  },
  methods: {
    async getCourses () {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.course = response.data['results'].find(course => course.status === 'W trasie')
        // console.log('dzisiaj', this.currentDate)
        // console.log(this.course)
        if (typeof this.course === 'undefined') {
          // console.log('puste')
          this.courses = response.data['results'].filter(course => course.courseDate === this.currentDate && course.status === 'Zaplanowany')
        }
        // console.log('kurs', this.course)
        // console.log('kursy', this.courses)
      })
    },
    async getOrder () {
      if (typeof this.course !== 'undefined') {
        const url = `${apiUrl}/orders/${this.course.order}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.order = response.data
          // console.log(this.order)
        })
      }
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
