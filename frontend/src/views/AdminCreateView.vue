<template>
    <div class="contenedor_HOME">
        <div class="contenedor_app">
            <div class="AD_1">
                <AdminNavigator />
            </div>
            <div class="AD_2">
                <div class="AD_2_1">
                    <h2>WHEN CREATING A PRODUCT, ALL FIELDS MUST BE FILLED</h2>
                </div>
                <div class="AD_2_2">
                    <div class="AD_2_2_1">
                        <CreateMotherboard
                            v-model="resources.motherboard_list"
                        />
                    </div>
                    <div class="AD_2_2_2">
                        <CreateComponent
                            v-model="resources.component_list"
                        />
                    </div>
                    <div class="AD_2_2_3">
                        <CreateCompatible
                            :motherboard_list="resources.motherboard_list"
                            :component_list="resources.component_list"
                        />
                    </div>
                </div>
                <ErrorList
                    class="no-dots"
                    v-if="error"
                    :error_list="error_list"
                />
            </div>
        </div>

    </div>
</template>

<script>
import AdminNavigator from '@/components/AdminNavigator.vue'
import CreateMotherboard from '@/components/CreateMotherboard.vue'
import CreateComponent from '@/components/CreateComponent.vue'
import CreateCompatible from '@/components/CreateCompatible.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
    components: { CreateMotherboard, AdminNavigator, CreateComponent, CreateCompatible, ErrorList },
    data() {
        return {
            resources: {
                motherboard_list: [],
                component_list: []
            },
            error: false,
            error_list: ''
        }
    },
    mounted () {
        if (localStorage.getItem('token')) {
           // if (this.$root.user_info.role === 'admin') {
                fetch('http://127.0.0.1:5000/motherboards', { method: 'GET' })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true){
                        this.resources.motherboard_list = JsonResponse['motherboards']
                    }
                    else {
                        this.error_list.push(JsonResponse['message'])
                        this.error = true
                    }
                })
                .catch(() => {
                    this.error_list.push('Something went wrong!')
                    this.error = true
                })
                fetch('http://127.0.0.1:5000/components', { method: 'GET' })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true){
                        const components_array = Object.values(JsonResponse['components'])
                        this.resources.component_list = [
                            ...components_array.filter(component => component.component_type === "RAM"),
                            ...components_array.filter(component => component.component_type === "SSD"),
                            ...components_array.filter(component => component.component_type === "GPU"),
                            ...components_array.filter(component => component.component_type === "PC Cooling")
                        ]
                    }
                    else {
                        this.error_list.push(JsonResponse['message'])
                        this.error = true
                    }
                })
                .catch(() => {
                    this.error_list.push('Something went wrong!')
                    this.error = true
                })
            }
         //   else {
           //     this.$router.push('/simulator')
           // }
   //     }
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
        width: 300px;
        height: 500px;
        padding: 10px;
        overflow: scroll;

        display: flex;
        justify-content: center;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .AD_2_2_2 {
        width: 300px;
        height: 500px;
        padding: 10px;
        overflow: scroll;

        display: flex;
        justify-content: center;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .AD_2_2_3 {
        width: 300px;
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
    .AD_2_2_3::-webkit-scrollbar {
    width: 7px;
    }

    .AD_2_2_3::-webkit-scrollbar-thumb {
        background: rgb(47, 137, 172);
        border-radius: 5px 5px;
    }
</style>