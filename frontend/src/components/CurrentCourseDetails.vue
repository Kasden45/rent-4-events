<template>
    <div id="course-details">
        <div id="one-course" v-if="typeof courseSource !== 'undefined'">
            <div class="row">
                <div class="col-6">
                    <h3>AKTUALNY KURS</h3>
                </div>
                <div class="col-6 text-end">
                    <button class="btn btn-4" @click="endCourse">ZAKOŃCZ KURS</button>
                </div>
            </div>
            <div class="row mt-3">
                <div class="col-md-7 col-12">
                    <div class="row my-3">
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">DATA:</span>
                                </div>
                                <div class="col-8">
                                    <span>{{courseSource.courseDate}}</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">TYP:</span>
                                </div>
                                <div class="col-8">
                                    <span class="text-uppercase">{{courseSource.type}}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">Z:</span>
                                </div>
                                <div class="col-8">
                                    <span class="text-uppercase" v-if="courseSource.type === 'Dostawa'">UL. KOŚCIERZYŃSKA 9 WROCŁAW</span>
                                    <span class="text-uppercase" v-else>{{orderSource.address}}</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">DO:</span>
                                </div>
                                <div class="col-8">
                                    <span class="text-uppercase" v-if="courseSource.type === 'Dostawa'">{{orderSource.address}}</span>
                                    <span class="text-uppercase" v-else>UL. KOŚCIERZYŃSKA 9 WROCŁAW</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">POJAZD:</span>
                                </div>
                                <div class="col-8">
                                    <span class="text-uppercase">{{courseSource.vehicle.brand}} {{courseSource.vehicle.model}} {{courseSource.vehicle.licensePlate}}</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-lg-6 col-12">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">KLIENT:</span>
                                </div>
                                <div class="col-8">
                                    <span class="text-uppercase">{{orderSource.client.firstName}} {{orderSource.client.lastName}}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="row my-3">
                        <div class="col-lg-6 col-12 offset-lg-6">
                            <div class="row">
                                <div class="col-4">
                                    <span class="fw-bolder">KONTAKT:</span>
                                </div>
                                <div class="col-8">
                                    <span>{{orderSource.client.phoneNumber}}</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="col-md-5 col-12">
                    <iframe :src="mapAddress" width="100%" height="100%" frameborder="0" style="border:0" allowfullscreen></iframe>
                </div>
            </div>
            <div class="row mt-3" id="accordion">
                <div class="accordion accordion-flush">
                    <div class="accordion-item">
                        <h2 class="accordion-header" id="headingOne">
                            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#order-details" aria-expanded="true" aria-controls="order-details">
                                Szczegóły zamówienia
                            </button>
                        </h2>
                        <div id="order-details" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
                            <div class="accordion-body">
                                <div class="row justify-content-center my-3">
                                    <order-preview-details :order-source="orderSource" :active-user="$props.activeUser"/>
                                </div>
                                <div class="row justify-content-center">
                                    <order-positions-table :order-source="orderSource" :active-user="$props.activeUser"/>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div id="today-courses" v-else-if="coursesSource.length > 0">
            <h3>DZISIEJSZE KURSY</h3>
            <div id="courses-table">
                <table class="table table-hover">
                    <thead>
                        <tr>
                            <th>Adres</th>
                            <th>Pojazd</th>
                            <th>Typ</th>
                            <th></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="course in coursesSource" :key="course.courseId" :id="'id_'+course.courseId">
                            <td>{{course.order.address}}</td>
                            <td>{{course.vehicle.brand}} {{course.vehicle.model}} {{course.vehicle.licensePlate}}</td>
                            <td>{{course.type}}</td>
                            <td>
                                <button type="button" class="btn btn-sm btn-4" @click="startCourse(course.courseId)">Rozpocznij</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <div id="no-courses" v-else>
            <p>Nie masz kursów zaplanowanych na dzisiaj</p>
        </div>

    </div>
</template>

<script>
import OrderPreviewDetails from './OrderPreviewDetails'
import OrderPositionsTable from './OrderPositionsTable'
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
export default {
  name: 'CurrentCourseDetails',
  props: {
    orderSource: Object,
    coursesSource: Array,
    courseSource: Object,
    mapAddress: String
  },
  components: {
    OrderPositionsTable,
    OrderPreviewDetails
  },

  methods: {
    async endCourse () {
      const url = `${apiUrl}/courses/${this.courseSource.courseId}/`
      const token = await this.$auth.getTokenSilently()
      const course = {
        status: 'Zrealizowany'
      }
      await axios.patch(url, course, {headers: {Authorization: `Bearer ${token}`}}).then(() => {
        this.$emit('rerender:course')
      })
    },
    async startCourse (id) {
      const url = `${apiUrl}/courses/${id}/`
      const token = await this.$auth.getTokenSilently()
      const course = {
        status: 'W trasie'
      }
      await axios.patch(url, course, {headers: {Authorization: `Bearer ${token}`}}).then(() => {
        this.$emit('rerender:course')
      })
    }
  }
}
</script>

<style scoped>
.accordion-button:hover, .accordion-button:focus, .accordion-button:not(.collapsed) {
    background-color: var(--COLOR2);
    color: #FFFFFF;
}

.accordion-button::after {
    color: #FFFFFF;
}

#no-courses {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    text-align: center;
    min-height: 50vh;
}

#no-courses p {
    font-size: 150%;
}
</style>
