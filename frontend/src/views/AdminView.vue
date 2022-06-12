<template>
    <div>
        <div>
            <button @click.prevent = "goHome">HOME ADMIN</button>
            <button @click.prevent = "goCreate">CREATE PRODUCTS</button>
            <button @click.prevent = "goDelete">DELETE PRODUCTS</button>
            <button @click.prevent = "goChange">CHANGE PRODUCTS</button>
            <router-link to="/simulator">SIMULATOR</router-link>
        </div>
        <div v-if = "home">HOME</div>
        <AdminCreateComponent v-if = "create" />
        <AdminDeleteComponent v-if = "delete_" />
        <AdminChangeComponent v-if = "change" />
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
            home: true,
            create: false,
            delete_: false,
            change: false
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
        goHome () {
            this.home = true
            this.create = false
            this.delete_ = false
            this.change = false
        },
        goCreate () {
            this.create = true
            this.delete_ = false
            this.change = false
            this.home = false
        },
        goDelete () {
            this.delete_ = true
            this.create = false
            this.change = false
            this.home = false
        },
        goChange () {
            this.change = true
            this.delete_ = false
            this.create = false
            this.home = false
        }

    }
}
</script>
