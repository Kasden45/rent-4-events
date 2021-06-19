<template>
    <div id="products" class="container">
        <div class="row justify-content-center">
            <div class="col-11">
                <product-form :categories-source="categories"  @add:product="addProduct"/>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-11">
                <products-table :products-source="products" :key="products" @edit:product="editProduct" @get:products="getProducts" @delete:product="deleteProduct"/>
            </div>
        </div>
    </div>
</template>

<script>
import ProductsTable from '../components/ProductsTable'
import ProductForm from '../components/ProductForm'
import axios from 'axios'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'Products',
  props: {
    activeUser: String
  },
  components: {
    ProductsTable,
    ProductForm
  },
  data () {
    return {
      products: [],
      categories: []
    }
  },
  methods: {
    async addProduct (product, image) {
      const url = `${apiUrl}/products/`
      const url2 = `${apiUrl}/images/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, product, {headers: {Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data'}}).then((response) => {
          image.append('product', response['data'].prodId)
          axios.post(url2, image, {headers: {Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data'}})})

        this.getProducts()
    },
    async getCategories () {
      const url = `${apiUrl}/categories/?query={catId, catName}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.categories = response.data['results']
        console.log(this.$auth.getIdTokenClaims())
      })
    },
    async getProducts () {
      const url = `${apiUrl}/products/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.products = response.data['results']
        return resp
      })
    },
    async editProduct (productData) {
      try {
        console.log(productData)
        const product = productData.data[0]
        const index = productData.data[1]
        console.log(productData.data[1])
        const url = `${apiUrl}/products/${product.prodId}/`
        const token = await this.$auth.getTokenSilently()
        await axios.put(url, product, {headers: {Authorization: `Bearer ${token}`}})
        await this.getProductById(product.prodId, index, productData)
      } catch (error) {
        console.log(error)
      }
    },
    async getProductById (id, index, productData) {
      try {
        const url = `${apiUrl}/products/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
          this.products[index] = response.data
          productData.done()
        })
      } catch (error) {
        console.log(error)
      }
    },
    async deleteProduct (id) {
      try {
        const url = `${apiUrl}/products/${id}/`
        const token = await this.$auth.getTokenSilently()
        await axios.delete(url, {headers: {Authorization: `Bearer ${token}`}})
        await this.getProducts()
      } catch (error) {
        console.log(error)
      }
    }
  },
  mounted () {
    this.getProducts()
    this.getCategories()
  }
}
</script>

<style scoped>

</style>
