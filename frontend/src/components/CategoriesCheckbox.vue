<template>
    <div id="categories" class="px-5">
        <div class="row">
            <h6>KATEGORIE</h6>
        </div>
        <div class="row" v-for="cat in categoriesSource" :key="cat.catId">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" :value="cat.catId" :id="cat.catId">
              <label class="form-check-label" :for="cat.catId">
                {{cat.catName}}
              </label>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'CategoriesCheckbox',
  props: {
    categoriesSource: Array
  }
}
</script>

<style scoped>
#categories {
    color: #000000;
}
</style>
