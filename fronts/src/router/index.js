import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Single from '../views/Single.vue'
import SignIn from '../components/SignIn.vue'
import SignUp from '../components/SignUp.vue'
import Cart from '../components/Cart.vue'

Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        name: 'Home',
        component: Home
    },
    {
        path : '/:id',
        name: 'Single',
        component: Single,
        props: true
    },
    {
        path: '/login',
        name: 'login',
        meta: {},
        component: SignIn,
    },
    {
        path: '/registration',
        name: 'registration',
        meta: {},
        component: SignUp,
    },
    {
        path: '/about',
        name: 'About',
        // route level code-splitting
        // this generates a separate chunk (about.[hash].js) for this route
        // which is lazy-loaded when the route is visited.
        component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
    },
    {
        path: '/cart',
        name: 'Cart',
        beforeEnter: (to, from, next) => {
            const auth = localStorage.getItem('authentication');
            if (auth)  {
                next()
            } else {
                next('/login')
            }
        },
        component: Cart
    }
]

const router = new VueRouter({
    mode: 'history',
    routes
})

export default router