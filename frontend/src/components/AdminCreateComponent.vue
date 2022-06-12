<template>
    <div>
        <h1>
            WHEN CREATING A PRODUCT, ALL FIELDS MUST BE FILLED
        </h1>

        <div>
            <h2>CREATE MOTHERBOARD</h2>
            <form @change = "clear">
                <p>MOTHERBOARD NAME</p>
                <input v-model = "motherboard.name" type="text"/>
                <p>MOTHERBOARD DESCRIPTION</p>
                <input v-model = "motherboard.description" type="text"/>
                <p>MOTHERBOARD PRICE</p>
                <input v-model = "motherboard.price" type="number" step="0.01"/>
                <button @click.prevent = "checkFormMotherboard">CREATE</button>
            </form>
            <ul class = "no-dots" v-if = "motherboard.error">
                <li v-for = "(error, index) in motherboard.errors_list" :key = "index">{{error}}</li>
            </ul>
        </div>

        <div>
            <h2>CREATE COMPONENT</h2>
            <form>
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
                <button @click.prevent = "createComponent">CREATE</button>
            </form>
        </div>

        <div>
            <h2>CREATE COMPATIBLE</h2>

            <form>
                <!--
                <p>MOTHERBOARD</p>
                <select>
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    {% for motherboard in motherboards %}
                    <option value={{motherboard.id}}>{{motherboard.name}}</option>
                    {% endfor %}
                </select>

                <p>COMPONENT</p>
                <select>
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    {% for component in components %}
                    <option value={{component.id}}>{{component.name}}</option>
                    {% endfor %}
                </select>
                <button>CREATE</button>
                -->
            </form>
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
                errors_list: [],
                error: false
            },
            component: {
                name: '',
                description: '',
                price: 0,
                type: ''
            }
        }
    },
    methods: {
        checkFormMotherboard () {
            this.clear()
            if (this.motherboard.name === ''){
                this.motherboard.errors_list.push('Motherboard name is required.')
            }
            if (this.motherboard.description === ''){
                this.motherboard.errors_list.push('Motherboard description is required')
            }
            if (this.motherboard.price === 0){
                this.motherboard.errors_list.push('Motherboard price cannot de 0')
            }
            else if (this.motherboard.price < 0){
                this.motherboard.errors_list.push('Motherboard price cannot be negative')
            }
            if (this.motherboard.errors_list.length) {
                this.motherboard.error = true
            }
            console.log(this.motherboard.errors_list)
            if (this.motherboard.error === false) {
                this.createMotherboard()
            }
        },
        clear () {
            this.motherboard.errors_list = []
            this.error = false
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
        }
    }
}

</script>
