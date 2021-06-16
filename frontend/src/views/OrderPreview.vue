<template>
    <div id="order-preview" class="container">
        <div class="row">
            <div class="col-11">
                <div class="row justify-content-between mt-3">
                    <div class="col-4">
                        <button class="btn btn-4" @click="goBack">POWRÓT DO ZAMÓWIEŃ</button>
                    </div>
                    <div class="col-5 offset-2 text-end" v-if="activeUser === 'Klient' && (order.status === 'Oczekujące' || order.status === 'W trakcie negocjacji')">
                        <button class="btn btn-4" @click="editOrder">EDYTUJ</button>
                        <button class="btn btn-4" @click="cancelOrder">ANULUJ ZAMÓWIENIE</button>
                    </div>
                </div>
                <div class="row justify-content-center my-3">
                    <order-preview-details v-if="order" :order-source="order" :active-user="$props.activeUser"/>
                </div>
                <div class="row justify-content-center">
                    <order-positions-table :order-source="order" :active-user="$props.activeUser"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import OrderPositionsTable from '../components/OrderPositionsTable'
import OrderPreviewDetails from '../components/OrderPreviewDetails'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'OrderPreview',
  props: {
    activeUser: String
  },
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
      const url = `${apiUrl}/orders/${this.$route.params.orderId}/?query={*,positions{*,product{prodId,prodName, quantity, available, price}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        console.log(response.data)
        this.order = response.data
        console.log('xxx', JSON.stringify(this.order))
      })
    },
    goBack () {
      this.$router.push({ name: 'Orders' })
    },
    async cancelOrder () {
      const url = `${apiUrl}/orders/${this.$route.params.orderId}/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        status: 'Anulowane'
      }
      await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      this.goBack()
    },
    async editOrder () {
      console.log(this.order.orderId)
      await this.$router.push({name: 'OrderEdit', params: {orderId: this.order.orderId}})
    }
  },
  mounted () {
    this.getOrder()
  }
}
</script>

<style scoped>

</style>
