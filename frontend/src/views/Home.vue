<template>

      <div id="intro" class="home">
        <div class="mask" id="bg">
          <div class="container">
            <div class="row">
              <p id="photo-text">
                Urządź swoje <br /> przyjęcie razem z nami
              </p>
              <div class="row step justify-content-center">
                <div class="col-md-3 line">
                  <img src="../assets/number1.png" alt="one" height="50px" width="auto" class="mx-auto d-block my-3">
                  <p class="step-title">Wybierz asortyment</p>
                  <p>Posiadamy szeroki asortyment, na pewno znajdziesz coś, co Cię zainteresuje</p>
                </div>
                <div class="col-md-3 line mx-2">
                  <img src="../assets/number2.png" alt="two" height="50px" width="auto" class="mx-auto d-block my-3">
                  <p class="step-title">Złóż zapytanie</p>
                  <p>Powiedz gdzie i kiedy chcesz zrealizować swoje zamówienie i wyślij zapytanie</p>
                </div>
                <div class="col-md-3 mx-2">
                  <img src="../assets/number3.png" alt="three" height="50px" width="auto" class="mx-auto d-block my-3">
                  <p class="step-title">Czekaj na odpowiedź</p>
                  <p>Nasz zespoł stara się odpowiadać jak najszybciej na zamówienia naszych Klientów, niedługo się odezwiemy!</p>
                </div>

              </div>
            </div>
          </div>
        </div>
      </div>

</template>

<script>

export default {
  name: 'Home'
}
</script>

<style scoped>

html {
    width: 100%;

}

#intro {
    color: #FFFFFF;
}

#intro {
  height: 80vh;
  width: 100%;
  background: url("../assets/event.jpg") no-repeat center center fixed;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}

#bg {
  height: 80vh;
  width: 100%;
  background: linear-gradient(
  150deg,
      rgba(0, 0, 0, 0.0),
      rgba(0, 0, 0, 0.5) 50%);
}

#photo-text {
  position: absolute;
  width: 100%;
  bottom: 55%;
  left: 10%;
  padding: 10px;
  font-weight: bold;
  font-size: 400%;
}

.step {
  position: absolute;
  bottom: 20%;
  left: 0;
  text-align: center;
}

.step-title {
  font-size: 24px;
  font-weight: bold;
}

.line {
  border-right: 1px solid #FFFFFF;
}

.container {
  height: inherit;
}

</style>
