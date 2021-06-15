<template>
    <div class="new-order px-3 py-3">
        <div class="col h-100">
            <div class="row">
                <h4>PODSUMOWANIE</h4>
            </div>

            <div class="row margin-bottom">
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
                        <tr v-for="elem in this.orderSource.positions" :key="elem.product.prodId">
                            <td>{{elem.product.prodName}}</td>
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
            </div>
            <div class="row">
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
                    <button class="btn btn-4 float-end" v-if="orderSource.status === 'W trakcie negocjacji' || orderSource.status === 'Oczekujące'" data-bs-toggle="modal" data-bs-target="#exampleModal">AKTUALIZUJ</button>
                    <button class="btn btn-4 float-end" v-else data-bs-toggle="modal" data-bs-target="#exampleModal">PRZEJDŹ DALEJ</button>
                </div>
            </div>
        </div>
        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" >
            <div class="modal-dialog modal-lg modal-dialog-scrollable">
                <div class="modal-content">
                    <div class="modal-header mx-3">
                        <h5 class="modal-title" id="exampleModalLabel">Upewnij się, że dane są poprawne</h5>
                        <button  class="btn btn-sm btn-4" data-bs-dismiss="modal" aria-label="Close">
                          <font-awesome-icon id="btn-close" icon="times" size="lg"/>
                        </button>
                    </div>
                    <div class="modal-body mx-3">
                        <div class="row">
                            <div class="col-6">
                                <p>
                                    <span> Termin wypożyczenia:</span>
                                    <br/>
                                    <span class="data">{{orderSource.startDate}} - {{orderSource.endDate}}</span>
                                </p>
                            </div>
                            <div class="col-6">
                                <p>
                                    <span> Adres eventu:</span>
                                    <br/>
                                    <span class="data">{{orderSource.address}}</span>
                                </p>
                            </div>
                        </div>
                        <div class="row">
                            <div class="col-6">
                                <p>
                                    <span> Transport:</span>
                                    <font-awesome-icon v-if="orderSource.isTransport" icon="check"></font-awesome-icon>
                                    <font-awesome-icon v-if="!orderSource.isTransport" icon="times"></font-awesome-icon>
                                </p>
                            </div>
                            <div class="col-6">
                                <p>
                                    <span>Koszt zamówienia: </span>
                                    <span class="data">{{orderSource.totalCost}} zł</span>
                                </p>
                            </div>
                        </div>
                        <div id="order-positions-table">
                            <table class="table table-responsive table-modal">
                                <thead>
                                    <tr>
                                        <th>Produkt</th>
                                        <th class="text-end">Liczba sztuk</th>
                                        <th class="text-end">Cena za sztukę</th>
                                        <th class="text-end">Cena razem</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr v-for="elem in orderSource.positions" :key="elem.product.prodId">
                                        <td>{{elem.product.prodName}}</td>
                                        <td class="text-end">{{elem.quantity}}</td>
                                        <td class="text-end">{{elem.product.price}} zł</td>
                                        <td class="text-end">{{(elem.quantity * elem.product.price).toFixed(2)}} zł</td>
                                    </tr>
                                </tbody>

                            </table>
                        </div>
                    </div>
                    <div class="modal-footer m-3">
                        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Zamknij</button>
                        <button type="button" class="btn btn-4" @click="sendOrder">Wyślij zapytanie</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import $ from 'jquery'
// import { Modal } from 'bootstrap'
export default {
  name: 'NewOrder',
  props: {
    orderSource: Object,
    activeUser: String,
    edit: Boolean
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
      $('#exampleModal button').click()
      // const myModal = new Modal(document.getElementById('exampleModal'))
      // myModal.hide()
      // $('#exampleModal').remove()
      this.$emit('send:order', this.redirect)
    },
    redirect () {
      this.$router.push({ name: 'Orders' })
    }
  }
}
</script>

<style scoped>
.new-order {
    background-color: var(--COLOR2);
    min-height: 90vh;
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

.modal-content {
    border-radius: 0;
}

.modal-header {
    border-bottom: none;
}

.modal-footer {
    border-top: none;
}

.table-modal, .table-modal th, .modal-body p, .modal-body span {
    color: var(--COLOR1);
}

.table-modal {
    font-weight: 400;
}

.modal-title {
    font-weight: 600;
}
</style>
