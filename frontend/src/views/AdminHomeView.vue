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
        if (localStorage.getItem('token') && this.$root.user_info.role === 'admin'){
            console.log('admin home view get data')
        }
        else {
            this.$router.push('/login')
        }
    }
}
</script>
