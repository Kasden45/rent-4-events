<template>
    <div id="courses" class="container">
        <div class="row justify-content-center">
            <div class="col-11">
                <courses-table :courses-source="courses" :key="courses" @edit:course="editCourse" @get:courses="getCourses" @delete:course="deleteCourse"/>
            </div>
        </div>
    </div>
</template>

<script>
import CoursesTable from '../components/CoursesTable'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'Courses',
  props: {
    activeUser: String
  },
  components: {
    CoursesTable,
  },
  data () {
    return {
      courses: [],
    }
  },
  methods: {
    async addCourse (course) {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, course, {headers: {Authorization: `Bearer ${token}`}})
      this.getCourses()
    },
    async getUsers () {
      const url = `${apiUrl}/users/?query={id, username}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.users = response.data['results']
        console.log(this.$auth.getIdTokenClaims())
      })
    },
    async getCourses () {
      const url = `${apiUrl}/courses/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.courses = response.data['results']

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
    // this.getUsers()
  }
}
</script>

<style scoped>

</style>
