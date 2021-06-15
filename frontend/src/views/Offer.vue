<template>
    <div>
        <div class="row justify-content-center">
            <div class="col-11">
                <div class="row mb-3 px-3 mt-3 mw-100" v-if="activeSearchWord.length > 0 && activeSearchWord.trim()">
                    <div class="col-md-6 search-info">
                        <span id="search-results">Wyniki wyszukiwania dla frazy: </span>
                        <span class="fst-italic">"{{this.activeSearchWord}}"</span>
                        <button class="btn btn-sm btn-outline-4 size" type="button" id="button-cancel" @click="deleteFilters">
                            <font-awesome-icon icon="times-circle"></font-awesome-icon>
                        </button>
                    </div>
                </div>
                <div class="row justify-content-center mw-100 mt-3">
                    <div class="col-lg-2 col-md-3 col-sm-4 col-10">
                        <new-order-filters :categories-source="categories" ref="child" @filter:product="filterProducts" @search:product="searchProducts"/>
                    </div>
                    <div class="col-lg-10 col-md-9 col-sm-7 col-10">
                        <div class="row align-content-center">
                            <div class="col-xl-3 col-lg-4 col-md-6 col-12 px-5 py-3 products-gallery" v-for="prod in products" :key="prod.prodId">
                                <product :product-source="prod" :order="false" @add:position="addProduct"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import NewOrderFilters from '../components/NewOrderFilters'
import Product from '../components/Product'
import NewOrderDates from '../components/NewOrderDates'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'

export default {
  name: 'offer',
  props: {
    activeUser: String
  },
  components: {
    NewOrderDates,
    NewOrderFilters,
    Product
  },
  data () {
    return {
      categories: [],
      products: [],
      activeSearchWord: ''
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
        return resp
      })
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
      })
    },
    deleteFilters () {
      this.$refs.child.clearFilters()
    }
  },

  mounted () {
    this.getCategories()
    this.getProducts()
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
