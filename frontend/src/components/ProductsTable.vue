<template>
    <div id="products-table">
        <table class="table table-hover">
            <thead>
                <tr>
                    <th>Nazwa</th>
                    <th>Kategoria</th>
                    <th>Razem</th>
                    <th>Dostępne</th>
                    <th>Cena</th>
                    <th>Opis</th>
                    <th>Zdjęcie</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="product in productsSource" :key="product.prodId" @click="openPreview(product.prodId)">
                    <td>{{product.prodName}}</td>
                    <td>{{product.catName}}</td>
                    <td>{{product.quantity}}</td>
                    <td>{{product.available}}</td>
                    <td>{{product.price}} zł</td>
                    <td>{{product.description}}</td>
                    <td v-if="product.images[0]">
                        <img :src="product.images[0].imageField" class="d-block img-fluid img-prod mx-auto" alt="..." width="45" >
                    </td>
                    <td v-else>
                        <img :src="'https://autoborawski.pl/photo/nophoto.jpg'" class="d-block img-fluid img-prod mx-auto" alt="...2" width="45" >
                    </td>
                    <td>
                        <button type="button" class="btn btn-sm btn-info" :id="product.prodId" @click="handleEdit">Edytuj</button>
                        <button type="button" class="btn btn-sm btn-danger" @click="handleDelete(product.prodId)">Usuń</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'ProductsTable',
  props: {
    productsSource: Array,
    categoriesSource: Array
  },
  data () {
    return {
      submitting: false,
      error: false,
      success: false,
      isEdit: false,
      editedProduct: {
        prodName: '',
        category: '',
        quantity: '',
        available: '',
        price: '',
        description: '',
        images: ''
      }
    }
  },
  methods: {
    openPreview (id) {
      if (!this.isEdit) { this.$router.push({ name: 'ProductPreview', params: { prodId: id } }) }
    },
    catNameFromId (catId) {
      alert('here')
      return this.categoriesSource.find(c => c.catId === catId).catName
    },
    changeButtons (row) {
      var $btn1 = row.children().eq(7).children().eq(0)
      var $btn2 = row.children().eq(7).children().eq(1)

      if (this.isEdit) {
        $btn1.html('Zapisz')
        $btn1.attr('class', 'btn btn-success btn-sm')
        $btn2.html('Anuluj')
      } else {
        $btn1.html('Edytuj')
        $btn1.attr('class', 'btn btn-info btn-sm')
        $btn2.html('Usuń')
      }
    },
    clearStatus () {
      this.success = false
      this.error = false
    },

    handleDelete (id) {
      event.stopPropagation()
      if (!this.isEdit) {
        if (confirm('Czy na pewno chcesz usunąć ten produkt?')) {
          this.$emit('delete:product', id)
        }
      } else {
        console.log('Anuluj')
        this.$emit('get:products')
      }
    },
    handleEdit: function (event) {
      event.stopPropagation()
      this.isEdit = !this.isEdit

      var $prodId = parseInt(event.target.id)
      var $productIndex = this.productsSource.map(function (product) {
        return product.prodId
      }).indexOf($prodId)
      var $product = this.productsSource[$productIndex]

      var $grandParent = $('#' + $prodId).parent().parent() // row

      var $prodName = $grandParent.children().eq(0)
      var $category = $grandParent.children().eq(1)
      var $quantity = $grandParent.children().eq(2)
      var $available = $grandParent.children().eq(3)
      var $price = $grandParent.children().eq(4)
      var $description = $grandParent.children().eq(5)
      var $images = $grandParent.children().eq(6)

      if (this.isEdit) {
        // disable buttons
        $('.btn-danger').not($grandParent.children().eq(7).children().eq(1)).prop('disabled', true)
        $('.btn-info').not($grandParent.children().eq(7).children().eq(0)).prop('disabled', true)

        // change controls -> form
        $prodName.html(function () {
          return '<input class="form-control"/>'
        })
        let newHtml = '<select  class="form-select">'
        this.categoriesSource.forEach(cat => { newHtml += `  <option value=${cat.catId}>${cat.catName}</option>` })
        newHtml += '</select>'
        console.log('new', newHtml)
        $category.html(function () {
          return newHtml
        })
        $quantity.html(function () {
          return '<input class="form-control" type="number" min="0"/>'
        })
        $available.html(function () {
          return '<input class="form-control" type="number" min="0"/>'
        })
        $price.html(function () {
          return '<input class="form-control"/>'
        })
        $description.html(function () {
          return '<input class="form-control"/>'
        })
        // select values that book has
        $prodName.children().val($product.prodName)
        $category.children().val($product.category)
        $quantity.children().val($product.quantity)
        $available.children().val($product.available)
        $price.children().val($product.price)
        $description.children().val($product.description)
        // $images.children().val($product.images)
      } else {
        this.submitting = true
        this.clearStatus()

        // take values
        this.editedProduct = {
          prodId: $product.prodId,
          prodName: $prodName.children().val(),
          category: $category.children().val(),
          quantity: $quantity.children().val(),
          available: $available.children().val(),
          price: $price.children().val(),
          description: $description.children().val(),
          status: $images.children().val()
        }

        // if (this.invalidBrand || this.invalidModel || this.invalidYear || this.invalidLicensePlate || this.invalidCarServiceTo || this.invalidType || this.invalidStatus) {
        //   this.error = true
        //   this.isEdit = !this.isEdit
        //
        //   return
        // }
        if (this.invalidName || this.invalidCategory || this.invalidQuantity || this.invalidAvailable || this.invalidPrice || this.invalidDescription || this.invalidImages) {
          this.error = true
          return
        }

        // enable buttons
        $('.btn-danger').prop('disabled', false)
        $('.btn-info').prop('disabled', false)
        const productData = [this.editedProduct, $productIndex]

        this.$emit('edit:product', {data: productData,
          done: () => {
            this.error = false
            this.success = true
            this.submitting = false

            $product = this.productsSource[$productIndex]

            $prodName.html(function () {
              return $product.prodName
            })
            $category.html(function () {
              return $product.category
            })
            $quantity.html(function () {
              return $product.quantity
            })
            $available.html(function () {
              return $product.available
            })
            $price.html(function () {
              return $product.price
            })
            $description.html(function () {
              return $product.description
            })
            // $images.html(function () {
            //   return `<img :src="$product.images[0].imageField" class="d-block img-fluid img-prod mx-auto" alt="..." width="45" >`
            // })
          }})
      }

      this.changeButtons($grandParent)
    }
  },
  computed: {
    invalidName () {
      return this.editedProduct.prodName === '' || this.editedProduct.prodName.length > 50
    },
    invalidCategory () {
      console.log(this.editedProduct.category)
      return false
    },
    invalidQuantity () {
      return this.editedProduct.quantity < 1
    },
    invalidAvailable () {
      return this.editedProduct.available < 0
    },
    invalidPrice () {
      return parseFloat(this.editedProduct.price) < 0
    },
    invalidDescription () {
      return this.editedProduct.description.length > 500
    }
  }
}
</script>

<style scoped>
img {
    height: 3rem;
    width: auto;
}
</style>
