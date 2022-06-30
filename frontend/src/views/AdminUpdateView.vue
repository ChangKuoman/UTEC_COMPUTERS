<template>
    <div class="contenedor_HOME">
        <div class="contenedor_app">
            <div class="AD_1">
                <AdminNavigator />
            </div>
            <div class="AD_2">
                <h1>
                    UPDATE CANNOT BE MADE TO ID, IF YOU DONT PUT ANYTHING, IT WILL NOT BE UPDATED
                </h1>

                <UpdateMotherboard />

                <UpdateComponent />
            </div>
        </div>
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

<style scoped>
    .AD_1{
        min-height: 120px;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .AD_2{
        min-height: 750px;
        width:100%;
        display: flex;
        align-items: center;
        justify-content: center;

        padding: 10px;
    }
</style>