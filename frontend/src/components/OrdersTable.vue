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
            <tr v-for="order in filters" :key="order.orderId" v-bind:style=" order.isEdited ? 'background-color: #D88C88;' : ''"  @click="openPreview(order.orderId)">
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
// import $ from 'jquery'
export default {
  name: 'OrdersTable',
  props: {
    ordersSource: Array,
    activeUser: String
  },
  methods: {
    openPreview (id) {
      this.$router.push({ name: 'OrderPreview', params: { orderId: id } })
    }
  },
  computed: {
    filters () {
      return this.ordersSource.filter(item => item.status !== 'Robocze')
    }
  }
}
</script>

<style scoped>

</style>
