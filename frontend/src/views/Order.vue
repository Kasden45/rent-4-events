<template>
    <div>
        <div class="row justify-content-end my-3 px-3">
            <div class="col-md-3 col-4">
                <router-link class="btn btn-3" to="/Zamowienia">Powrót do zamówień</router-link>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-md-2 col-4">
                <categories-checkbox :categories-source="categories"/>
            </div>
            <div class="col-md-7 col-7">
                <div class="row align-content-center">
                    <div class="col-lg-4 col-md-6 col-12 px-5 py-3 products-gallery" v-for="prod in products" :key="prod.prodId">
                        <product :product-source="prod" @add:product="addProduct"/>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-10">
                <div class="row">
                    <new-order :order-source="newOrder" @delete:product="deleteProduct"/>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import CategoriesCheckbox from '../components/CategoriesCheckbox'
import NewOrder from '../components/NewOrder'
import Product from '../components/Product'
import axios from 'axios'
const API_URL = 'http://localhost:8000'

export default {
  name: 'Order',
  components: {
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
      // const token = this.$auth.getIdTokenClaims()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        // console.log(JSON.stringify(response.data['results']))
        this.categories = response.data['results']
        // console.log(this.categories)
        return resp
      })
    },
    async getProducts () {
      const url = `${API_URL}/products/?query={prodId, prodName, price, images}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      // const token = this.$auth.getIdTokenClaims()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        // console.log(JSON.stringify(response.data['results']))
        this.products = response.data['results']
        // console.log(this.categories)
        return resp
      })
    },
    async getOrder () {
      const url = `${API_URL}/orders/`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        const orders = response.data['results']
        orders.forEach(
          (item) => {
            if (item.status === 'Robocze') {
              this.newOrder = item
            }
          }
        )
        if (this.newOrder === {}) {
          this.addOrder()
        }
      })
      console.log(this.newOrder)
    },
    async addOrder () {
      const url = `${API_URL}/orders/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        clientId: this.$auth.user, // ZMIENIC NA ID KLIENTA!!!!ONEONE11!!!
        startDate: new Date().toISOString().slice(0, 10),
        endDate: new Date().toISOString().slice(0, 10),
        address: '',
        totalCost: 0,
        status: 'Robocze',
        positions: []
      }
      await axios.post(url, order, {headers: {Authorization: `Bearer ${token}`}})
      this.newOrder = order
    },
    getQuantityOfProduct (id) {
      for (let i = 0; i < this.newOrder.positions.length; i++) {
        if (this.newOrder.positions[i].product === id) {
          return this.newOrder.positions[i].quantity
        }
      }
    },
    getIndexOfProduct (id) {
      for (let i = 0; i < this.newOrder.positions.length; i++) {
        if (this.newOrder.positions[i].product === id) {
          return i
        }
      }
    },
    addProduct (id, quantity) {
      var found = false
      for (let i = 0; i < this.newOrder.positions.length; i++) {
        if (this.newOrder.positions[i].product === id) {
          found = true
          break
        }
      }
      found ? this.editPosition(id, quantity) : this.addPosition(id, quantity)
    },
    async addPosition (id, quantity) {
      const url = `${API_URL}/order-positions/`
      const token = await this.$auth.getTokenSilently()

      const product = {
        order: this.newOrder.orderId,
        product: id,
        quantity: quantity
      }
      await axios.post(url, product, {headers: {Authorization: `Bearer ${token}`}})
      this.newOrder.positions = [...this.newOrder.positions, product]
    },
    async editPosition (id, quantity) {
      const url = `${API_URL}/order-positions/${id}/`
      const token = await this.$auth.getTokenSilently()
      const currentQuantity = this.getQuantityOfProduct(id)
      const prodIndex = this.getIndexOfProduct(id)
      const product = {
        order: this.newOrder.orderId,
        product: id,
        quantity: currentQuantity + quantity
      }
      await axios.put(url, product, {headers: {Authorization: `Bearer ${token}`}})
      this.newOrder.positions[prodIndex] = currentQuantity + quantity
    },
    async deleteProduct (id) {
      const url = `${API_URL}/order-positions/`
      const token = await this.$auth.getTokenSilently()
      await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
      // this.newOrder.positions = [...this.newOrder.positions, product] tu cos
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
  }
}
</script>

<style scoped>

</style>
