<template>
    <div id="order-preview" class="container">
        <div class="row">
            <div class="col-11">
                <div class="row justify-content-between mt-3">
                    <div class="col-3">
                        <button class="btn btn-4" @click="goBack">POWRÓT DO ZAMÓWIEŃ</button>
                    </div>
                    <div class="col-3 text-end" v-if="order.status === 'Oczekujące'">
                        <button class="btn btn-4" @click="cancelOrder">ANULUJ ZAMÓWIENIE</button>
                    </div>
                </div>
                <div class="row justify-content-center my-3">
                    <order-preview-details :order-source="order"/>
                </div>
                <div class="row justify-content-center">
                    <order-positions-table :order-source="order"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import OrderPositionsTable from '../components/OrderPositionsTable'
import OrderPreviewDetails from '../components/OrderPreviewDetails'
import axios from 'axios'
import { api_url } from '../../auth_config.json'
export default {
  name: 'OrderPreview',
  components: {
    OrderPositionsTable,
    OrderPreviewDetails
  },
  data () {
    return {
      order: {}
    }
  },
  methods: {
    async getOrder () {
      const url = `${api_url}/orders/${this.$route.params.orderId}/?query={*,positions{*,product{prodId,prodName, quantity, price}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        console.log(response.data)
        this.order = response.data
      })
    },
    goBack () {
      this.$router.push({ name: 'Orders' })
    },
    async cancelOrder () {
      const url = `${api_url}/orders/${this.$route.params.orderId}/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        status: 'Anulowane'
      }
      await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      this.goBack()
    }
  },
  mounted () {
    this.getOrder()
  }
}
</script>

<style scoped>

</style>
