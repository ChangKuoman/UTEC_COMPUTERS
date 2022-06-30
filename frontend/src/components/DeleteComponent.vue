<template>
    <div>
        <h3>DELETE COMPONENT</h3>
        <form @change="clearError()">
            <select v-model="component">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option v-for="(component, index) in component_list" :key="index" :value="component.id">{{component.name}}</option>
            </select>
            <button @click.prevent="clearError(); deleteComponent()">DELETE</button>
        </form>
        <p :v-if="error_show">
            {{error_text}}
        </p>
    </div>
</template>

<script>
export default {
    name: 'DeleteComponent',
    props: [ 'component_list' ],
    data () {
        return {
            error_show: false,
            error_text: '',
            component: ''
        }
    },
    methods: {
        clearError () {
            this.error_show = false
            this.error_text = ''
        },
        deleteComponent () {
            if (this.component === '') {
                this.error_show = true
                this.error_text = 'You must select a component to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/components/' + this.component, { method: 'DELETE' })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.component = ''
                        this.$emit('onUpdateComponents')
                        this.$emit('onUpdateCompatibles')
                        alert("DELETED COMPONENT SUCCESSFULLY")
                    }
                    else {
                        this.error_show = true
                        this.error_text = JsonResponse['message']
                    }
                })
                .catch(() => {
                    this.error_show = true
                    this.error_text = 'Something went wrong!'
                })
            }
        }
    }
}
</script>
