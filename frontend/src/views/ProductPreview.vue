<template>
    <div id="product-preview">
        <div class="row justify-content-center mt-3">
            <div class="col-11">
                <div class="row">
                    <div class="col-md-5 col-10 offset-1">
                        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                            <div class="carousel-indicators">
                                <button v-for="index in product.images.length" :key="index" :id="index-1" type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="index-1" class="btn-swipe active" aria-current="true"></button>
                            </div>
                            <div class="carousel-inner">
                                <div v-for="image in product.images" :key="image.imageId" class="carousel-item active">
                                    <img :src="image.imageField" class="d-block img-fluid img-prod mx-auto" alt="...">
                                </div>
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                <font-awesome-icon class="position-absolute" icon="chevron-left" color="#000000" size="2x"/>
                                <font-awesome-icon class="position-absolute" icon="chevron-left" color="#EEEEEE" size="2x"/>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                <font-awesome-icon class="position-absolute" icon="chevron-right" color="#000000" size="2x"/>
                                <font-awesome-icon class="position-absolute" icon="chevron-right" color="#EEEEEE" size="2x"/>
<!--                                <span class="carousel-control-next-icon" aria-hidden="true"></span>-->
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                    <div class="col-md-4 col-10 offset-1">
                        <div class="row">
                            <p class="prod-title">{{this.product.prodName}}</p>
                        </div>
                        <div class="row">
                            <p class="text-justify">{{this.product.description}}</p>
                        </div>
                        <div class="row text-end">
                            <p class="prod-price">{{this.product.price}}zł/dzień</p>
                        </div>
                    </div>
                </div>
                <div class="row justify-content-center">
                    <p class="similar ms-2">Może Cię zainteresować:</p>
                    <div class="col-md-2 col-10 mx-auto" v-for="prod in similarProducts" :key="prod.prodId">
                        <product :product-source="prod" :order="false" @add:position="() => {}"/>
                    </div>
                </div>

            </div>

        </div>
    </div>
</template>

<script>
import Product from '../components/Product'
import axios from 'axios'
import $ from 'jquery'
import { apiUrl } from '../../auth_config.json'
export default {
  name: 'ProductPreview',
  props: {
    activeUser: String
  },
  components: {
    Product
  },
  data () {
    return {
      product: {},
      similarProducts: []
    }
  },
  methods: {
    async getProduct () {
      const url = `${apiUrl}/products/${this.$route.params.prodId}/`
      let token = null
      if (this.$auth.isAuthenticated) {
        token = await this.$auth.getTokenSilently()
      }
      await axios.get(url, token !== null ? {headers: {Authorization: `Bearer ${token}`}} : {}).then((response) => {
        this.product = response.data
        console.log('images', JSON.stringify(this.product.images))
      })
    },
    async getSimilarProducts () {
      const url = `${apiUrl}/products/${this.$route.params.prodId}/similar/?query={prodId, prodName, price, images}`
      let token = null
      if (this.$auth.isAuthenticated) {
        token = await this.$auth.getTokenSilently()
      }
      await axios.get(url, token !== null ? {headers: {Authorization: `Bearer ${token}`}} : {}).then((response) => {
        this.similarProducts = response.data['results']
      })
    },
    removeClasses () {
      const img0 = this.product.images[0].imageField
      $('.carousel-item').each(function () {
        if ($(this).children().attr('src') !== img0) {
          $(this).prop('classList').remove('active')
        }
      })

      $('.btn-swipe').each(function () {
        if (parseInt($(this).attr('id')) !== 0) {
          $(this).prop('classList').remove('active')
          $(this).data('aria-current', false)
        }
      })
    },
    removePrevNext () {
      if (this.product.images.length === 1) {
        $('.carousel-indicators').remove()
        $('.carousel-control-prev').remove()
        $('.carousel-control-next').remove()
      }
    }
  },
  mounted () {
    const sth = this.getProduct().then(() => {
      this.removeClasses()
      this.removePrevNext()
      return 'wow'
    })
    console.log(sth)
    this.getSimilarProducts()
  }
}
</script>

<style scoped>
.carousel-control-prev:hover,
.carousel-control-prev:focus,
.carousel-control-next:hover,
.carousel-control-next:focus {
    background: none;
    border: none;
}

.img-prod {
    max-height: 20rem;
    width: auto;
}

.prod-title {
    font-weight: bold;
    font-size: 300%;
}

.prod-price {
    font-size: 150%;
    font-weight: 500;
}

 .similar {
     font-size: 125%;
     font-weight: 500;
 }

</style>
