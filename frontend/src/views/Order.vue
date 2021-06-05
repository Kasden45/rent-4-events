<template>
    <div>
        <div class="row justify-content-end my-3 px-3">
            <div class="col-md-7 col-12">
                <new-order-dates-filter-sort :order-source="newOrder" @edit:order="editOrder"/>
            </div>
            <div class="col-md-3 col-12 align-self-end py-2">
                <router-link class="btn btn-4" to="/Zamowienia">Powrót do zamówień</router-link>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-2 col-4">
                <categories-checkbox :categories-source="categories"/>
            </div>
            <div class="col-md-7 col-7">
                <div class="row align-content-center">
                    <div class="col-lg-4 col-md-6 col-12 px-5 py-3 products-gallery" v-for="prod in products" :key="prod.prodId">
                        <product :product-source="prod" @add:position="addProduct"/>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-10">
                <div class="row">
                    <new-order :order-source="newOrder" @delete:position="deletePosition" @edit:position="editPosition" @set:position="setPosition"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CategoriesCheckbox from '../components/CategoriesCheckbox'
import NewOrder from '../components/NewOrder'
import Product from '../components/Product'
import NewOrderDatesFilterSort from '../components/NewOrderDatesFilterSort'
import axios from 'axios'
const API_URL = 'http://localhost:8000'

export default {
  name: 'Order',
  components: {
    NewOrderDatesFilterSort,
    CategoriesCheckbox,
    NewOrder,
    Product
  },
  data () {
    return {
      categories: [],
      newOrder: {},
      products: []
    }
  },
  methods: {
    async getCategories () {
      const url = `${API_URL}/categories/?query={catId, catName}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.categories = response.data['results']
        return resp
      })
    },
    async getProducts () {
      const url = `${API_URL}/products/?query={prodId, prodName, price, images}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
        return resp
      })
    },
    async getOrder () {
      const url = `${API_URL}/orders/?query={*,positions{*,product{prodId,prodName}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        response.data['results'].forEach(
          (item) => {
            if (item.status === 'Robocze') {
              this.newOrder = item
              console.log(item)
            }
          }
        )
        console.log('newOrder ' + JSON.stringify(this.newOrder))
        if (JSON.stringify(this.newOrder) === '{}') {
          console.log('STWORZ NOWY')
          this.addOrder()
        }
      })
    },
    async addOrder () {
      const url = `${API_URL}/orders/`
      const token = await this.$auth.getTokenSilently()
      var order = {
        clientId: this.$auth.user,
        startDate: new Date().toISOString().slice(0, 10),
        endDate: new Date().toISOString().slice(0, 10),
        address: 'Niezdefiniowany',
        totalCost: 0,
        status: 'Robocze'
      }
      await axios.post(url, order, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.newOrder = response.data
      })
    },
    async editOrder (order) {
      const url = `${API_URL}/orders/${this.newOrder.orderId}/`
      const token = await this.$auth.getTokenSilently()
      await axios.put(url, order, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    getQuantityOfPosition (id) {
      for (let i = 0; i < this.newOrder.positions.length; i++) {
        if (this.newOrder.positions[i].product.prodId === id) {
          return this.newOrder.positions[i].quantity
        }
      }
    },
    addProduct (id, quantity) {
      var found = false
      for (let i = 0; i < this.newOrder.positions.length; i++) {
        if (this.newOrder.positions[i].product.prodId === id) {
          found = true
          break
        }
      }
      found ? this.editPosition(id, quantity) : this.addPosition(id, quantity)
    },
    async addPosition (id, quantity) {
      const url = `${API_URL}/order-positions/`
      const token = await this.$auth.getTokenSilently()

      const position = {
        order: this.newOrder.orderId,
        product: id,
        quantity: quantity
      }
      await axios.post(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async editPosition (id, quantity) {
      const url = `${API_URL}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const currentQuantity = this.getQuantityOfPosition(id)
      const position = {
        quantity: currentQuantity + parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async setPosition (id, quantity) {
      const url = `${API_URL}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const position = {
        quantity: parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async deletePosition (id) {
      console.log(id)
      const url = `${API_URL}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async getProductById (id) {
      const url = `${API_URL}/products/${id}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        return response.data['results']
      })
    }

  },
  mounted () {
    this.getCategories()
    this.getProducts()
    this.getOrder()
    console.log(this.newOrder)
  }
}
</script>

<style scoped>

</style>
