<template>
    <div>
        <AdminNavigator />
        <h1>WHEN CREATING A PRODUCT, ALL FIELDS MUST BE FILLED</h1>

        <CreateMotherboard
            v-model="resources.motherboard_list"
        />

        <CreateComponent
            v-model="resources.component_list"
        />

        <CreateCompatible
            :motherboard_list="resources.motherboard_list"
            :component_list="resources.component_list"
        />

        <ErrorList
            class="no-dots"
            v-if="error"
            :error_list="error_list"
        />
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
            if (this.$root.user_info.role === 'admin') {
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
                    console.log(JsonResponse)
                    if (JsonResponse['success'] === true){
                        const components_array = Object.values(JsonResponse['components'])
                        this.resources.component_list = [
                            ...components_array.filter(component => component.component_type === "RAM"),
                            ...components_array.filter(component => component.component_type === "SSD"),
                            ...components_array.filter(component => component.component_type === "GPU"),
                            ...components_array.filter(component => component.component_type === "PC Cooling")
                        ]
                        console.log(this.resources.component_list)
                    }
                    else {
                        this.error_list.push(JsonResponse['message'])
                        this.error = true
                    }
                })
                .catch(() => {
                    console.log("error js")
                    this.error_list.push('Something went wrong!')
                    this.error = true
                })
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
