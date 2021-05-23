import Vue from 'vue'
import Router from 'vue-router'
// import HelloWorld from '@/components/HelloWorld'
import Home from '../views/Home'
import Offer from '../views/Offer'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/Oferta',
      name: 'Offer',
      component: Offer
    }
  ]
})
