<template>
    <div class="row">
        <div class="col-sm-5 col-12">
            <label class="form-check-label" for="start-date">Data wypożyczenia:</label>
            <input class="form-control" type="date" id="start-date" :value="this.orderSource.startDate" @change="editOrder">
        </div>
        <div class="col-sm-5 col-12">
            <label class="form-check-label" for="end-date">Data zwrotu:</label>
            <input class="form-control" type="date" id="end-date" :value="this.orderSource.endDate" @change="editOrder">
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'NewOrderDates', //FIX
  props: {
    orderSource: Object
  },
  data () {
    return {
      editedOrder: {
        client: this.orderSource.client,
        startDate: this.orderSource.startDate,
        endDate: this.orderSource.endDate,
        address: this.orderSource.address,
        totalCost: this.orderSource.totalCost,
        status: this.orderSource.status
      }
    }
  },
  methods: {
    editOrder () {
      const $newStart = $('#start-date')
      const $newEnd = $('#end-date')

      const $newStartVal = $newStart.val()
      const $newEndVal = $newEnd.val()

      if ($newStartVal <= $newEndVal) {
        this.editedOrder.startDate = $newStartVal
        this.editedOrder.endDate = $newEndVal
        this.$emit('edit:order', this.editedOrder)
      } else {
        $newStart.val(this.orderSource.startDate)
        $newEnd.val(this.orderSource.endDate)
      }
    }
  }
}
</script>

<style scoped>

</style>
