import Vue from 'vue'
import Router from 'vue-router'
import Home from '../views/Home'
import Offer from '../views/Offer'
import Orders from '../views/Orders'
import Order from '../views/Order'
// import OrderEdit from '../views/OrderEdit'
import Drivers from '../views/Drivers'
import OrderPreview from '../views/OrderPreview'
import ProductPreview from '../views/ProductPreview'

import { authGuard, auth } from '../auth/authGuard'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home,
      beforeEnter: auth
    },
    {
      path: '/Oferta',
      name: 'Offer',
      component: Offer
    },
    {
      path: '/Zamowienia',
      name: 'Orders',
      component: Orders,
      beforeEnter: authGuard
    },
    {
      path: '/Zamowienia/Nowe',
      name: 'Order',
      component: Order,
      beforeEnter: authGuard
    },
    {
      path: '/Kadra',
      name: 'Drivers',
      component: Drivers,
      beforeEnter: authGuard
    },
    {
      path: '/Zamowienia/:orderId',
      name: 'OrderPreview',
      component: OrderPreview,
      beforeEnter: authGuard
    },
    {
      path: '/Zamowienia/:orderId/Edycja',
      name: 'OrderEdit',
      component: Order,
      beforeEnter: authGuard
    },
    {
      path: '/Produkt/:prodId',
      name: 'ProductPreview',
      component: ProductPreview,
      beforeEnter: authGuard
    }
  ]
})
