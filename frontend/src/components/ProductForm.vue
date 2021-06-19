<template>
    <div id="product-form">
        <form @submit.prevent="handleSubmit">
            <div class="row py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="name-form">Nazwa:</label>
                        <input
                            v-model="product.prodName"
                            type="text"
                            class="form-control"
                            id="name-form"
                            :class="{ 'has-error': submitting && invalidName}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="category-form">Kategoria:</label>
                        <select
                            v-model="product.category"
                            class="form-select"
                            id="category-form"
                            :class="{ 'has-error': submitting & invalidCategory}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        >
                            <option
                                v-for="category in categoriesSource" :key="category.catId"
                                :value="category.catId"
                            >{{category.catName}}</option>
                        </select>
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="quantity-form">Razem:</label>
                        <input
                            v-model="product.quantity"
                            type="number"
                            min="1"
                            class="form-control"
                            id="quantity-form"
                            :class="{ 'has-error': submitting && invalidQuantity}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>

            </div>
            <div class="row justify-content-between py-2">

                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="available-form">Dostępne:</label>
                        <input
                            v-model="product.available"
                            type="number"
                            min="0"
                            class="form-control"
                            id="available-form"
                            :class="{ 'has-error': submitting && invalidAvailable}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="price-form">Cena:</label>
                        <input
                            v-model="product.price"
                            type="text"
                            class="form-control"
                            id="price-form"
                            :class="{ 'has-error': submitting && invalidPrice}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label for="description-form">Opis:</label>
                        <input
                            v-model="product.description"
                            type="text"
                            class="form-control"
                            id="description-form"
                            :class="{ 'has-error': submitting && invalidDescription}"
                            @focus="clearStatus"
                            @keypress="clearStatus"
                        />
                    </div>
                </div>
            </div>
            <div class="row justify-content-between py-2">
                <div class="col-md-4 col-12">
                    <div class="form-group">
                        <label >Zdjecie:</label>
                        <input type="file" v-on:change="changeImage" name="image" id="image_file" ref="myFile" multiple>
                        <input v-if="selectedImage" v-model="selectedImage.name" type="hidden" name="photo" />
                        <img v-if="image" v-for="image_file in selectedImages" :key="image_file.name" :src="image_file" class="img-fluid img-prod mt-3" alt="..." width="200" >
                    </div>
                </div>

                <div class="col-md-2 col-12 text-end align-self-end pb-2">
                    <button class="btn btn-success" id="confirm">DODAJ</button>
                </div>
            </div>

            <p v-if="error && submitting" class="error-message">
                Proszę wypełnić wskazane pola formularza
            </p>
            <p v-if="success" class="success-message">
                Dane poprawnie zapisano
            </p>
        </form>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'ProductForm',
  props: {
    usersSource: Array,
    categoriesSource: Array
  },
  data () {
    return {
        file: '',
    allowableTypes: ['jpg', 'jpeg', 'png', 'gif'],
    maximumSize: 5000000,
    selectedImage: null,
    image: null,
      submitting: false,
      error: false,
      success: false,
      product: {
        prodId: '',
        prodName: '',
        category: '',
        quantity: '',
        available: '',
        price: '',
        description: '',
        images: ''
      },
        selectedImages: [],
        options:{
      url: 'https://httpbin.org/post',
      type: "POST",
      processData: false,
      contentType: false
    },
      statuses: ['Sprawny', 'W warsztacie', 'Niesprawny']
    }
  },
  methods: {
    handleSubmit () {
        console.log('idk')
      // console.log('pre emit', JSON.stringify($('#image_file').files[0]))
      this.submitting = true
      this.clearStatus()
        // return;
      if (this.invalidName || this.invalidCategory || this.invalidQuantity || this.invalidAvailable || this.invalidPrice || this.invalidDescription || this.invalidImages) {
        console.log('shit')
          this.error = true
        return
      }

        const formData = new FormData()
        const formData2 = new FormData()
        formData.append('prodName', this.product.prodName )
        formData.append('category', this.product.category)
        formData.append('quantity', this.product.quantity)
        formData.append('available', this.product.available)
        formData.append('price', this.product.price)
        formData.append('description', this.product.description)
        formData2.append('imageName', this.selectedImage.name)
        formData2.append('imageUrl', 'irrelevant')
        // formData2.append('product', 4)
        formData2.append('imageField', this.$refs.myFile.files[0])
      this.$emit('add:product', formData, formData2)

      this.product = {
        prodId: '',
        prodName: '',
        category: '',
        quantity: '',
        available: '',
        price: '',
        description: '',
        images: ''
      }

      this.error = false
      this.success = true
      this.submitting = false
    },
    clearStatus () {
      this.success = false
      this.error = false
    },
     validate(image) {
      if (!this.allowableTypes.includes(image.name.split(".").pop().toLowerCase())) {
        alert(`Sorry you can only upload ${this.allowableTypes.join("|").toUpperCase()} files.`)
        return false
      }

      if (image.size > this.maximumSize){
        alert("Sorry File size exceeding from 5 Mb")
        return false
      }

      return true
    },
    onImageError(err){
      console.log(err, 'do something with error')
    },
    changeImage($event) {
        // console.log('Imageaaaa')
      this.selectedImage = $event.target.files[0]
        // console.log('Imagessssss', $event.target.files)
        Array.from($event.target.files).forEach(f => {this.selectedImages.push(URL.createObjectURL(f))})

      //validate the image
      if (!this.validate(this.selectedImage))
        return
      // create a form
      const form = new FormData();
      form.append('file', this.selectedImage);
      // submit the image
      $.ajax(Object.assign({}, this.options, {data: form}))
        .then(this.createImage)
        .catch(this.onImageError);
    },
    createImage() {
      const image = new Image()
      const reader = new FileReader()
      reader.onload = (e) => {
        this.image = e.target.result
          console.log('xd',e.target.result)
      };
      reader.readAsDataURL(this.selectedImage)
    }
  },
  computed: {
    invalidName () {
      return this.product.prodName === ''
    },
    invalidCategory () {
        console.log(this.product.category)
      return false
    },
    invalidQuantity () {
      return this.product.quantity < 1
    },
    invalidAvailable () {
      return this.product.available < 0
    },
    invalidPrice () {
      return parseFloat(this.product.price) < 0
    },
    invalidDescription () {
      return this.product.description === ''
    },
    invalidImages () {
      return false
    }
  }
}
</script>

<style scoped>
option {
    overflow: auto;
}

[class*='-message'] {
    font-weight: 500;
}

.error-message {
    color: #D33C40;
}

.success-message {
    color: #32A95D;
}

</style>

