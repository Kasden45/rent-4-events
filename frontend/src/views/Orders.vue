<template>
  <div class="orders">
    <div class="row justify-content-end my-3">
      <div class="col-3">
          <router-link class="btn btn-primary btn-primary" to="/Zamowienia/Nowe">NOWE ZAMÓWIENIE</router-link>
      </div>
    </div>
    <div class="row">
      <div class="col align-content-center px-5">

        <h1>Zamówienia</h1>
        <orders-table :orders-source="orders"/>

      </div>
    </div>
  </div>
</template>

<script>
import OrdersTable from '../components/OrdersTable'
import axios from 'axios'
const API_URL = 'http://localhost:8000'
export default {
  name: 'Orders',
  components: {
    OrdersTable
  },
  data () {
    return {
      orders: []
    }
  },
  methods: {
    async getOrders () {
      const url = `${API_URL}/orders/`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      // const token = this.$auth.getIdTokenClaims()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        console.log(JSON.stringify(response.data))
        this.orders = response.data['results']
        return resp
      })
    }
  },
  mounted () {
    this.getOrders()
  }
}
</script>

<style scoped>
h1 {
  color: #000000;
}

.order {
  background: #000000;
  height: 80vh;
  border-radius: 10px 0px 0px 10px;
}

</style>
