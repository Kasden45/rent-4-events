<template>
  <div id="orders-table">
      <div class="table-responsive">
          <table class="table table-hover">
          <thead>
            <tr>
              <th>Data od</th>
              <th>Data do</th>
              <th>Miejsce realizacji</th>
              <th>Koszt</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="order in ordersSource" :key="order.orderId"  @click="openPreview(order.orderId)">
              <td>{{order.startDate}}</td>
              <td>{{order.endDate}}</td>
              <td>{{order.address}}</td>
              <td>{{order.totalCost}} zł</td>
              <td>{{order.status}}</td>
            </tr>
          </tbody>
        </table>
      </div>
  </div>
</template>

<script>
export default {
  name: 'OrdersTable',
  props: {
    ordersSource: Array
  },
  methods: {
    openPreview (id) {
      this.$router.push({ name: 'OrderPreview', params: { orderId: id } })
    }
  }
}
</script>

<style scoped>

</style>
