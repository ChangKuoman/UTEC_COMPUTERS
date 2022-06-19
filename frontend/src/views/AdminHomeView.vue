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
                // here nothing happens
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
