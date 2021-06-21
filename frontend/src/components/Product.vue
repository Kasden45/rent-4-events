<template>
    <div class="product" :id="productSource.prodId" v-bind:class="[productSource.availableAtDate<=0 ? {'unavailable': true} : {}]">
        <div class="row">
            <img class="mx-auto" :src="productSource.images[0].imageField" alt="prodImage" @click="productPreview(productSource.prodId)">
        </div>
        <div class="row mt-2">
            <p>{{productSource.prodName}}</p>
        </div>
        <div class="row" v-if="order && productSource.availableAtDate !== null">
            <p v-bind:style= "[productSource.availableAtDate<=0 ? {'color':'red'} : {}]" >{{productSource.availableAtDate>0 ? 'Dostępne: ' + Math.max(0,productSource.availableAtDate) : 'Niedostępne'}}</p>
        </div>
        <div class="row">
            <div class="col-7">
                <p>{{productSource.price}} zł/dzień</p>
            </div>
            <div v-if="order" class="col-5">
                <input class="form-control" type="number" value="1" min="1" :id="'prod' + productSource.prodId">
            </div>

        </div>
        <div class="row" v-if="order">
            <button class="btn btn-outline-2" @click="handleAddItem(productSource.prodId)"> DODAJ DO ZAMÓWIENIA</button>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Product',
  props: {
    productSource: Object,
    order: Boolean
  },
  methods: {
    handleAddItem (id) {
      const $quantity = $('#prod' + id).val()
      console.log($quantity)
      this.$emit('add:position', id, $quantity)
    },
    productPreview (id) {
      this.$router.push({ name: 'ProductPreview', params: { prodId: id } })
    }

  }
}
</script>

<style scoped>
img {
    height: 10rem;
    width: auto;
}

input[type=number]::-webkit-inner-spin-button,
input[type=number]::-webkit-outer-spin-button {

   opacity: 1;

}
.unavailable {
    opacity: 0.7;
    outline: 110px solid rgba(76, 75, 75, 0.1) !important;
    outline-offset: -100px;
    overflow: hidden;
    position: relative;
}
</style>
