<template>
    <div id="products" class="container-fluid">
        <div class="row justify-content-center mt-5">
            <div class="col-11 px-5">
                <h3>ASORTYMENT</h3>
                <product-form :categories-source="categories"  @add:product="addProduct"/>
            </div>
        </div>
        <div class="row justify-content-center">
            <div class="col-11 px-5">
                <products-table :products-source="products" :categories-source="categories" :key="products" @edit:product="editProduct" @get:products="getProducts" @delete:product="deleteProduct"/>
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
    async addProduct (product, images) {
      const url = `${apiUrl}/products/`
      const url2 = `${apiUrl}/images/`
      const token = await this.$auth.getTokenSilently()
      await axios.post(url, product, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        images.forEach(im => {
          const formData = new FormData()
          formData.append('imageName', im.imageName)
          formData.append('imageUrl', im.imageUrl)
          formData.append('product', response['data'].prodId)
          formData.append('imageField', im.imageField)
          axios.post(url2, formData, {headers: {Authorization: `Bearer ${token}`, 'Content-Type': 'multipart/form-data'}})
        })
      }).then(() => {
        this.getProducts()
      })
    },
    async getCategories (products) {
      const url = `${apiUrl}/categories/?query={catId, catName}`
      const token = await this.$auth.getTokenSilently()
      await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        this.categories = response.data['results']
        products.forEach(prod => {
          prod.catName = this.categories.find(cat => cat.catId === prod.category).catName
        })
        console.log('productssss after', JSON.stringify(products))
        this.products = products
      })
    },
    async getProducts () {
      const url = `${apiUrl}/products/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        const products = response.data['results']
        this.getCategories(products)
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
      await this.getProducts()
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
  }
}
</script>

<style scoped>

</style>
