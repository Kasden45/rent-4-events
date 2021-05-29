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
                        <product :product-source="prod"/>
                    </div>
                </div>
            </div>
            <div class="col-md-3 col-10">
                <div class="row">
                    <new-order :order-source="neworder"/>
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
      neworder: {},
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
    }
  },
  mounted () {
    this.getCategories()
    this.getProducts()
  }
}
</script>

<style scoped>

</style>
