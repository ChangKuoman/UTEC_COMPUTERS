<template>
    <div>
        <h2>DELETE COMPATIBLE</h2>
        <form @change="clearError()">
            <select v-model="compatible">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option v-for="(compatible, index) in compatible_list" :key="index" :value="compatible.id">
                    Motherboard: {{compatible.motherboard}} - Component: {{compatible.component}}
                </option>
            </select>
            <button @click.prevent="clearError(); deleteCompatible()">DELETE</button>
        </form>
        <p :v-if="error_show">
            {{error_text}}
        </p>
    </div>
</template>

<script>
export default {
    name: 'DeleteCompatible',
    props: [ 'compatible_list' ],
    data () {
        return {
            error_show: false,
            error_text: '',
            compatible: ''
        }
    },
    methods: {
        clearError () {
            this.error_show = false
            this.error_text = ''
        },
        deleteCompatible () {
            if (this.compatible === '') {
                this.error_show = true
                this.error_text = 'You must select a compatible to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/compatibles/' + this.compatible, { method: 'DELETE' })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.compatible = ''
                        this.$emit('onUpdateCompatibles')
                        alert("DELETED COMPATIBLES SUCCESSFULLY")
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