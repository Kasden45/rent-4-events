<template>
    <div id="vehicles-table">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Marka</th>
                    <th>Model</th>
                    <th>Rok produkcji</th>
                    <th>Nr rejestracyjny</th>
                    <th>Przegląd do</th>
                    <th>Typ</th>
                    <th>Status</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="vehicle in vehiclesSource" :key="vehicle.vehicleId">
                    <td>{{vehicle.brand}}</td>
                    <td>{{vehicle.model}}</td>
                    <td>{{vehicle.year}}</td>
                    <td>{{vehicle.licensePlate}}</td>
                    <td>{{vehicle.carServiceTo}}</td>
                    <td>{{vehicle.type}}</td>
                    <td>{{vehicle.status}}</td>
                    <td>
                        <button type="button" class="btn btn-sm btn-info" :id="vehicle.vehicleId" @click="handleEdit">Edytuj</button>
                        <button type="button" class="btn btn-sm btn-danger" @click="handleDelete(vehicle.vehicleId)">Usuń</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'VehiclesTable',
  props: {
    vehiclesSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      isEdit: false,
      editedVehicle: {
        brand: '',
        model: '',
        year: '',
        licensePlate: '',
        carServiceTo: '',
        type: '',
        status: ''
      }
    }
  },
  methods: {
    changeButtons (row) {
      var $btn1 = row.children().eq(7).children().eq(0)
      var $btn2 = row.children().eq(7).children().eq(1)

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
          this.$emit('delete:vehicle', id)
        }
      }
      else {
          console.log("Anuluj");
            this.$emit('get:vehicles')
      }
    },
    handleEdit: function (event) {
      this.isEdit = !this.isEdit

      var $vehicleId = parseInt(event.target.id)
      var $vehicleIndex = this.vehiclesSource.map(function (vehicle) {
        return vehicle.vehicleId
      }).indexOf($vehicleId)
      var $vehicle = this.vehiclesSource[$vehicleIndex]

      var $grandParent = $('#' + $vehicleId).parent().parent() // row

      var $brand = $grandParent.children().eq(0)
      var $model = $grandParent.children().eq(1)
      var $year = $grandParent.children().eq(2)
      var $licensePlate = $grandParent.children().eq(3)
      var $carServiceTo = $grandParent.children().eq(4)
      var $type = $grandParent.children().eq(5)
      var $status = $grandParent.children().eq(6)

      if (this.isEdit) {
        // disable buttons
        $('.btn-danger').not($grandParent.children().eq(7).children().eq(1)).prop('disabled', true)
        $('.btn-info').not($grandParent.children().eq(7).children().eq(0)).prop('disabled', true)

        // change controls -> form
        $brand.html(function () {
          return '<input class="form-control"/>'
        })
        $model.html(function () {
          return '<input class="form-control"/>'
        })
        $year.html(function () {
          return '<input class="form-control" type="number" min="1950" max="2021"/>'
        })
        $licensePlate.html(function () {
          return '<input class="form-control" maxlength="8"/>'
        })
        $carServiceTo.html(function () {
          return '<input class="form-control" type="date"/>'
        })
        $type.html(function () {
          return '<select  class="form-select">' +
              '  <option value="Bus">Bus</option>\n' +
              '  <option value="Ciężarówka">Ciężarówka</option>\n' +
              '</select>'
        })
        $status.html(function () {
          return '<select  class="form-select">' +
              '  <option value="Sprawny">Sprawny</option>\n' +
              '  <option value="W warsztacie">W warsztacie</option>\n' +
              '  <option value="Niesprawny">Niesprawny</option>\n' +
              '</select>'
        })
        // select values that book has
        $brand.children().val($vehicle.brand)
        $model.children().val($vehicle.model)
        $year.children().val($vehicle.year)
        $licensePlate.children().val($vehicle.licensePlate)
        $carServiceTo.children().val($vehicle.carServiceTo)
        $type.children().val($vehicle.type)
        $status.children().val($vehicle.status)
      } else {
        this.submitting = true
        this.clearStatus()

        // take values
        this.editedVehicle = {
          vehicleId: $vehicle.vehicleId,
          brand: $brand.children().val(),
          model: $model.children().val(),
          year: $year.children().val(),
          licensePlate: $licensePlate.children().val(),
          carServiceTo: $carServiceTo.children().val(),
          type: $type.children().val(),
          status: $status.children().val(),
        }

        if (this.invalidBrand || this.invalidModel || this.invalidYear || this.invalidLicensePlate || this.invalidCarServiceTo || this.invalidType || this.invalidStatus) {
          this.error = true
          this.isEdit = !this.isEdit

          return
        }

        // enable buttons
        $('.btn-danger').prop('disabled', false)
        $('.btn-info').prop('disabled', false)
        const vehicleData = [this.editedVehicle, $vehicleIndex]

        this.$emit('edit:vehicle', {data: vehicleData,
          done: () => {
            this.error = false
            this.success = true
            this.submitting = false

            $vehicle = this.vehiclesSource[$vehicleIndex]

            $brand.html(function () {
              return $vehicle.brand
            })
            $model.html(function () {
              return $vehicle.model
            })
            $year.html(function () {
              return $vehicle.year
            })
            $licensePlate.html(function () {
              return $vehicle.licensePlate
            })
            $carServiceTo.html(function () {
              return $vehicle.carServiceTo
            })
            $type.html(function () {
              return $vehicle.type
            })
            $status.html(function () {
              return $vehicle.status
            })
          }})
      }

      this.changeButtons($grandParent)
    }
  },
  computed: {
    invalidBrand () {
      return this.editedVehicle.brand === ''
    },
    invalidModel () {
      return this.editedVehicle.model === ''
    },
    invalidYear () {
      return this.editedVehicle.year < 1950
    },
    invalidLicensePlate () {
      return this.vehicle.licensePlate.length > 8
    },
    invalidCarServiceTo () {
      return this.editedVehicle.carServiceTo < '1950-01-01'
    },
    invalidType () {
      return this.editedVehicle.type === ''
    },
    invalidStatus () {
      return this.editedVehicle.status === ''
    }
  }
}
</script>

<style scoped>

</style>
