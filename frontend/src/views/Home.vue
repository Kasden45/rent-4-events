<template>
      <div id="intro" class="home">
        <div class="mask" id="bg">
          <div class="container">
            <div class="row">
              <p id="photo-text">
                Urządź swoje <br /> przyjęcie razem z nami
              </p>
            </div>
              <div class="row step justify-content-center mw-100">
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

</template>

<script>
import { domain, apiKey, apiUrl } from '../../auth_config.json'
import axios from 'axios'

export default {
  name: 'Home',
  props: {
    activeUser: String
  },
  methods: {
    async createClient () {
      const url = `${apiUrl}/clients/`
      if (this.$auth.isAuthenticated) {
        const token = await this.$auth.getTokenSilently()
        const idToken = await this.$auth.getIdTokenClaims()
        const meta = this.$auth.user
        console.log(JSON.stringify(meta))
        console.log('imie: ' + idToken.given_name + ' nazwisko: ' + idToken.family_name)
        const clientInfo = {
          firstName: idToken.given_name,
          lastName: idToken.family_name
          // phoneNumber:
        }
        axios.get(`https://${domain}/api/v2/users/${meta.sub}`, {headers: {Authorization: `Bearer ${apiKey}`}}).then((response) => {
          if (response.data.user_metadata !== undefined) {
            console.log(JSON.stringify(response.data.user_metadata.phone_number))
            clientInfo.phoneNumber = response.data.user_metadata.phone_number
          }

          axios.post(url, clientInfo, {headers: {Authorization: `Bearer ${token}`}})
        })
      } else {
        console.log('not authenticated!')
      }
    }
  },
  mounted () {
    this.createClient()
  }
}
</script>

<style scoped>

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
  width: 80%;
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
