<template>
    <div id="product-preview">
        <p>Produkt: {{$route.params.prodId}}</p>
        <div class="row justify-content-center">
            <div class="col-11">
                <div class="row">
                    <div class="col-3">
                        <button class="btn btn-4" @click="goBack">POWRÓT</button>
                    </div>
                </div>
                <div class="row">
                    <div class="col-5 offset-md-1">
                        <div id="carouselExampleIndicators" class="carousel slide" data-bs-ride="carousel">
                            <div class="carousel-indicators">
                                <button v-for="index in this.product.images.length" :key="index" :id="index-1" type="button" data-bs-target="#carouselExampleIndicators" :data-bs-slide-to="index-1" class="btn-swipe active" aria-current="true"></button>
                            </div>
                            <div class="carousel-inner">
                                <div v-for="image in this.product.images" :key="image.imageId" class="carousel-item active">
                                    <img :src="image.imageUrl" class="d-block img-prod mx-auto" alt="...">
                                </div>
                            </div>
                            <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="prev">
                                <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Previous</span>
                            </button>
                            <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleIndicators" data-bs-slide="next">
                                <span class="carousel-control-next-icon" aria-hidden="true"></span>
                                <span class="visually-hidden">Next</span>
                            </button>
                        </div>
                    </div>
                    <div class="col-4">
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

            </div>

        </div>
    </div>
</template>

<script>
import axios from 'axios'
import $ from 'jquery'
const API_URL = 'http://localhost:8000'
export default {
  name: 'ProductPreview',
  data () {
    return {
      product: {}
    }
  },
  methods: {
    async getProduct () {
      const url = `${API_URL}/products/${this.$route.params.prodId}/`
      const token = await this.$auth.getTokenSilently()
      const resp = await axios.get(url, {headers: {Authorization: `Bearer ${token}`}}).then((response) => {
        console.log(response.data)
        this.product = response.data
        // console.log('000', this.product.images[0].imageUrl)
      })
      return resp
    },
    removeClasses () {
      const img0 = this.product.images[0].imageUrl
      $('.carousel-item').each(function () {
        // console.log('src', $(this).children().attr('src'))
        // console.log('0', img0)
        if ($(this).children().attr('src') !== img0) {
          // console.log($(this).prop('classList').value)
          $(this).prop('classList').remove('active')
          // console.log($(this).prop('classList').value)
        }
      })

      $('.btn-swipe').each(function () {
        // console.log('src', $(this).children().attr('src'))
        // console.log('id', $(this).attr('id'))
        if (parseInt($(this).attr('id')) !== 0) {
          // console.log('jestwem tu')
          $(this).prop('classList').remove('active')
          $(this).data('aria-current', false)
        }
      })
      // this.removePrevNext()
    },
    removePrevNext () {
      if (this.product.images.length === 1) {
        $('.carousel-indicators').remove()
        $('.carousel-control-prev').remove()
        $('.carousel-control-next').remove()
      }
    },
    goBack () {
      this.$router.push({ name: 'Order' })
    }
  },
  mounted () {
    this.getProduct().then(() => {
      this.removeClasses()
      this.removePrevNext()
    })
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
  height: 25rem;
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

</style>
