import Login from './login.js'
import Admin from './admin.js'
import User from './user.js'
import Register from './register.js'

const routes = [
    { path : '/login', component: Login},
    { path : '/admin', component: Admin },
    { path: '/user', component: User},
    { path: '/register', component:Register }
]


const router = new VueRouter({
    routes
})

const app = new Vue({
    el : "#app",
    router,

    template: `
    <div class="container"> 
         <router-view :loggedIn = 'loggedIn' @login = "handleLogin"> </router-view>   
    </div>
    `,
    data : {
        loggedIn : false
    },
    methods: {
        handleLogin(){
            this.loggedIn = true
        },
        handleLogout(){
            this.loggedIn = false
        }
    }


})