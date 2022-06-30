<template>
    <div class="contenedor_HOME">
        <div class="contenedor_app">
            <div class="AD_1">
                <AdminNavigator />
            </div>
            <div class="AD_2">
                <div class="AD_2_1">
                    <h2>
                        UPDATE CANNOT BE MADE TO ID, IF YOU DONT PUT ANYTHING, IT WILL NOT BE UPDATED
                    </h2>
                </div>
                <div class="AD_2_2">
                    <div class="AD_2_2_1">
                        <UpdateMotherboard />
                    </div>
                    <div class="AD_2_2_2">
                        <UpdateComponent />
                    </div>
                </div>
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
        flex-direction: column;
        align-items: center;
        justify-content: center;

        padding: 10px;
    }
    .AD_2_1 {
        width: 100%;
        height: 10%;
        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .AD_2_2 {
        width: 100%;
        height: 80%;
        display: flex;
        flex-direction: row;
        justify-content: space-evenly;
        align-items: center;
    }
    .AD_2_2_1 {
        width: 350px;
        height: 500px;
        padding: 10px;
        overflow: scroll;

        display: flex;
        justify-content: center;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .AD_2_2_2 {
        width: 350px;
        height: 500px;
        padding: 10px;
        overflow: scroll;

        display: flex;
        justify-content: center;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .AD_2_2_1::-webkit-scrollbar {
    width: 7px;
    }

    .AD_2_2_1::-webkit-scrollbar-thumb {
        background: rgb(47, 137, 172);
        border-radius: 5px 5px;
    }
    .AD_2_2_2::-webkit-scrollbar {
    width: 7px;
    }

    .AD_2_2_2::-webkit-scrollbar-thumb {
        background: rgb(47, 137, 172);
        border-radius: 5px 5px;
    }
</style>