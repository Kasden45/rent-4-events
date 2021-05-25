<template>
    <div>
        <div class="row justify-content-end my-3">
            <div class="col-3">
                <router-link class="btn btn-primary btn-primary" to="/Zamowienia">Powrót do zamówień</router-link>
            </div>
        </div>
        <div class="row">
            <div class="col-3">
                <categories-checkbox :categories-source="categories"/>
            </div>
            <div class="col-6 align-content-center">

            </div>
            <div class="col-3">
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
import axios from 'axios'
const API_URL = 'http://localhost:8000'

export default {
  name: 'Order',
  components: {
    CategoriesCheckbox,
    NewOrder
  },
  data () {
    return {
      categories: [],
      neworder: {}
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
    }
  },
  mounted () {
    this.getCategories()
  }
}
</script>

<style scoped>
.order {
    background-color: #000000;
}

</style>
