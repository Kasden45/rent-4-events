<template>
    <div id="course-details">
        <div class="row justify-content-center mt-3">
            <div class="col-11">
                <div id="one-course" v-if="typeof courseSource !== 'undefined'">
                    <div class="row">
                        <div class="col-6">
                            <h3>AKTUALNY KURS</h3>
                        </div>
                        <div class="col-6 text-end">
                            <button class="btn btn-4">ZAKOŃCZ KURS</button>
                        </div>
                    </div>
                    <div class="row">
                        <div class="col-7">
                            <div class="row my-3">
                                <div class="col-6">
                                    <span>DATA:</span>
                                    <span>{{courseSource.courseDate}}</span>
                                </div>
                                <div class="col-6">
                                    <span>TYP:</span>
                                    <span>{{courseSource.type}}</span>
                                </div>
                            </div>
                            <div class="row my-3">
                                <div class="col-6">
                                    <span>Z:</span>
                                    <span v-if="courseSource.type === 'Dostawa'">UL. KOŚCIERZYŃSKA 9 WROCŁAW</span>
                                    <span v-else>{{orderSource.address}}</span>
                                </div>
                                <div class="col-6">
                                    <span>DO:</span>
                                    <span v-if="courseSource.type === 'Dostawa'">{{orderSource.address}}</span>
                                    <span v-else>UL. KOŚCIERZYŃSKA 9 WROCŁAW</span>
                                </div>
                            </div>
                            <div class="row my-3">
                                <div class="col-6">
                                    <span>POJAZD:</span>
                                    <span>{{courseSource.vehicle.brand}} {{courseSource.vehicle.model}} {{courseSource.vehicle.licensePlate}}</span>
                                </div>
                                <div class="col-6">
                                    <span>KLIENT:</span>
                                    <span>{{courseSource.client.firstName}} {{courseSource.client.lastName}}</span>
                                </div>
                            </div>
                            <div class="row my-3">
                                <div class="col-6 offset-6">
                                    <span>KONTAKT:</span>
                                    <span>{{courseSource.client.phoneNumber}}</span>
                                </div>
                            </div>
                        </div>
                        <div class="col-5">

                        </div>
                    </div>
                </div>
                <div id="today-courses" v-else>
                </div>
            </div>

        </div>
    </div>
</template>

<script>
export default {
  name: 'CurrentCourseDetails',
  props: {
    orderSource: Object,
    coursesSource: Array,
    courseSource: Object
  }
}
</script>

<style scoped>

</style>
