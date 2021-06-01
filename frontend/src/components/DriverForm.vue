<template>
    <div id="driver-form">
        <form @submit.prevent="handleSubmit">
            <div class="row py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="username-form">Użytkownik:</label>
                        <select
                            v-model="driver.userId"
                            type="text"
                            class="form-select"
                            id="username-form"
                            options="usersSource"
                            :class="{ 'has-error': submitting}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        >
                            <option
                                v-for="user in usersSource" :key="user.id"
                                :value="user.id"
                            >{{user.username}}</option>
                        </select>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="first-name-form">Imię:</label>
                        <input
                            v-model="driver.firstName"
                            type="text"
                            class="form-control"
                            id="first-name-form"
                            :class="{ 'has-error': submitting && invalidFirstName}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="last-name-form">Nazwisko:</label>
                        <input
                            v-model="driver.lastName"
                            type="text"
                            class="form-control"
                            id="last-name-form"
                            :class="{ 'has-error': submitting && invalidLastName}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>

            </div>
            <div class="row justify-content-between py-2">

                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="birth-date-form">Data urodzenia:</label>
                        <input
                            v-model="driver.birthDate"
                            type="date"
                            class="form-control"
                            id="birth-date-form"
                            :class="{ 'has-error': submitting && invalidBirthDate}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="employment-date-form">Data zatrudnienia:</label>
                        <input
                            v-model="driver.employmentDate"
                            type="date"
                            class="form-control"
                            id="employment-date-form"
                            :class="{ 'has-error': submitting && invalidEmploymentDate}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="phone-number-form">Numer telefonu:</label>
                        <input
                            v-model="driver.phoneNumber"
                            type="text"
                            class="form-control"
                            id="phone-number-form"
                            :class="{ 'has-error': submitting && invalidPhoneNumber}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
            </div>
            <div class="row justify-content-between py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="salary-form">Pensja:</label>
                        <input
                            v-model="driver.salary"
                            type="text"
                            class="form-control"
                            id="salary-form"
                            :class="{ 'has-error': submitting && invalidSalary}"
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
  name: 'DriverForm',
  props: {
    usersSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      driver: {
        userId: '',
        firstName: '',
        lastName: '',
        birthDate: '',
        employmentDate: new Date().toISOString().slice(0, 10),
        salary: '',
        phoneNumber: ''
      }
    }
  },
  methods: {
    handleSubmit () {
      this.submitting = true
      this.clearStatus()

      if (this.invalidFirstName || this.invalidLastName || this.invalidBirthDate || this.invalidEmploymentDate || this.invalidSalary || this.invalidPhoneNumber) {
        this.error = true
        return
      }

      this.$emit('add:driver', this.driver)

      this.driver = {
        userId: '',
        firstName: '',
        lastName: '',
        birthDate: '',
        employmentDate: '',
        salary: '',
        phoneNumber: ''
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
    invalidFirstName () {
      return this.driver.firstName === ''
    },
    invalidLastName () {
      return this.driver.lastName === ''
    },
    invalidBirthDate () {
      return this.driver.birthDate === ''
    },
    invalidEmploymentDate () {
      return this.driver.employmentDate === ''
    },
    invalidSalary () {
      return this.driver.salary === '' || parseFloat(this.driver.salary) < 0
    },
    invalidPhoneNumber () {
      return this.driver.phoneNumber.length !== 9
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
