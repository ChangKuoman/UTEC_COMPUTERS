<template>
    <div>
        <h2>CREATE COMPATIBLE</h2>
        <form @change = "clearError()">
            <p>MOTHERBOARD</p>
            <select v-model = "motherboard">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option v-for="(motherboard_e, index) in motherboard_list" :key="index" :value="motherboard_e.id">{{motherboard_e.name}}</option>
            </select>

            <p>COMPONENT</p>
            <select v-model = "component">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option v-for="(component_e, index) in component_list" :key="index" :value="component_e.id">{{component_e.name}}</option>
            </select>
            <button @click.prevent = "clearError(); checkFormCompatible()">CREATE</button>
        </form>
        <ErrorList
            class="no-dots"
            v-if="error"
            :error_list="error_list"
        />
    </div>
</template>

<script>
import ErrorList from '@/components/ErrorList.vue'

export default {
    name: 'CreateCompatible',
    components: { ErrorList },
    props: [ 'motherboard_list', 'component_list' ],
    data () {
        return {
            motherboard: '',
            component: '',
            error: false,
            error_list: []
        }
    },
    methods: {
        clearError() {
            this.error_list = []
            this.error = false
        },
        checkFormCompatible () {
            if (this.motherboard === "") {
                this.error_list.push('Motherboard for compatible cannot be empty')
            }
            if (this.component === "") {
                this.error_list.push("Component for compatible cannot be empty")
            }
            if (this.error_list.length) {
                this.error = true
            }
            if (this.error === false) {
                this.createCompatible()
            }
        },
        createCompatible () {
            fetch('http://127.0.0.1:5000/compatibles', {
                method: 'POST',
                body: JSON.stringify({
                    'id_motherboard': this.motherboard,
                    'id_component': this.component,
                    'token': localStorage.getItem('token')
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    this.motherboard = ''
                    this.component = ''
                    alert("COMPATIBLE ADDED SUCCESSFULLY")
                }
                else {
                    this.error = true
                    this.error_list.push(JsonResponse['message'])
                }
            }).catch(() => {
                this.error = true
                this.error_list.push('Something went wrong!')
            })
        }
    }
}
</script>
