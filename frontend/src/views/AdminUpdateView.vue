<template>
    <div>
        <AdminNavigator />

        <h1>
            UPDATE CANNOT BE MADE TO ID, IF YOU DONT PUT ANYTHING, IT WILL NOT BE UPDATED
        </h1>

        <UpdateMotherboard />

        <UpdateComponent />

    </div>
</template>

<script>
import AdminNavigator from '@/components/AdminNavigator.vue'
import UpdateMotherboard from '@/components/UpdateMotherboard.vue'
import UpdateComponent from '@/components/UpdateComponent.vue'

export default {
    components: { AdminNavigator, UpdateMotherboard, UpdateComponent },
    mounted () {
        if (localStorage.getItem('token')){
            if (this.$root.user_info.role === 'admin') {
                console.log('admin update view get data')
            }
            else {
                this.$router.push('/simulator')
            }
        }
        else {
            this.$router.push('/login')
        }
    }
}
</script>
