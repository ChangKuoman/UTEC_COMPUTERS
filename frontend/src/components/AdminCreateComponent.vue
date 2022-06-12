<template>
    <div>
        <h1>
            WHEN CREATING A PRODUCT, ALL FIELDS MUST BE FILLED
        </h1>

        <div>
            <h2>CREATE MOTHERBOARD</h2>
            <form>
                <p>MOTHERBOARD NAME</p>
                <input v-model = "motherboardName" type="text"/>
                <p>MOTHERBOARD DESCRIPTION</p>
                <input v-model = "motherboardDescription" type="text"/>
                <p>MOTHERBOARD PRICE</p>
                <input v-model = "motherboardPrice" type="number" step="0.01"/>
                <button @click.prevent = "createMotherboard">CREATE</button>
            </form>
        </div>

        <div>
            <h2>CREATE COMPONENT</h2>
            <form>
                <p>COMPONENT NAME</p>
                <input v-model = "componentName" type="text"/>
                <p>COMPONENT DESCRIPTION</p>
                <input v-model = "componentDescription" type="text"/>
                <p>COMPONENT TYPE</p>
                <select v-model = "componentType">
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
                <input v-model = "componentPrice" type="number" step="0.01"/>
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
            motherboardName: '',
            motherboardDescription: '',
            motherboardPrice: 0,
            componentName: '',
            componentDescription: '',
            componentType: '',
            componentPrice: 0
        }
    },
    methods: {
        // TODO: create_by
        createMotherboard () {
            fetch('http://127.0.0.1:5000/motherboards', {
                method: 'POST',
                body: JSON.stringify({
                    'name': this.motherboardName,
                    'description': this.motherboardDescription,
                    'price': this.motherboardPrice,
                    'create_by': 1
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    // TODO: actualizar las motherboards en create compatible
                    this.motherboardName = '',
                    this.motherboardDescription = '',
                    this.motherboardPrice = 0
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
            console.log(this.componentName, this.componentDescription, this.componentType, this.componentPrice)
            fetch('http://127.0.0.1:5000/components', {
                method: 'POST',
                body: JSON.stringify({
                    'name': this.componentName,
                    'description': this.componentDescription,
                    'price': this.componentPrice,
                    'type': this.componentType,
                    'create_by': 1
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    // TODO: actualizar las motherboards en create compatible
                    this.componentName = '',
                    this.componentDescription = '',
                    this.componentPrice = 0
                    this.componentType = '',
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
