<template>
    <div class="new-order">
        <p>PODSUMOWANIE</p>
        <div class="tab-content">
            <table class="table table-sm table-borderless ">
            <thead>
                <tr>PRODUKT</tr>
                <tr>SZT</tr>
                <tr></tr>
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
            <button class="btn btn-primary">Złóż zapytanie</button>
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
    background-color: #267478;
    height: 80vh;
    box-shadow: 0 0 1rem 0 rgba(0, 0, 0, .2);
    border-bottom-left-radius: 15px;
    border-top-left-radius: 15px;
    /*opacity: 60%;*/

}

.tab-content {
    height: 50vh;
    overflow: auto;
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
