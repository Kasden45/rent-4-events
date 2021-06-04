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
                <tr v-for="elem in orderSource.positions" :key="elem.prodId">
                    <td>{{elem.product}}</td> <!--DODAĆ PRODNAME!!!!!!!!!!!!!!!!!!!!!!! I WYLICZANIE KOSZTÓW ZAMÓWIENIA-->
                    <td>
                        <div class="col-6">
                            <input class="form-control" type="number" :value="elem.quantity">
                        </div>
                    </td>
                    <td>
                        <button class="btn btn-sm btn-danger" @click="handleDelete(elem.product)">X</button>
                    </td>
                </tr>
<!--                <tr>-->
<!--                    <td>Piesekkkkkkkkk njcnscn jd</td>-->
<!--                    <td>-->
<!--                        <div class="col-6">-->
<!--                            <input class="form-control" type="number" value="1">-->
<!--                        </div>-->

<!--                    </td>-->
<!--                    <td>-->
<!--                        <button class="btn btn-sm btn-danger">X</button>-->
<!--                    </td>-->
<!--                </tr>-->
            </tbody>
        </table>
        </div>

        <div>
            <p>
                <span> Termin wypożyczenia:</span>
                <br/>
                <span class="data">{{orderSource.startDate}} - {{orderSource.endDate}}</span>
            </p>
            <p>
                <span>Koszt zamówienia: </span>
                <span class="data">{{orderSource.totalCost}} zł</span>
            </p>
            <button class="btn btn-4 float-end">Złóż zapytanie</button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'NewOrder',
  props: {
    orderSource: Object
  },
  methods: {
    handleDelete (id) {
      this.$emit('delete:product', id)
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
    opacity: 90%;
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
</style>
