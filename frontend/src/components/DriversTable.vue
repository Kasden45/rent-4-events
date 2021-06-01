<template>
    <div id="drivers-table">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Imię</th>
                    <th>Nazwisko</th>
                    <th>Data urodzenia</th>
                    <th>Data zatrudnienia</th>
                    <th>Pensja</th>
                    <th>Numer telefonu</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="driver in driversSource" :key="driver.userId">
                    <td>{{driver.firstName}}</td>
                    <td>{{driver.lastName}}</td>
                    <td>{{driver.birthDate}}</td>
                    <td>{{driver.employmentDate}}</td>
                    <td>{{driver.salary}}</td>
                    <td>{{driver.phoneNumber}}</td>
                    <td>
                        <button type="button" class="btn btn-sm btn-info" :id="driver.userId" @click="handleEdit">Edytuj</button>
                        <button type="button" class="btn btn-sm btn-danger" @click="handleDelete(driver.userId)">Usuń</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'DriversTable',
  props: {
    driversSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      isEdit: false,
      editedDriver: {
        firstName: '',
        lastName: '',
        birthDate: '',
        employmentDate: '',
        salary: '',
        phoneNumber: ''
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
        if (confirm('Are you sure you want to delete this driver?')) {
          this.$emit('delete:driver', id)
        }
      }
    },
    handleEdit: function (event) {
      this.isEdit = !this.isEdit

      // get book
      var $driverId = parseInt(event.target.id)
      var $driverIndex = this.driversSource.map(function (driver) {
        return driver.userId
      }).indexOf($driverId)
      var $driver = this.driversSource[$driverIndex]

      var $grandParent = $('#' + $driverId).parent().parent() // row

      var $firstName = $grandParent.children().eq(0)
      var $lastName = $grandParent.children().eq(1)
      var $birthDate = $grandParent.children().eq(2)
      var $employmentDate = $grandParent.children().eq(3)
      var $salary = $grandParent.children().eq(4)
      var $phoneNumber = $grandParent.children().eq(5)

      if (this.isEdit) {
        // disable buttons
        $('.btn-danger').not($grandParent.children().eq(6).children().eq(1)).prop('disabled', true)
        $('.btn-info').not($grandParent.children().eq(6).children().eq(0)).prop('disabled', true)

        // change controls -> form
        $firstName.html(function () {
          return '<input class="form-control"/>'
        })
        $lastName.html(function () {
          return '<input class="form-control"/>'
        })
        $birthDate.html(function () {
          return '<input class="form-control" type="date"/>'
        })
        $employmentDate.html(function () {
          return '<input class="form-control" type="date"/>'
        })
        $salary.html(function () {
          return '<input class="form-control"/>'
        })
        $phoneNumber.html(function () {
          return '<input class="form-control"/>'
        })
        // select values that book has
        $firstName.children().val($driver.firstName)
        $lastName.children().val($driver.lastName)
        $birthDate.children().val($driver.birthDate)
        $employmentDate.children().val($driver.employmentDate)
        $salary.children().val($driver.salary)
        $phoneNumber.children().val($driver.phoneNumber)
      } else {
        this.submitting = true
        this.clearStatus()

        // take values
        this.editedDriver = {
          userId: $driver.userId,
          firstName: $firstName.children().val(),
          lastName: $lastName.children().val(),
          birthDate: $birthDate.children().val(),
          employmentDate: $employmentDate.children().val(),
          salary: $salary.children().val(),
          phoneNumber: $phoneNumber.children().val()
        }

        if (this.invalidFirstName || this.invalidLastName || this.invalidBirthDate || this.invalidEmploymentDate || this.invalidSalary || this.invalidPhoneNumber) {
          this.error = true
          this.isEdit = !this.isEdit

          return
        }

        // enable buttons
        $('.btn-danger').prop('disabled', false)
        $('.btn-info').prop('disabled', false)
        const driverData = [this.editedDriver, $driverIndex]

        this.$emit('edit:driver', {data: driverData,
          done: () => {
            this.error = false
            this.success = true
            this.submitting = false

            $driver = this.driversSource[$driverIndex]

            $firstName.html(function () {
              return '<td>' + $driver.firstName + '</td>'
            })
            $lastName.html(function () {
              return '<td>' + $driver.lastName + '</td>'
            })
            $birthDate.html(function () {
              return '<td>' + $driver.birthDate + '</td>'
            })
            $employmentDate.html(function () {
              return '<td>' + $driver.employmentDate + '</td>'
            })
            $salary.html(function () {
              return '<td>' + $driver.salary + '</td>'
            })
            $phoneNumber.html(function () {
              return '<td>' + $driver.phoneNumber + '</td>'
            })
          }})
      }

      this.changeButtons($grandParent)
    }
  },
  computed: {
    invalidFirstName () {
      return this.editedDriver.firstName === ''
    },
    invalidLastName () {
      return this.editedDriver.lastName === ''
    },
    invalidBirthDate () {
      return this.editedDriver.birthDate === ''
    },
    invalidEmploymentDate () {
      return this.editedDriver.employmentDate === ''
    },
    invalidSalary () {
      return this.editedDriver.salary < 0
    },
    invalidPhoneNumber () {
      return this.editedDriver.phoneNumber.length !== 9
    }
  }
}
</script>

<style scoped>

</style>
