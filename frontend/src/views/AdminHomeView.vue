<template>
    <div class="contenedor_HOME">
        <div class="contenedor_app">
            <div class="AD_1">
                <AdminNavigator />
            </div>
            <div class="AD_2">

            </div>
        </div>
    </div>
</template>

<script>
import { host } from '@/host.js';
import AdminNavigator from '@/components/AdminNavigator.vue'

export default {
    components: { AdminNavigator },
    mounted () {
        if (localStorage.getItem('token')){
            fetch(host + '/users', {
                method: 'POST',
                body: JSON.stringify({
                    'token': localStorage.getItem('token'),
                    'admin': true
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    // Here nothing happens
                }
                else {
                    this.$router.push('/')
                }
            })
            .catch(() => {
                this.$router.push('/login')
            })
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