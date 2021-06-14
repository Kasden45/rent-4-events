<template>
    <div id="order-preview-details">
        <div class="row">
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Data od:</span>
                <span>{{this.orderSource.startDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Data do:</span>
                <span>{{this.orderSource.endDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Adres:</span>
                <span>{{this.orderSource.address}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Transport:</span>
                <font-awesome-icon v-if="orderSource.isTransport" icon="check"></font-awesome-icon>
                <font-awesome-icon v-if="!orderSource.isTransport" icon="times"></font-awesome-icon>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Status:</span>
                <span>{{this.orderSource.status}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Koszt całkowity:</span>
                <span>{{this.orderSource.totalCost}}</span>
            </div>
            <div class="col-sm-6 col-12" v-if="activeUser === 'Klient' || !statusArray.includes(orderSource.status)">
                <span class="fw-bolder">Komentarz:</span>
                <p>{{this.orderSource.comment}}</p>
            </div>
        </div>
        <div class="row mt-md-4" v-if="activeUser === 'Admin' && statusArray.includes(orderSource.status)">
            <div class="col-md-8 col-sm-12 col-12">
                <div class="form-group">
                    <label  class="fw-bolder" for="comment">Komentarz:</label>
                    <textarea class="form-control" id="comment" :value="this.orderSource.comment" rows="4"></textarea>
                </div>
            </div>
            <div class="col-md-4 col-12">
                <button class="btn btn-2 my-1 mx-auto btn-width d-block" @click="changeStatus('Do realizacji')">Zaakceptuj</button>
                <button class="btn btn-3 my-1 mx-auto btn-width d-block" @click="changeStatus('W trakcie negocjacji')">Zaproponuj zmiany</button>
                <button class="btn btn-4 my-1 mx-auto btn-width d-block" @click="changeStatus('Odrzucone')">Odrzuć</button>
            </div>
        </div>
    </div>
</template>

<script>
import {apiUrl} from '../../auth_config.json'
import axios from 'axios'
import $ from 'jquery'
export default {
  name: 'OrderPreviewDetails',
  props: {
    orderSource: Object,
    activeUser: String
  },
  data () {
    return {
      statusArray: ['W trakcie negocjacji', 'Oczekujące', 'Odrzucone', 'Do realizacji']
    }
  },
  methods: {
    async changeStatus (status) {
      console.log(status)
      const comment = $('#comment').val()
      console.log(comment)
      const url = `${apiUrl}/orders/${this.$route.params.orderId}/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        status: status,
        comment: comment
      }
      await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      await this.$router.push({name: 'Orders'})
    }
  }
}
</script>

<style scoped>
.btn-width {
    width: 160px;
}
</style>
