<template>
    <div class="contenedor_HOME">
        <div class="contenedor_app">
            <div class="AD_1">
                <AdminNavigator />
            </div>
            <div class="AD_2">
                <h1>
                    WHEN A MOTHERBOARD OR COMPONENT IS DELETED, COMPATIBILITIES AND SIMULATIONS RELATED ARE ALSO REMOVED
                </h1>

                <DeleteMotherboard
                    v-if="!errors.motherboard.text"
                    :motherboard_list="resources.motherboard_list"
                    @onUpdateMotherboards="getMotherboards()"
                    @onUpdateCompatibles="getCompatibles()"
                />
                <div v-if="errors.motherboard.text">There are no motherboards to show</div>

                <DeleteComponent
                    v-if="!errors.component.text"
                    :component_list="resources.component_list"
                    @onUpdateComponents="getComponents()"
                    @onUpdateCompatibles="getCompatibles()"
                />
                <div v-if="errors.component.text">There are no components to show</div>

                <DeleteCompatible
                    v-if="!errors.compatible.text"
                    :compatible_list="resources.compatible_list"
                    @onUpdateCompatibles="getCompatibles()"
                />
                <div v-if="errors.compatible.text">There are no compatibles to show</div>

                </div>
        </div>
    </div>
</template>

<script>
import AdminNavigator from '@/components/AdminNavigator.vue'
import DeleteMotherboard from '@/components/DeleteMotherboard.vue'
import DeleteComponent from '@/components/DeleteComponent.vue'
import DeleteCompatible from '@/components/DeleteCompatible.vue'

export default {
    components: { AdminNavigator, DeleteMotherboard, DeleteComponent, DeleteCompatible },
    data () {
        return {
            resources: {
                motherboard_list: [],
                component_list: [],
                compatible_list: []
            },
            errors: {
                motherboard: {
                    text: '',
                    clear: () => {
                        this.errors.motherboard.text = ''
                    }
                },
                component: {
                    text: '',
                    clear: () => {
                        this.errors.component.text = ''
                    }
                },
                compatible: {
                    text: '',
                    clear: () => {
                        this.errors.compatible.text = ''
                    }
                }
            },
            error: false,
            error_list: []
        }
    },
    methods: {
        getCompatibles() {
            this.errors.compatible.clear()
            fetch('http://127.0.0.1:5000/compatibles', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.resources.compatible_list = Object.values(JsonResponse['compatibles'])
                }
                else {
                    this.errors.compatible.text = JsonResponse['message']
                }
            })
            .catch(() => {
                this.errors.compatible.text = 'Something went wrong!'
            })
        },
        getMotherboards () {
            this.errors.motherboard.clear()
            fetch('http://127.0.0.1:5000/motherboards', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.resources.motherboard_list = JsonResponse['motherboards']
                }
                else {
                    this.errors.motherboard.text = JsonResponse['message']
                }
            })
            .catch(() => {
                this.errors.motherboard.text = 'Something went wrong!'
            })
        },
        getComponents () {
            this.errors.component.clear()
            fetch('http://127.0.0.1:5000/components', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.resources.component_list = Object.values(JsonResponse['components'])
                }
                else {
                    this.errors.component.text = JsonResponse['message']
                }
            })
            .catch(() => {
                this.errors.component.text = 'Something went wrong!'
            })
        }
    },
    mounted () {
        if (localStorage.getItem('token')) {
            if (this.$root.user_info.role === 'admin') {
                this.getComponents()
                this.getCompatibles()
                this.getMotherboards()
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