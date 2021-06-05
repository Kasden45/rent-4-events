<template>
    <div id="categories" class="px-5">
        <div class="row">
            <label class="form-check-label" for="sorting">Sortowanie:</label>
            <select class="form-control" id="sorting" v-model="sorting" @change="changeSorting($event)">
                <option value="prodName">A-Z</option>
                <option value="-prodName">Z-A</option>
                <option value="price">Cena rosnąco</option>
                <option value="-price">Cena malejąco</option>
            </select>
        </div>
        <div class="row">
            <label class="form-check-label" for="availability">Dostępność:</label>
            <select class="form-control" id="availability" @change="changeAvailability($event)">
                <option>Dostępne</option>
                <option>Niedostępne</option>
                <option>Wszystkie</option>
            </select>
        </div>
        <div class="row">
            <h6>KATEGORIE</h6>
        </div>
        <div class="row" v-for="cat in categoriesSource" :key="cat.catId">
            <div class="form-check">
              <input class="form-check-input" type="checkbox" :value="cat.catId" :id="cat.catId" @change="changeCategories($event)">
              <label class="form-check-label" :for="cat.catId">{{cat.catName}}</label>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'CategoriesCheckbox',
  props: {
    categoriesSource: Array
  },
  data () {
    return {
      sorting: '',
      categories: [],
      availability: ''
    }
  },
  methods: {
    changeSorting (event) {
      this.sorting = event.target.value
      this.applyFilters()
    },
    changeAvailability (event) {
      this.availability = event.target.value
      this.applyFilters()
    },
    changeCategories (event) {
      console.log(event.target.value)
      const list = []
      $('.form-check input:checked').each(function (e) {
        list.push(parseInt($(this).val()))
      })
      this.categories = list
      this.applyFilters()
    },
    applyFilters () {
      this.$emit('filter:product', this.sorting, this.categories)
    }
  }
}
</script>

<style scoped>
#categories {
    color: #000000;
}
.form-check-label {
    margin: 0px;
}

.form-check {
    margin: 10px 0px 10px 0px;
}
</style>
