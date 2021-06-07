<template>
    <div id="order-preview-details">
        <div class="row">
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Data od:</span>
                <span>{{this.orderSource.startDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Data do:</span>
                <span>{{this.orderSource.endDate}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Adres:</span>
                <span>{{this.orderSource.address}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Transport:</span>
                <font-awesome-icon v-if="orderSource.isTransport" icon="check"></font-awesome-icon>
                <font-awesome-icon v-if="!orderSource.isTransport" icon="times"></font-awesome-icon>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Status:</span>
                <span>{{this.orderSource.status}}</span>
            </div>
            <div class="col-md-4 col-sm-6 col-12">
                <span class="fw-bolder">Koszt całkowity:</span>
                <span>{{this.orderSource.totalCost}}</span>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'OrderPreviewDetails',
  props: {
    orderSource: Object
  }
}
</script>

<style scoped>

</style>
