<template>
    <div>
        <div class="row justify-content-center justify-content-md-start align-items-end">
            <div class="col-md-4 col-sm-5 col-10">
                <label class="form-check-label" for="start-date">Data wypożyczenia:</label>
                <input class="form-control" type="date" id="start-date" :value="this.orderSource.startDate" @change="editOrder">
            </div>
            <div class="col-md-4 col-sm-5 col-10">
                <label class="form-check-label" for="end-date">Data zwrotu:</label>
                <input class="form-control" type="date" id="end-date" :value="this.orderSource.endDate" @change="editOrder">
            </div>
            <div class="col-md-4 col-sm-5 col-10">
                <label class="form-check-label" for="address">Adres eventu:</label>
                <input class="form-control" type="text" id="address" :value="this.orderSource.address" @change="editOrder">
            </div>
        </div>
        <div class="row justify-content-center justify-content-md-start">
            <div class="col-md-4 col-sm-5 col-10 align-self-center">
                <input class="form-check-input" type="checkbox" v-model="editedOrder.isTransport" :value="this.orderSource.isTransport" id="transport" @change="editOrder">
                <label class="form-check-label" for="transport">Transport</label>
            </div>
        </div>
    </div>

</template>

<script>
import $ from 'jquery'
export default {
  name: 'NewOrderDates',
  props: {
    orderSource: Object,
    edit: Boolean
  },
  data () {
    return {
      editedOrder: {
        client: this.orderSource.client.userId,
        startDate: this.orderSource.startDate,
        endDate: this.orderSource.endDate,
        address: this.orderSource.address,
        isTransport: this.orderSource.isTransport,
        totalCost: this.orderSource.totalCost,
        status: this.orderSource.status
      }
    }
  },
  methods: {
    editOrder () {
      this.fillData()
      const $newStart = $('#start-date')
      const $newEnd = $('#end-date')
      const $newAdress = $('#address')

      const $newStartVal = $newStart.val()
      const $newEndVal = $newEnd.val()
      const $newAddressVal = $newAdress.val()
      console.log('edited', JSON.stringify(this.editedOrder))
      console.log('source', JSON.stringify(this.orderSource))
      console.log('start', $newStartVal,'end', $newEndVal)

      if ($newStartVal <= $newEndVal) {
        this.editedOrder.startDate = $newStartVal
        this.editedOrder.endDate = $newEndVal
        this.editedOrder.address = $newAddressVal
        this.editedOrder.client = this.orderSource.client.userId
          console.log('cli' + this.editedOrder.client + ' vs ' + this.orderSource.client.userId)
        this.$emit('edit:order', this.editedOrder)
      } else {
        $newStart.val(this.orderSource.startDate)
        $newEnd.val(this.orderSource.endDate)
        $newAdress.val(this.orderSource.address)
      }
    },
    fillData () {
      if (!this.editedOrder.client) {
        this.editedOrder.client = this.orderSource.client.userId
        this.editedOrder.startDate = this.orderSource.startDate
        this.editedOrder.endDate = this.orderSource.endDate
        this.editedOrder.address = this.orderSource.address
        this.editedOrder.isTransport = this.orderSource.isTransport
        this.editedOrder.totalCost = this.orderSource.totalCost
        this.editedOrder.status = this.orderSource.status
      }
    }
  },
    mounted() {
      console.log('Mounted:' + JSON.stringify(this.orderSource))
    }
}
</script>

<style scoped>
.form-check-label {
    margin: 0px;
}
</style>
