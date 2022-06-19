<template>
    <div>
        <AdminNavigator />
    </div>
</template>

<script>
import AdminNavigator from '@/components/AdminNavigator.vue'

export default {
    components: { AdminNavigator },
    mounted () {
        if (localStorage.getItem('token')){
            if (this.$root.user_info.role === 'admin') {
                console.log('admin home view get data')
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
