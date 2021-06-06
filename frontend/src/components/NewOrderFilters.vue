<template>
    <div id="categories" class="ps-sm-5">
        <div class="row mb-0">
            <div class="input-group p-0">
                <input type="text" class="form-control m-0" id="input-search" placeholder="Szukaj...">
                <button class="btn btn-4 m-0" type="button" id="button-search" @click="readSearch()">
                    <font-awesome-icon icon="search"></font-awesome-icon>
                </button>
            </div>
        </div>
        <div class="row mb-3">
            <div class="form-check">
                <input class="form-check-input" type="checkbox" id="desc-input" v-model="searchDescription">
                <label class="form-check-label" for="desc-input" id="desc-label">Szukaj także w opisach</label>
            </div>
        </div>
        <div class="row mb-4">
            <label class="form-check-label p-0 mb-2" for="sorting">Sortowanie:</label>
            <select class="form-control" id="sorting" v-model="sorting" @change="changeSorting($event)">
                <option value="prodName">A-Z</option>
                <option value="-prodName">Z-A</option>
                <option value="price">Cena rosnąco</option>
                <option value="-price">Cena malejąco</option>
            </select>
        </div>
        <div class="row mb-4">
            <label class="form-check-label p-0 mb-2" for="availability">Dostępność:</label>
            <select class="form-control" id="availability" v-model="availability" @change="changeAvailability($event)">
                <option>Dostępne</option>
                <option>Niedostępne</option>
                <option>Wszystkie</option>
            </select>
        </div>
        <div class="row">
            <h6 class="p-0">KATEGORIE</h6>
        </div>
        <div class="row" v-for="cat in categoriesSource" :key="cat.catId">
            <div class="form-check" id="cat-check">
              <input class="form-check-input" type="checkbox" :value="cat.catId" :id="cat.catId" @change="changeCategories">
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
      availability: 'Wszystkie',
      searching: false,
      searchWord: '',
      searchDescription: false
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
    changeCategories () {
      const list = []
      $('#cat-check input:checked').each(function () {
        list.push(parseInt($(this).val()))
      })
      this.categories = list
      this.applyFilters()
    },
    readSearch () {
      this.searchWord = $('#input-search').val()
      this.searching = true
      $('#cat-check input:checked').each(function () {
        this.checked = false
      })
      this.availability = 'Wszystkie'
      this.sorting = ''
      this.searching = false

      this.$emit('search:product', this.searchWord, this.searchDescription)
    },
    applyFilters () {
      if (!this.searching) {
        this.$emit('filter:product', this.sorting, this.categories, this.searchWord, this.searchDescription)
      }
    },
    clearFilters () {
      this.searching = true
      $('.form-check input:checked').each(function () {
        this.checked = false
      })
      this.availability = 'Wszystkie'
      this.sorting = ''
      this.searchWord = ''
      $('#input-search').val('')
      this.searching = false
      this.$emit('filter:product', this.sorting, this.categories, this.searchWord, this.searchDescription)
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

#desc-label {
    font-weight: 400;
}
</style>
