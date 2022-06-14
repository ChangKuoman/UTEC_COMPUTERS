<template>
    <div>
        <h1>
            WHEN CREATING A PRODUCT, ALL FIELDS MUST BE FILLED
        </h1>

        <div>
            <h2>CREATE MOTHERBOARD</h2>
            <form @change = "motherboard.clear">
                <p>MOTHERBOARD NAME</p>
                <input v-model = "motherboard.name" type="text"/>
                <p>MOTHERBOARD DESCRIPTION</p>
                <input v-model = "motherboard.description" type="text"/>
                <p>MOTHERBOARD PRICE</p>
                <input v-model = "motherboard.price" type="number" step="0.01"/>
                <button @click.prevent = "motherboard.clear(); checkFormMotherboard()">CREATE</button>
            </form>
            <ul class = "no-dots" v-if = "motherboard.error">
                <li v-for = "(error, index) in motherboard.error_list" :key = "index">{{error}}</li>
            </ul>
        </div>

        <div>
            <h2>CREATE COMPONENT</h2>
            <form @change = "component.clear">
                <p>COMPONENT NAME</p>
                <input v-model = "component.name" type="text"/>
                <p>COMPONENT DESCRIPTION</p>
                <input v-model = "component.description" type="text"/>
                <p>COMPONENT TYPE</p>
                <select v-model = "component.type">
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
                <p>COMPONENT PRICE</p>
                <input v-model = "component.price" type="number" step="0.01"/>
                <button @click.prevent = "component.clear(); checkFormComponent()">CREATE</button>
            </form>
            <ul class = "no-dots" v-if = "component.error">
                <li v-for = "(error, index) in component.error_list" :key = "index">{{error}}</li>
            </ul>
        </div>

        <div>
            <h2>CREATE COMPATIBLE</h2>

            <form @change = "compatible.clear">

                <p>MOTHERBOARD</p>
                <select v-model = "compatible.motherboard">
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    <option v-for = "(motherboard_e, index) in resources.motherboard_list" :key = "index" value = "motherboard_e.id">{{motherboard_e.name}}</option>
                </select>

                <p>COMPONENT</p>
                <select v-model = "compatible.component">
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    <option v-for = "(component_e, index) in resources.component_list" :key = "index" value = "component_e.id">{{component_e.name}}</option>
                </select>
                <button @click.prevent = "compatible.clear(); checkFormCompatible()">CREATE</button>
            </form>
            <ul class = "no-dots">
                <li v-for = "(error, index) in compatible.error_list" :key = "index">{{error}}</li>
            </ul>
            <div v-if = "resources.error">
                {{compatible.error_text}}
            </div>
        </div>
    </div>

</template>

<script>
export default {
    data() {
        return {
            motherboard: {
                name: '',
                description: '',
                price: 0,
                error_list: [],
                error: false,
                clear: () => {
                    this.motherboard.error_list = []
                    this.motherboard.error = false
                }
            },
            component: {
                name: '',
                description: '',
                price: 0,
                type: '',
                error_list: [],
                error: false,
                clear: () => {
                    this.component.error_list = []
                    this.component.error = false
                }
            },
            resources: {
                motherboard_list: [],
                component_list: [],
                error: false,
                error_text: '',
            },
            compatible: {
                motherboard: '',
                component: '',
                error: false,
                error_list: [],
                clear: () => {
                    this.compatible.error = false
                    this.compatible.error_list = []
                }
            }
        }
    },
    mounted () {
        fetch('http://127.0.0.1:5000/motherboards', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(JsonResponse => {
            if (JsonResponse['success'] === true){
                this.resources.motherboard_list = JsonResponse['motherboards']
            }
            else {
                this.resources.error_list = JsonResponse['message']
                this.resources.error = true
            }
        })
        .catch(() => {
            this.resources.error_list = 'Something went wrong!'
            this.resources.error = true
        })
        // TODO: get components (must be able to be compatible - generar un search ://)
        fetch('http://127.0.0.1:5000/components', {
            method: 'POST',
            body: JSON.stringify({
                'search': true,
                'components': ['RAM', 'SSD', 'GPU', 'PC Cooling']
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(JsonResponse => {
            console.log(JsonResponse)
            if (JsonResponse['success'] === true){
                this.resources.component_list = JsonResponse['components']
            }
            else {
                console.log("error servidor")

                this.resources.error_list = JsonResponse['message']
                this.resources.error = true
            }
        })
        .catch(() => {
            console.log("error js")
            this.resources.error_list = 'Something went wrong!'
            this.resources.error = true
        })
    },
    methods: {
        checkFormMotherboard () {
            if (this.motherboard.name === ''){
                this.motherboard.error_list.push('Motherboard name is required.')
            }
            if (this.motherboard.description === ''){
                this.motherboard.error_list.push('Motherboard description is required')
            }
            if (this.motherboard.price === 0){
                this.motherboard.error_list.push('Motherboard price cannot de 0')
            }
            else if (this.motherboard.price < 0){
                this.motherboard.error_list.push('Motherboard price cannot be negative')
            }
            if (this.motherboard.error_list.length) {
                this.motherboard.error = true
            }
            if (this.motherboard.error === false) {
                this.createMotherboard()
            }
        },
        createMotherboard () {
            fetch('http://127.0.0.1:5000/motherboards', {
                method: 'POST',
                body: JSON.stringify({
                    'name': this.motherboard.name,
                    'description': this.motherboard.description,
                    'price': this.motherboard.price,
                    'create_by': this.$root.$root.user_info.id
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    console.log('here')
                    // TODO: actualizar las motherboards en create compatible
                    this.motherboard.name = '',
                    this.motherboard.description = '',
                    this.motherboard.price = 0
                    alert("MOTHERBOARD ADDED SUCCESSFULLY")
                }
                else {
                    console.log('error')
                    console.log(JsonResponse)
                }
            }).catch(() => {
                    console.log('error')
            })
        },
        checkFormComponent() {
            if (this.component.name === ''){
                this.component.error_list.push('Component name is required.')
            }
            if (this.component.description === ''){
                this.component.error_list.push('Component description is required')
            }
            if (this.component.type === ''){
                this.component.error_list.push('Component type is required')
            }
            if (this.component.price === 0){
                this.component.error_list.push('Component price cannot de 0')
            }
            else if (this.component.price < 0){
                this.component.error_list.push('Component price cannot be negative')
            }
            if (this.component.error_list.length) {
                this.component.error = true
            }
            if (this.component.error === false) {
                this.createComponent()
            }
        },
        createComponent () {
            fetch('http://127.0.0.1:5000/components', {
                method: 'POST',
                body: JSON.stringify({
                    'name': this.component.name,
                    'description': this.component.description,
                    'price': this.component.price,
                    'type': this.component.type,
                    'create_by': this.$root.$root.user_info.id
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    // TODO: actualizar las motherboards en create compatible
                    this.component.name = '',
                    this.component.description = '',
                    this.component.price = 0
                    this.component.type = '',
                    alert("COMPONENT ADDED SUCCESSFULLY")
                }
                else {
                    console.log('error')
                    console.log(JsonResponse)
                }
            }).catch(() => {
                    console.log('error')
            })
        },
        checkFormCompatible () {
            if (this.compatible.motherboard === "") {
                this.compatible.error_list.push('Motherboard for compatible cannot be empty')
            }
            if (this.compatible.component === "") {
                this.compatible.error_list.push("Component for compatible cannot be empty")
            }
            if (this.compatible.error_list.length) {
                this.compatible.error = true
            }
            if (this.compatible.error === false) {
                this.createCompatible()
            }
        },
        createCompatible () {
            // TODO: crear la compatibilidad
            console.log('something')
        }
    }
}

</script>
