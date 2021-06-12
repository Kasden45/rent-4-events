<template>
    <div>
        <div class="row justify-content-end my-3 px-3 mw-100">
            <div class="col-md-7 col-12">
                <new-order-dates v-if="newOrder" :order-source="newOrder" @edit:order="editOrder"/>
            </div>
            <div class="col-md-3 col-11 align-self-end py-2">
                <router-link class="btn btn-4 ml-auto" to="/Zamowienia">Powrót do zamówień</router-link>
            </div>
        </div>
        <div class="row mb-3 px-3 mw-100" v-if="activeSearchWord.length > 0 && activeSearchWord.trim()">
            <div class="col-md-6 offset-md-2 offset-sm-5 search-info">
                <span id="search-results">Wyniki wyszukiwania dla frazy: </span>
                <span class="fst-italic">"{{this.activeSearchWord}}"</span>
                <button class="btn btn-sm btn-outline-4 size" type="button" id="button-cancel" @click="deleteFilters">
                    <font-awesome-icon icon="times-circle"></font-awesome-icon>
                </button>
            </div>
        </div>
        <div class="row justify-content-center mw-100">
            <div class="col-md-2 col-sm-4 col-10">
                <new-order-filters :categories-source="categories" :delete-filters="cancel" ref="child" @filter:product="filterProducts" @search:product="searchProducts"/>
            </div>
            <div class="col-md-7 col-sm-7 col-10">
                <div class="row align-content-center">
                    <div class="col-lg-4 col-md-6 col-12 px-5 py-3 products-gallery" v-for="prod in products" :key="prod.prodId">
                        <product :product-source="prod" :order="true" @add:position="addProduct"/>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-10 ">
                <div class="row">
                    <new-order :order-source="newOrder" @delete:position="deletePosition" @edit:position="editPosition" @set:position="setPosition" @send:order="sendOrder"/>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import NewOrderFilters from '../components/NewOrderFilters'
import NewOrder from '../components/NewOrder'
import Product from '../components/Product'
import NewOrderDates from '../components/NewOrderDates'
import axios from 'axios'
import { api_url } from '../../auth_config.json'

export default {
  name: 'Order',
  components: {
    NewOrderDates,
    NewOrderFilters,
    NewOrder,
    Product
  },
  data () {
    return {
      categories: [],
      newOrder: {},
      products: [],
      activeSearchWord: ''
    }
  },
  methods: {
    async getCategories () {
      const url = `${api_url}/categories/?query={catId, catName}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.categories = response.data['results']
        return resp
      })
    },
    async getProducts () {
      const url = `${api_url}/products/?query={prodId, prodName, price, images}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
        return resp
      })
    },
    async getOrder () {
      const url = `${api_url}/orders/?query={*,positions{*,product{prodId,prodName, quantity, price}}}`
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
      const url = `${api_url}/orders/`
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
      console.log('ORDER', JSON.stringify(order))
      const url = `${api_url}/orders/${this.newOrder.orderId}/`
      const token = await this.$auth.getTokenSilently()
      await axios.put(url, order, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
      console.log('NEW ORDER', this.newOrder)
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
      const url = `${api_url}/order-positions/`
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
      const url = `${api_url}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const currentQuantity = this.getQuantityOfPosition(id)
      const position = {
        quantity: currentQuantity + parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async setPosition (id, quantity) {
      const url = `${api_url}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const position = {
        quantity: parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async deletePosition (id) {
      const url = `${api_url}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrder()
    },
    async filterProducts (sorting, categories, searchWord, searchDescription) {
      var url = `${api_url}/products/?query={prodId, prodName, price, images}`
      if (sorting !== '') {
        url += `&ordering=${sorting}`
      }
      if (categories.length > 0) {
        url += `&categories=[${categories}]`
      }
      searchWord = searchWord.replace('&', '')
      if (searchWord.length > 0 && searchWord.trim() && !searchWord.includes('&')) {
        url += `&search=${searchWord}`
        if (searchDescription === false) {
          url += `&name_only=1`
        }
      }
      this.activeSearchWord = searchWord
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
      })
    },
    async searchProducts (searchWord, searchDescription) {
      searchWord = searchWord.replace('&', '')
      var url = `${api_url}/products/?query={prodId, prodName, price, images}`
      if (searchWord.length > 0 && searchWord.trim()) {
        url += `&search=${searchWord}`
        if (searchDescription === false) {
          url += `&name_only=1`
        }
      }
      this.activeSearchWord = searchWord
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
      })
    },
    deleteFilters () {
      this.$refs.child.clearFilters()
    },
    async sendOrder (done) {
      const url = `${api_url}/orders/${this.newOrder.orderId}/`
      const token = await this.$auth.getTokenSilently()
      const order = {
        status: 'Oczekujące'
      }
      await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      done()
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
#search-results {
    font-weight: 600;
}

#button-cancel {
    border: none;
}

#button-cancel:hover, #button-cancel:focus {
    color: var(--COLOR4);
    border-color: var(--COLOR4);
    background-color: #FFFFFF;
}
</style>
