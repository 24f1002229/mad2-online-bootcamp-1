export default {
    template: `
    <div>
        <h1 style="text-align:center;" > Vehicle Parking App</h1>
        <p style="text-align:center;"> This is a Vehicle Parking App used for park your car. this is very helpful you should use it.</p> 
        <div> 
            <router-link v-if="!loggedIn" class="btn btn-primary" to="/login"> Login </router-link>
            <router-link v-if="!loggedIn" class="btn btn-warning" to="/register"> Register </router-link>
        </div>
    </div>
    `
}