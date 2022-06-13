<template>
    <div>
        <div>
            <button @click.prevent = "admin_routes.change_home">HOME ADMIN</button>
            <button @click.prevent = "admin_routes.change_create">CREATE PRODUCTS</button>
            <button @click.prevent = "admin_routes.change_delete_">DELETE PRODUCTS</button>
            <button @click.prevent = "admin_routes.change_change">CHANGE PRODUCTS</button>
            <router-link to="/simulator">SIMULATOR</router-link>
        </div>
        <div v-show = "admin_routes.home">HOME</div>
        <AdminCreateComponent v-show = "admin_routes.create" />
        <AdminDeleteComponent v-show = "admin_routes.delete_" />
        <AdminChangeComponent v-show = "admin_routes.change" />
    </div>
</template>

<script>
import AdminCreateComponent from '../components/AdminCreateComponent.vue'
import AdminDeleteComponent from '../components/AdminDeleteComponent.vue'
import AdminChangeComponent from '../components/AdminChangeComponent.vue'

export default {
    components: {AdminCreateComponent, AdminDeleteComponent, AdminChangeComponent},
    data() {
        return {
            admin_routes: {
                home: true,
                create: false,
                delete_: false,
                change: false,
                change_home: () => {
                    this.admin_routes.change_route({home: true})
                },
                change_create: () => {
                    this.admin_routes.change_route({create: true})
                },
                change_delete_: () => {
                    this.admin_routes.change_route({delete_: true})
                },
                change_change: () => {
                    this.admin_routes.change_route({change: true})
                },
                change_route: ({home=false, create=false, delete_=false, change=false} = {}) => {
                    this.admin_routes.home = home
                    this.admin_routes.create = create
                    this.admin_routes.delete_ = delete_
                    this.admin_routes.change = change
                }
            }
        }
    },
    mounted () {
        if (localStorage.getItem('token')){
            console.log('get data')
        }
        else {
            this.$router.push('/login')
        }
    },
    methods: {

    }
}
</script>
