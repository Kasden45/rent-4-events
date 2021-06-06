<template>
    <div class="new-order px-3 py-3">
        <h4>PODSUMOWANIE</h4>
        <div class="tab-content">
            <table class="table table-sm table-borderless ">
            <thead>
                <tr>
                    <th>PRODUKT</th>
                    <th>SZT</th>
                    <th></th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="elem in orderSource.positions" :key="elem.product.prodId">
                    <td>{{elem.product.prodName}}</td> <!--DODAĆ WYLICZANIE KOSZTÓW ZAMÓWIENIA-->
                    <td>
                        <div>
                            <button class="btn btn-sm btn-4 d-inline" @click="deleteOne(elem.product.prodId)">-</button>
                            <input class="form-control w-50 d-inline size" :id="'write' + elem.product.prodId" type="number" :value="elem.quantity" @change="readQuantity(elem.product.prodId)">
                            <button class="btn btn-sm btn-4 d-inline" @click="addOne(elem.product.prodId)">+</button>
                        </div>
                    </td>
                    <td>
                        <button class="btn btn-sm btn-3" @click="handleDelete(elem.product.prodId)">
                            <font-awesome-icon icon="trash"></font-awesome-icon>
                        </button>
                    </td>
                </tr>
            </tbody>
        </table>
        </div>

        <div class="mt-3">
            <p>
                <span> Adres eventu:</span>
                <br/>
                <span class="data">{{orderSource.address}}</span>
            </p>
            <p>
                <span> Transport:</span>
                <font-awesome-icon v-if="orderSource.isTransport" icon="check"></font-awesome-icon>
                <font-awesome-icon v-if="!orderSource.isTransport" icon="times"></font-awesome-icon>
            </p>
            <p>
                <span> Termin wypożyczenia:</span>
                <br/>
                <span class="data">{{orderSource.startDate}} - {{orderSource.endDate}}</span>
            </p>
            <p>
                <span>Koszt zamówienia: </span>
                <span class="data">{{orderSource.totalCost}} zł</span>
            </p>
            <button class="btn btn-4 float-end" @click="sendOrder">Złóż zapytanie</button>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
export default {
  name: 'NewOrder',
  props: {
    orderSource: Object
  },
  methods: {
    handleDelete (id) {
      this.$emit('delete:position', id)
    },
    addOne (id) {
      this.$emit('edit:position', id, 1)
    },
    deleteOne (id) {
      const $value = parseInt($('#write' + id).val())
      if ($value > 1) {
        this.$emit('edit:position', id, -1)
      } else if ($value === 1) {
        this.handleDelete(id)
      }
    },
    readQuantity (id) {
      const $input = $('#write' + id)
      const $value = parseInt($input.val())
      if ($value > 0) {
        this.$emit('set:position', id, $value)
      } else {
        const $positionIndex = this.orderSource.positions.map(function (elem) {
          return elem.product.prodId
        }).indexOf(id)
        $input.val(this.orderSource.positions[$positionIndex].quantity)
      }
    },
    sendOrder () {
      this.$emit('send:order')
      this.$router.push({ name: 'Orders' })
    }
  }
}
</script>

<style scoped>
.new-order {
    background-color: var(--COLOR2);
    max-height: 90vh;
    color: #FFFFFF;
    font-weight: 600;
    /*opacity: 90%;*/
}

.new-order h4 {
    color: #FFFFFF;
}

.tab-content {
    height: 50vh;
    overflow: auto;
}

.table {
    color: #E2DEDE;
}

th {
    color: #FFFFFF;
}

span.data {
    color: var(--COLOR5);
    font-weight: 400;
}

::-webkit-scrollbar {
    width: 8px;
    border-radius: 5px;
}

/* Track */
::-webkit-scrollbar-track {
    background: #267478;

}

/* Handle */
::-webkit-scrollbar-thumb {
    background: #FFFFFF;
    border-radius: 10px;
}

/* Handle on hover */
::-webkit-scrollbar-thumb:hover {
    background: #555555;
}

.btn-sm {
    width: 30px;
    height: 30px;
}

.size {
    height: 30px;
    max-width: 70px;
    margin: 0;
    vertical-align: middle;
    text-align: center;
}

td {
    vertical-align: middle;
}

/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type=number] {
  -moz-appearance: textfield;
}
</style>
