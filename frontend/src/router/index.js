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
import Vehicles from '../views/Vehicles'
import Courses from '../views/Courses'
import Products from '../views/Products'
import CurrentCourse from '../views/CurrentCourse'
import Reports from '../views/Reports'

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
      component: Offer,
      beforeEnter: auth
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
      path: '/Pojazdy',
      name: 'Vehicles',
      component: Vehicles,
      beforeEnter: authGuard
    },
    {
      path: '/Kursy',
      name: 'Courses',
      component: Courses,
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
      beforeEnter: auth
    },
    {
      path: '/Asortyment',
      name: 'Products',
      component: Products,
      beforeEnter: authGuard
    },
    {
      path: '/AktualnyKurs',
      name: 'CurrentCourse',
      component: CurrentCourse,
      beforeEnter: authGuard
    },
    {
      path: '/Raporty',
      name: 'Reports',
      component: Reports,
      beforeEnter: authGuard
    }
  ]
})
