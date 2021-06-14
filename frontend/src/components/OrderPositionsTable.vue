<template>
    <div id="order-positions-table">
        <table class="table table-hover table-responsive">
            <thead>
                <tr>
                    <th>Produkt</th>
                    <th class="text-end">Liczba sztuk</th>
                    <th class="text-end" v-if="activeUser === 'Admin'">Dostępne</th>
                    <th class="text-end">Cena za sztukę</th>
                    <th class="text-end">Cena razem</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="elem in orderSource.positions" :key="elem.product.prodId" @click="productPreview(elem.product.prodId)">
                    <td>{{elem.product.prodName}}</td>
                    <td class="text-end">{{elem.quantity}}</td>
                    <td class="text-end" v-if="activeUser === 'Admin'">{{elem.product.available}}</td>
                    <td class="text-end">{{elem.product.price}} zł</td>
                    <td class="text-end">{{(elem.quantity * elem.product.price).toFixed(2)}} zł</td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
export default {
  name: 'OrderPositionsTable',
  props: {
    orderSource: Object,
    activeUser: String
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
