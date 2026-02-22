import Login from './login.js'
import Admin from './admin.js'
import AdminNavbar from './admin_navbar.js'
import User from './user.js'
import UserNavbar from './user_navbar.js'
import Register from './register.js'
import Home from './home.js'

const routes = [
    { path : '/login', component: Login},
    { path : '/admin', component: Admin },
    { path : '/admin_navbar', component: AdminNavbar },
    { path: '/user', component: User},
    { path : '/user_navbar', component: UserNavbar },
    { path: '/register', component:Register },
    { path: '/', component: Home }
]


const router = new VueRouter({
    routes
})

const app = new Vue({
    el : "#app",
    router,

    template: `
    <div class="container"> 

        <!-- Admin Navbar -->
        <admin-navbar v-if="$route.path.startsWith('/admin')"></admin-navbar>

        <!-- User Navbar -->
        <user-navbar v-if="$route.path.startsWith('/user')"></user-navbar>

         <router-view :loggedIn = 'loggedIn' @login = "handleLogin"> </router-view>   
    </div>
    `,
    data : {
        loggedIn: !!localStorage.getItem("auth_token")
    },

    components : {
        "admin-navbar" : AdminNavbar,
        "user-navbar" : UserNavbar
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