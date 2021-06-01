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
<!--                <tr v-for="elem in orderSource" :key="elem.prodId">-->
<!--                    <td>{{elem.product}}</td>-->
<!--                    <td>{{elem.quantity}}</td>-->
<!--                    <td>-->
<!--                        <button class="btn btn-danger">X</button>-->
<!--                    </td>-->
<!--                </tr>-->
                <tr>
                    <td>Piesekkkkkkkkk njcnscn jd</td>
                    <td>
                        <div class="col-6">
                            <input class="form-control" type="number" value="1">
                        </div>

                    </td>
                    <td>
                        <button class="btn btn-sm btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr><tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr><tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>
            <tr>
                    <td>Piesek</td>
                    <td>5</td>
                    <td>
                        <button class="btn btn-danger">X</button>
                    </td>
                </tr>

            </tbody>
        </table>
        </div>

        <div>
            <p>Termin wypożyczenia:</p>
            <p>{{orderSource.startDate}} - {{orderSource.endDate}}</p>
            <p>Koszt zamówienia: {{orderSource.totalCost}}</p>
            <button class="btn btn-3 float-end">Złóż zapytanie</button>
        </div>
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
    background-color: var(--COLOR2);
    max-height: 90vh;
    color: #FFFFFF;
    opacity: 90%;
}

.tab-content {
    height: 50vh;
    overflow: auto;
}

.table {
    color: #FFFFFF;
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
