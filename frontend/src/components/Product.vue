<template>
    <div class="product" :id="productSource.prodId">
        <div class="row">
            <img :src="productSource.images[0].imageUrl" alt="prodImage" height="150" width="150">
        </div>
        <div class="row">
            <p>{{productSource.prodName}}</p>
        </div>
        <div class="row">
            <div class="col-7">
                <p>{{productSource.price}} zł/dzień</p>
            </div>
            <div class="col-5">
                <input class="form-control" type="number" value="1" min="1" :id="'prod' + productSource.prodId">
            </div>

        </div>
        <div class="row">
            <button class="btn btn-outline-2" @click="handleAddItem(productSource.prodId)"> DODAJ DO ZAMÓWIENIA</button>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'Product',
  props: {
    productSource: Object
  },
  methods: {
    handleAddItem (id) {
      const $quantity = $('#prod' + id).val()
      console.log($quantity)
      this.$emit('add:position', id, $quantity)
    }

  }
}
</script>

<style scoped>

</style>
