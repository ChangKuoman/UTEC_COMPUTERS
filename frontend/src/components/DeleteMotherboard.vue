<template>
    <div>
        <h2>DELETE MOTHERBOARD</h2>
        <form @change="clearError()">
            <select v-model="motherboard">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option v-for="(motherboard, index) in motherboard_list" :key="index" :value="motherboard.id">{{motherboard.name}}</option>
            </select>
            <button @click.prevent="clearError(); deleteMotherboard()">DELETE</button>
        </form>
        <p :v-if="error_show">
            {{error_text}}
        </p>
    </div>
</template>

<script>
export default {
    name: 'DeleteMotherboard',
    props: [ 'motherboard_list' ],
    data () {
        return {
            motherboard: '',
            error_show: false,
            error_text: ''
        }
    },
    methods: {
        clearError () {
            this.error_show = false
            this.error_text = ''
        },
        deleteMotherboard () {
            if (this.motherboard === '') {
                this.error_show = true
                this.error_text = 'You must select a motherboard to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/motherboards/' + this.motherboard, { method: 'DELETE' })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.motherboard = ''
                        this.$emit('onUpdateMotherboards')
                        this.$emit('onUpdateCompatibles')
                        alert("DELETED MOTHERBOARD SUCCESSFULLY")
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
