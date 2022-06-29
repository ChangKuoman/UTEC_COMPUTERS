<template>
    <div>
        <h2>UPDATE MOTHERBOARD</h2>
        <form v-if="!error_text.length" @change.prevent="clearError()">
            <select v-model="motherboard">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option :value="motherboard_e" v-for="(motherboard_e, index) in motherboard_list" :key="index">{{motherboard_e.name}}</option>
            </select>
            <InputText
                v-model="name"
                title="NEW MOTHERBOARD NAME"
                type="text"
            />
            <InputText
                v-model="price"
                title="NEW MOTHERBOARD PRICE"
                type="number"
                step="0.01"
            />
            <InputText
                v-model="description"
                title="NEW MOTHERBOARD DESCRIPTION"
                type="text"
            />
            <button @click.prevent="clearError(); checkForm()">UPDATE</button>
        </form>
        <ErrorList
            class="no-dots"
            v-if="error_list.length"
            :error_list="error_list"
        />
        <div v-if="error_text.length">There are no motherboards to update the motherboard</div>
    </div>
</template>

<script>
import InputText from '@/components/InputText.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
    name: 'UpdateMotherboard',
    components: { InputText, ErrorList },
    data () {
        return {
            error_list: [],
            error_text: '',
            name: '',
            price: 0,
            description: '',
            motherboard: '',
            motherboard_list: []
        }
    },
    mounted () {
        fetch('http://127.0.0.1:5000/motherboards', { method: 'GET' })
        .then(response => response.json())
        .then(JsonResponse => {
            if (JsonResponse['success'] === true){
                this.motherboard_list = JsonResponse['motherboards']
            }
            else {
                this.error_text = JsonResponse['message']
            }
        })
        .catch(() => {
            this.error_text = 'Something went wrong!'
        })
    },
    methods: {
        clearError () {
            this.error_list = []
        },
        checkForm () {
            if (this.motherboard === '') {
                this.error_list.push('Select a motherboard to update')
            }
            else if (this.name === '' && this.price === 0 && this.description === '') {
                this.error_list.push('You must fill at least 1 field to update')
            }
            else {
                if (this.price === this.motherboard.price) {
                    this.error_list.push('Motherboard price cannot be the same')
                }
                else if (this.price < 0) {
                    this.error_list.push("Motherboard price cannot be negative")
                }
                if (this.description === this.motherboard.description) {
                    this.error_list.push('Motherboard description cannot be the same')
                }
                if (this.name === this.motherboard.name) {
                    this.error_list.push('Motherboard name cannot be the same')
                }
                else if (Object.values(this.motherboard_list).map(motherboard => motherboard.name).includes(this.name)) {
                    this.error_list.push('Motherboard name exists in database')
                }
            }
            if (!this.error_list.length) {
                this.updateMotherboard()
            }
        },
        updateMotherboard () {
            const name = this.name!='' ? {'name': this.name} : {}
            const description = this.description!='' ? {'description': this.description} : {}
            const price = this.price!=0 ? {'price': this.price} : {}
            const modify_by = {'modify_by': this.$root.user_info.id}
            const result = Object.assign(name, description, price, modify_by)

            fetch('http://127.0.0.1:5000/motherboards/' + this.motherboard.id, {
                method: 'PATCH',
                body: JSON.stringify(
                    result
                ),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    this.name = ''
                    this.description = ''
                    this.price = 0
                    this.motherboard = ''
                    this.motherboard_list = JsonResponse['motherboards']
                    alert('MOTHERBOARD UPDATED SUCCESSFULLY')
                }
                else {
                    this.error_list.push(JsonResponse['message'])
                }
            })
            .catch(() => {
                this.error_list.push('Something went wrong!')
            })
        }
    }
}
</script>
