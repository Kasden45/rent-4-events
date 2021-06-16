<template>
    <div id="courses-table">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Zamowienie</th>
                    <th>Kierowca</th>
                    <th>Pojazd</th>
                    <th>Data kursu</th>
                    <th>Typ</th>
                    <th>Status</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="course in coursesSource" :key="course.courseId">
                    <td>{{course.order}}</td>
                    <td>{{course.driver}}</td>
                    <td>{{course.vehicle}}</td>
                    <td>{{course.courseDate}}</td>
                    <td>{{course.type}}</td>
                    <td>{{course.status}}</td>
                    <td>
                        <button type="button" class="btn btn-sm btn-info" :id="course.courseId" @click="handleEdit">Edytuj</button>
                        <button type="button" class="btn btn-sm btn-danger" @click="handleDelete(course.courseId)">Usuń</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'CoursesTable',
  props: {
    coursesSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      isEdit: false,
      editedCourse: {
        courseId: '',
        order: '',
        driver: '',
        vehicle: '',
        courseDate: '',
        type: '',
        status: ''
      }
    }
  },
  methods: {
    changeButtons (row) {
      var $btn1 = row.children().eq(6).children().eq(0)
      var $btn2 = row.children().eq(6).children().eq(1)

      if (this.isEdit) {
        $btn1.html('Zapisz')
        $btn1.attr('class', 'btn btn-success btn-sm')
        $btn2.html('Anuluj')
      } else {
        $btn1.html('Edytuj')
        $btn1.attr('class', 'btn btn-info btn-sm')
        $btn2.html('Usuń')
      }
    },
    clearStatus () {
      this.success = false
      this.error = false
    },

    handleDelete (id) {
      if (!this.isEdit) {
        if (confirm('Czy na pewno chcesz usunąć ten pojazd?')) {
          this.$emit('delete:course', id)
        }
      }
      else {
          console.log("Anuluj");
            this.$emit('get:courses')
      }
    },
    handleEdit: function (event) {
      this.isEdit = !this.isEdit

        console.log('cou2' + parseInt(event.target))
      var $courseId = parseInt(event.target.id)

        console.log('cou' + $courseId)
      var $courseIndex = this.coursesSource.map(function (course) {
        return course.courseId
      }).indexOf($courseId)
      var $course = this.coursesSource[$courseIndex]
      var $grandParent = $('#' + $courseId).parent().parent() // row

      var $order = $grandParent.children().eq(0)
      var $driver = $grandParent.children().eq(1)
      var $vehicle = $grandParent.children().eq(2)
      var $courseDate = $grandParent.children().eq(3)
      var $type = $grandParent.children().eq(4)
      var $status = $grandParent.children().eq(5)

      if (this.isEdit) {
        // disable buttons
        $('.btn-danger').not($grandParent.children().eq(6).children().eq(1)).prop('disabled', true)
        $('.btn-info').not($grandParent.children().eq(6).children().eq(0)).prop('disabled', true)

        // change controls -> form
        $order.html(function () {
          return '<input class="form-control"/>'
        })
        $driver.html(function () {
          return '<input class="form-control"/>'
        })
        $vehicle.html(function () {
          return '<input class="form-control"/>'
        })
        $courseDate.html(function () {
          return '<input class="form-control" type="date"/>'
        })
        $type.html(function () {
          return '<select  class="form-select">' +
              '  <option value="Dostawa">Dostawa</option>\n' +
              '  <option value="Odbiór">Odbiór</option>\n' +
              '</select>'
        })
        $status.html(function () {
          return '<select  class="form-select">' +
              '  <option value="Zaplanowany">Zaplanowany</option>\n' +
              '  <option value="W trasie">W trasie</option>\n' +
              '  <option value="Zrealizowany">Zrealizowany</option>\n' +
              '</select>'
        })
        // select values that book has
        $order.children().val($course.order)
        $driver.children().val($course.driver)
        $vehicle.children().val($course.vehicle)
        $courseDate.children().val($course.courseDate)
        $type.children().val($course.type)
        $status.children().val($course.status)
      } else {
        this.submitting = true
        this.clearStatus()

        // take values
        this.editedCourse = {
          courseId: $course.courseId,
          order: $order.children().val(),
          driver: $driver.children().val(),
          vehicle: $vehicle.children().val(),
          courseDate: $courseDate.children().val(),
          type: $type.children().val(),
          status: $status.children().val(),
        }

        if (this.invalidOrder || this.invalidDriver || this.invalidVehicle || this.invalidCourseDate || this.invalidCarServiceTo || this.invalidType || this.invalidStatus) {
          this.error = true
          this.isEdit = !this.isEdit

          return
        }

        // enable buttons
        $('.btn-danger').prop('disabled', false)
        $('.btn-info').prop('disabled', false)
        const courseData = [this.editedCourse, $courseIndex]

        this.$emit('edit:course', {data: courseData,
          done: () => {
            this.error = false
            this.success = true
            this.submitting = false

            $course = this.coursesSource[$courseIndex]

            $order.html(function () {
              return $course.order
            })
            $driver.html(function () {
              return $course.driver
            })
            $vehicle.html(function () {
              return $course.vehicle
            })
            $courseDate.html(function () {
              return $course.courseDate
            })
            $type.html(function () {
              return $course.type
            })
            $status.html(function () {
              return $course.status
            })
          }})
      }

      this.changeButtons($grandParent)
    }
  },
  computed: {
    invalidOrder () {
      return this.editedCourse.order === ''
    },
    invalidDriver () {
      return this.editedCourse.driver === ''
    },
    invalidVehicle () {
      return this.editedCourse.vehicle === ''
    },
    invalidCourseDate () {
      return this.editedCourse.courseDate < '1950-01-01'
    },
    invalidType () {
      return this.editedCourse.type === ''
    },
    invalidStatus () {
      return this.editedCourse.status === ''
    }
  }
}
</script>

<style scoped>

</style>
