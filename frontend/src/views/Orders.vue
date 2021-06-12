<template>
  <div class="orders">
    <div class="row justify-content-end py-3 mw-100">
      <div class="col-3">
          <router-link class="btn btn-2" to="/Zamowienia/Nowe/">NOWE ZAMÓWIENIE</router-link>
      </div>
    </div>
    <div class="row mw-100">
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
import { api_url } from '../../auth_config.json'
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
      const url = `${api_url}/orders/`
      console.log(this.$auth.getIdTokenClaims())
      const token = await this.$auth.getTokenSilently()
      // const token = this.$auth.getIdTokenClaims()
      console.log(token)
      console.log(this.$auth.user)
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

</style>
