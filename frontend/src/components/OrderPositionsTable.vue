<template>
    <div id="order-positions-table">
        <table class="table table-hover table-responsive">
            <thead>
                <tr>
                    <th>Produkt</th>
                    <th>Liczba sztuk</th>
                    <th>Cena za sztukę</th>
                    <th>Cena razem</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="elem in orderSource.positions" :key="elem.product.prodId" @click="productPreview(elem.product.prodId)">
                    <td>{{elem.product.prodName}}</td>
                    <td>{{elem.quantity}}</td>
                    <td>{{elem.product.price}} zł</td>
                    <td>{{(elem.quantity * elem.product.price).toFixed(2)}} zł</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
  name: 'OrderPositionsTable',
  props: {
    orderSource: Object
  },
  methods: {
    productPreview (id) {
      this.$router.push({ name: 'ProductPreview', params: { prodId: id } })
    }
  }
}
</script>

<style scoped>

</style>
