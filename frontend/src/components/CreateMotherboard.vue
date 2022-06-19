<template>
    <div>
        <h2>CREATE MOTHERBOARD</h2>
        <form @change = "clearError">
            <InputText
                v-model="name"
                title="MOTHERBOARD NAME"
                type="text"
            />
            <InputText
                v-model="description"
                title="MOTHERBOARD DESCRIPTION"
                type="text"
            />
            <InputText
                v-model="price"
                title="MOTHERBOARD PRICE"
                type="number"
                step="0.01"
            />
            <button @click.prevent="clearError(); checkFormMotherboard()">CREATE</button>
        </form>
        <ErrorList
            class="no-dots"
            v-if="error"
            :error_list="error_list"
        />
    </div>
</template>

<script>
import InputText from '@/components/InputText.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
    name: 'CreateMotherboard',
    components: { InputText, ErrorList },
    data () {
        return {
            name: '',
            description: '',
            price: 0,
            error_list: [],
            error: false
        }
    },
    methods: {
        clearError() {
            this.error_list = []
            this.error = false
        },
        checkFormMotherboard () {
            if (this.name === ''){
                this.error_list.push('Motherboard name is required.')
            }
            if (this.description === ''){
                this.error_list.push('Motherboard description is required')
            }
            if (this.price === 0){
                this.error_list.push('Motherboard price cannot de 0')
            }
            else if (this.price < 0){
                this.error_list.push('Motherboard price cannot be negative')
            }
            if (this.error_list.length) {
                this.error = true
            }
            if (this.error === false) {
                this.createMotherboard()
            }
        },
        createMotherboard () {
            fetch('http://127.0.0.1:5000/motherboards', {
                method: 'POST',
                body: JSON.stringify({
                    'name': this.name,
                    'description': this.description,
                    'price': this.price,
                    'create_by': this.$root.user_info.id
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    this.$emit('update:modelValue', JsonResponse['motherboards'])
                    this.name = ''
                    this.description = ''
                    this.price = 0
                    alert("MOTHERBOARD ADDED SUCCESSFULLY")
                }
                else {
                    this.error = true
                    this.error_list.push(JsonResponse['message'])
                }
            }).catch(() => {
                this.error = true
                this.error_list.push('Something went wrong!')
            })
        },
    }
}
</script>
