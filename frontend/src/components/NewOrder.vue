<template>
    <div class="new-order">
        <p>PODSUMOWANIE ZAMÓWIENIA</p>
    </div>
</template>

<script>
export default {
  name: 'NewOrder',
  props: {
    orderSource: Object
  }
}
</script>

<style scoped>
.new-order {
    background-color: bisque;
    height: 70vh;
}
</style>
