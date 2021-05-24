<template>
  <div id="orders-table">
    <div class="table table-hover">
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
        <tr v-for="order in ordersSource" :key="order.orderId">
          <td>{{order.startDate}}</td>
          <td>{{order.endDate}}</td>
          <td>{{order.address}}</td>
          <td>{{order.totalCost}}</td>
          <td>{{order.status}}</td>
        </tr>
      </tbody>
    </div>

  </div>
</template>

<script>
export default {
  name: 'OrdersTable',
  props: {
    ordersSource: Array
  },
  data () {
    return {
      isEdit: false,
      editedOrder: {
        orderId: 0,
        client: 0,
        startDate: 0,
        endDate: 0,
        address: '',
        totalCost: 0,
        status: ''
      }
    }
  },
  methods: {

  }
}
</script>

<style scoped>

</style>
