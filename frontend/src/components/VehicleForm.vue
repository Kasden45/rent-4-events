<template>
    <div id="vehicle-form">
        <form @submit.prevent="handleSubmit">
            <div class="row py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="brand-form">Marka:</label>
                        <input
                            v-model="vehicle.brand"
                            type="text"
                            class="form-control"
                            id="brand-form"
                            :class="{ 'has-error': submitting && invalidBrand}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="username-form">Typ:</label>
                        <select
                            v-model="vehicle.type"
                            type="text"
                            class="form-select"
                            id="username-form"
                            :class="{ 'has-error': submitting}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        >
                            <option
                                value="Bus"
                            >Bus</option>
                            <option
                                value="Ciężarówka"
                            >Ciężarówka</option>
                        </select>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="model-form">Model:</label>
                        <input
                            v-model="vehicle.model"
                            type="text"
                            class="form-control"
                            id="model-form"
                            :class="{ 'has-error': submitting && invalidModel}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>

            </div>
            <div class="row justify-content-between py-2">

                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="car-service-to-form">Przegląd do:</label>
                        <input
                            v-model="vehicle.carServiceTo"
                            type="date"
                            class="form-control"
                            id="car-service-to-form"
                            :class="{ 'has-error': submitting && invalidCarServiceTo}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="status-form">Status:</label>
                        <select
                            v-model="vehicle.status"
                            type="text"
                            class="form-select"
                            id="status-form"
                            :class="{ 'has-error': submitting}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        >
                            <option
                                v-for="status in statuses" :key="status"
                                :value="status"
                            >{{status}}</option>
                        </select>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="license-plate-form">Tablica rejestracyjna:</label>
                        <input
                            v-model="vehicle.licensePlate"
                            type="text"
                            class="form-control"
                            id="license-plate-form"
                            :class="{ 'has-error': submitting && invalidLicensePlate}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
            </div>
            <div class="row justify-content-between py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="year-form">Rok produkcji:</label>
                        <input
                            v-model="vehicle.year"
                            type="text"
                            class="form-control"
                            id="year-form"
                            :class="{ 'has-error': submitting && invalidYear}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>

                <div class="col-md-2 col-12 text-end align-self-end pb-2">
                    <button class="btn btn-success" id="confirm">DODAJ</button>
                </div>
            </div>

            <p v-if="error && submitting" class="error-message">
                Proszę wypełnić wskazane pola formularza
            </p>
            <p v-if="success" class="success-message">
                Dane poprawnie zapisano
            </p>
        </form>
    </div>
</template>

<script>
export default {
  name: 'VehicleForm',
  props: {
    usersSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      vehicle: {
        vehicleId: '',
        brand: '',
        model: '',
        year: '',
        licensePlate: '',
        carServiceTo: new Date().toISOString().slice(0, 10),
        type: '',
        status: ''
      },
      statuses: ['Sprawny', 'W warsztacie', 'Niesprawny']
    }
  },
  methods: {
    handleSubmit () {
      this.submitting = true
      this.clearStatus()

      if (this.invalidBrand || this.invalidModel || this.invalidYear || this.invalidLicensePlate || this.invalidCarServiceTo || this.invalidType || this.invalidStatus) {
        this.error = true
        return
      }

      this.$emit('add:vehicle', this.vehicle)

      this.vehicle = {
        vehicleId: '',
        brand: '',
        model: '',
        year: '',
        licensePlate: '',
        carServiceTo: new Date().toISOString().slice(0, 10),
        type: '',
        status: ''
      }

      this.error = false
      this.success = true
      this.submitting = false
    },
    clearStatus () {
      this.success = false
      this.error = false
    }
  },
  computed: {
    invalidBrand () {
      return this.vehicle.brand === ''
    },
    invalidModel () {
      return this.vehicle.model === ''
    },
    invalidYear () {
      return this.vehicle.year < 1950
    },
    invalidLicensePlate () {
      return this.vehicle.licensePlate.length > 8
    },
    invalidCarServiceTo () {
      return this.vehicle.carServiceTo < '1950-01-01'
    },
    invalidType () {
      return this.vehicle.type === ''
    },
    invalidStatus () {
      return this.vehicle.status === ''
    }
  }
}
</script>

<style scoped>
option {
    overflow: auto;
}

[class*='-message'] {
    font-weight: 500;
}

.error-message {
    color: #D33C40;
}

.success-message {
    color: #32A95D;
}

</style>

