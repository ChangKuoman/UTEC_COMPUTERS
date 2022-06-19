<template>
    <div>
        <h2>UPDATE COMPONENT</h2>
        <form v-if="!error_text.length" @change.prevent="clearError()">
            <select v-model="component">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option :value="component_e" v-for="(component_e, index) in component_list" :key="index">{{component_e.name}}</option>
            </select>
            <InputText
                v-model="name"
                title="NEW COMPONENT NAME"
                type="text"
            />
            <InputText
                v-model="price"
                title="NEW COMPONENT PRICE"
                type="number"
                step="0.01"
            />
            <InputText
                v-model="description"
                title="NEW COMPONENT DESCRIPTION"
                type="text"
            />
            <p>NEW COMPONENT TYPE</p>
            <select v-model="type">
                <option value="" hidden selected>SELECT AN OPTION</option>
                <option value="RAM">RAM (Random Access Memory)</option>
                <option value="SSD">SSD (Solid State Drive)</option>
                <option value="HDD">HDD (Hard Drive Disk)</option>
                <option value="CPU">CPU (Central Processing Unit)</option>
                <option value="GPU">GPU (Graphics Processing Unit)</option>
                <option value="PSU">PSU (Power Supply Unit)</option>
                <option value="PC Cooling">PC Cooling</option>
                <option value="Peripheral">Peripheral</option>
            </select>
            <button @click.prevent="clearError(); checkForm()">UPDATE</button>
        </form>
        <ErrorList
            class="no-dots"
            v-if="error_list.length"
            :error_list="error_list"
        />
        <div v-if="error_text.length">There are no components to update</div>
    </div>
</template>

<script>
import InputText from '@/components/InputText.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
    name: 'UpdateComponent',
    components: { InputText, ErrorList },
    data () {
        return {
            error_list: [],
            error_text: '',
            name: '',
            price: 0,
            description: '',
            type: '',
            component: '',
            component_list: []
        }
    },
    mounted () {
        fetch('http://127.0.0.1:5000/components', { method: 'GET' })
        .then(response => response.json())
        .then(JsonResponse => {
            if (JsonResponse['success'] === true){
                this.component_list = Object.values(JsonResponse['components'])
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
            if (this.component === '') {
                this.error_list.push('Select a component to update')
            }
            else if (this.name === '' && this.price === 0 && this.description === '' && this.type === '') {
                this.error_list.push('You must fill at least 1 field to update')
            }
            else {
                if (this.price === this.component.price) {
                    this.error_list.push('Component price cannot be the same')
                }
                else if (this.price < 0) {
                    this.error_list.push("Component price cannot be negative")
                }
                if (this.description === this.component.description) {
                    this.error_list.push('Component description cannot be the same')
                }
                if (this.type === this.component.component_type) {
                    this.error_list.push('Component type cannot be the same')
                }
                if (this.name === this.component.name) {
                    this.error_list.push('Component name cannot be the same')
                }
                else if (Object.values(this.component_list).map(component => component.name).includes(this.name)) {
                    this.error_list.push('Component name exists in database')
                }
            }
            if (!this.error_list.length) {
                this.updateComponent()
            }
        },
        updateComponent () {
            const name = this.name!='' ? {'name': this.name} : {}
            const description = this.description!='' ? {'description': this.description} : {}
            const price = this.price!=0 ? {'price': this.price} : {}
            const type = this.type!='' ? {'type': this.type} : {}
            const modify_by = {'modify_by': this.$root.user_info.id}
            const result = Object.assign(name, description, price, type, modify_by)

            fetch('http://127.0.0.1:5000/components/' + this.component.id, {
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
                    this.type = ''
                    this.component = ''
                    this.component_list = JsonResponse['components']
                    alert('COMPONENT UPDATED SUCCESSFULLY')
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
