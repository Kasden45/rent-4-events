<template>
    <div>
        <div class="row justify-content-end my-3 px-3 mw-100">
            <div class="col-md-7 col-12">
                <new-order-dates :key="newOrder" :availability-source="productsAvailability" :order-source="newOrder" :edit="false"  @edit:order="editOrder"/>
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
                <new-order-filters :categories-source="categories" ref="child" @filter:product="filterProducts" @search:product="searchProducts"/>
            </div>
            <div class="col-md-7 col-sm-7 col-10">
                <div class="row align-content-center">
                    <div class="col-lg-4 col-md-6 col-12 px-5 py-3 products-gallery" v-for="prod in products" :key="prod.prodId">
                        <product :product-source="prod" :order="true" @add:position="addProduct" :key="productsAvailability"/>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-10 ">
                <div class="row">
                    <new-order v-if="this.$route.params.orderId" :key="newOrder" :availability-source="productsAvailability" :order-source="newOrder" :active-user="activeUser" :edit="true" @delete:position="deletePosition" @edit:position="editPosition" @set:position="setPosition" @send:order="sendOrder"/>
                    <new-order v-else :availability-source="productsAvailability" :order-source="newOrder" :key="newOrder" :active-user="activeUser" :edit="false" @delete:position="deletePosition" @edit:position="editPosition" @set:position="setPosition" @send:order="sendOrder"/>
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
import { apiUrl } from '../../auth_config.json'

export default {
  name: 'Order',
  props: {
    activeUser: String
  },
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
      activeSearchWord: '',
      productsAvailability: []
    }
  },
  methods: {
    async getCategories () {
      const url = `${apiUrl}/categories/?query={catId, catName}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.categories = response.data['results']
        return resp
      })
    },
    async getProducts () {
      const url = `${apiUrl}/products/?query={prodId, prodName, price, images}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
        return this.getAvailable()
      })
      console.log(resp)
    },
    async getAvailable (from_ = new Date().toISOString().slice(0, 10), to_ = new Date().toISOString().slice(0, 10)) {
      if (from_ === undefined && to_ === undefined) { from_ = to_ = new Date().toISOString().slice(0, 10) }
      console.log('from', from_, 'to', to_)
      const url = `${apiUrl}/available/?from=${from_}&to=${to_}`
      console.log(this.$auth)
      const token = await this.$auth.getTokenSilently()
      console.log(token)
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.productsAvailability = response.data

        console.log('ava response', JSON.stringify(response.data))
        console.log('availability', this.productsAvailability)
        this.products.forEach(prod => {
          prod.availableAtDate = this.getAvailableForProduct(prod.prodId)
        })
        console.log('products with availability', JSON.stringify(this.products))
        return resp
      })
    },
    getAvailableForProduct (prodId) {
      return this.productsAvailability.find(p => p.prodId === prodId).available
    },
    async getOrderCopied () {
      const url = `${apiUrl}/orders/${this.newOrder.orderId}/?query={*,positions{*,product{prodId,prodName, quantity, price}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.newOrder = response.data

        this.getAvailable(this.newOrder.startDate, this.newOrder.endDate)
      })
    },
    async getOrderCopy () {
      const url = `${apiUrl}/orders/${this.$route.params.orderId}/?query={*,positions{*,product{prodId,prodName, quantity, price}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response1) => {
        this.newOrder.orderId = response1.data.orderId
        this.newOrder.client = response1.data.client
        this.newOrder.startDate = response1.data.startDate
        this.newOrder.endDate = response1.data.endDate
        this.newOrder.address = response1.data.address
        this.newOrder.isTransport = response1.data.isTransport
        this.newOrder.isEdited = response1.data.isEdited
        this.newOrder.totalCost = response1.data.totalCost
        this.newOrder.status = response1.data.status
        this.newOrder.creationDate = response1.data.creationDate
        this.newOrder.comment = response1.data.comment
        this.addOrderCopy().then(() => {
          response1.data.positions.forEach((pos) => {
            const newPos = {
              order: this.newOrder.orderId,
              product: pos.product.prodId,
              quantity: pos.quantity
            }
            this.addPositionCopy(newPos)
          })

          this.getAvailable(this.newOrder.startDate, this.newOrder.endDate)
        })
      })
    },
    async addOrderCopy () {
      const url = `${apiUrl}/orders/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, this.newOrder, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.newOrder = response.data
      })
    },
    async addPositionCopy (position) {
      const url = `${apiUrl}/order-positions/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, position, {headers: {Authorization: `Bearer ${token}`}})
      await this.getOrderCopied()
    },
    async getOrder () {
      const url = `${apiUrl}/orders/?query={*,positions{*,product{prodId,prodName, quantity, price}}}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        response.data['results'].forEach(
          (item) => {
            if (item.status === 'Robocze') {
              this.newOrder = item
              console.log('Znalazłem robocze' + JSON.stringify(item))
            }
          }
        )
        console.log('newOrder ' + JSON.stringify(this.newOrder))
        if (JSON.stringify(this.newOrder) === '{}') {
          console.log('STWORZ NOWY')
          this.addOrder()
        }
        this.getAvailable(this.newOrder.startDate, this.newOrder.endDate)
      })
    },
    async addOrder () {
      const url = `${apiUrl}/orders/`
      const token = await this.$auth.getTokenSilently()
      var order = {
        startDate: new Date().toISOString().slice(0, 10),
        endDate: new Date().toISOString().slice(0, 10),
        address: 'Niezdefiniowany',
        isTransport: false,
        isEdited: false,
        totalCost: 0,
        status: 'Robocze',
        creationDate: new Date().toISOString().slice(0, 10),
        comment: ''
      }
      await axios.post(url, order, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.newOrder = response.data
      }).then(() => { this.getOrder() })
    },
    async editOrder (order) {
      console.log('ORDER', JSON.stringify(order))
      const url = `${apiUrl}/orders/${this.newOrder.orderId}/`
      const token = await this.$auth.getTokenSilently()
      await axios.put(url, order, {headers: {Authorization: `Bearer ${token}`}})
      if (this.$route.params.orderId) {
        await this.getOrderCopied()
      } else {
        await this.getOrder()
      }
      await this.getAvailable(order.startDate, order.endDate)
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
      const url = `${apiUrl}/order-positions/`
      const token = await this.$auth.getTokenSilently()

      const position = {
        order: this.newOrder.orderId,
        product: id,
        quantity: quantity
      }
      await axios.post(url, position, {headers: {Authorization: `Bearer ${token}`}})
      if (this.$route.params.orderId) {
        await this.getOrderCopied()
      } else {
        await this.getOrder()
      }
    },
    async editPosition (id, quantity) {
      const url = `${apiUrl}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const currentQuantity = this.getQuantityOfPosition(id)
      const position = {
        quantity: currentQuantity + parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      if (this.$route.params.orderId) {
        await this.getOrderCopied()
      } else {
        await this.getOrder()
      }
    },
    async setPosition (id, quantity) {
      const url = `${apiUrl}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      const position = {
        quantity: parseInt(quantity)
      }
      await axios.patch(url, position, {headers: {Authorization: `Bearer ${token}`}})
      if (this.$route.params.orderId) {
        await this.getOrderCopied()
      } else {
        await this.getOrder()
      }
    },
    async deletePosition (id) {
      const url = `${apiUrl}/order-positions/${this.newOrder.orderId}/${id}`
      const token = await this.$auth.getTokenSilently()
      await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
      if (this.$route.params.orderId) {
        await this.getOrderCopied()
      } else {
        await this.getOrder()
      }
    },
    async filterProducts (sorting, categories, searchWord, searchDescription) {
      var url = `${apiUrl}/products/?query={prodId, prodName, price, images}`
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

        this.getAvailable(this.newOrder.startDate, this.newOrder.endDate)
      })
    },
    async searchProducts (searchWord, searchDescription) {
      searchWord = searchWord.replace('&', '')
      var url = `${apiUrl}/products/?query={prodId, prodName, price, images}`
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

        this.getAvailable(this.newOrder.startDate, this.newOrder.endDate)
      })
    },
    deleteFilters () {
      this.$refs.child.clearFilters()
    },
    async sendOrder (done) {
      const token = await this.$auth.getTokenSilently()
      var order = {}
      if (this.$route.params.orderId) {
        const url = `${apiUrl}/orders/${this.$route.params.orderId}/`
        order = {
          client: this.newOrder.client.userId,
          startDate: this.newOrder.startDate,
          endDate: this.newOrder.endDate,
          address: this.newOrder.address,
          isTransport: this.newOrder.isTransport,
          isEdited: true,
          totalCost: this.newOrder.totalCost,
          status: this.newOrder.status,
          creationDate: this.newOrder.creationDate,
          comment: this.newOrder.comment,
          positions: []
        }
        this.newOrder.positions.forEach((pos) => {
          const posToChange = {
            product: pos.product.prodId,
            quantity: pos.quantity
          }
          order.positions.push(posToChange)
        })
        await axios.put(url, order, {headers: {Authorization: `Bearer ${token}`}}).then(() => {
          this.deleteOrder()
        })
      } else {
        const url = `${apiUrl}/orders/${this.newOrder.orderId}/`
        order = {
          status: 'Oczekujące'
        }
        await axios.patch(url, order, {headers: {Authorization: `Bearer ${token}`}})
      }
      done()
    },
    async deleteOrder () {
      const url = `${apiUrl}/orders/${this.newOrder.orderId}/`
      const token = await this.$auth.getTokenSilently()
      await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
    }
  },
  beforeDestroy () {
    if (this.newOrder.status !== 'Robocze') {
      this.deleteOrder()
    }
  },
  mounted () {
    this.getCategories()
    this.getProducts()
    this.getAvailable()
    if (this.$route.params.orderId) {
      this.getOrderCopy()
    } else {
      this.getOrder()
    }
    console.log('New order: ' + this.newOrder)
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
