<template>

    <div>
        <h1>
            WHEN A MOTHERBOARD OR COMPONENT IS DELETED, COMPATIBILITIES AND SIMULATIONS RELATED ARE ALSO REMOVED
        </h1>

        <div>
            <h2>DELETE MOTHERBOARD</h2>
            <form @change = "errors.motherboard.clear">
                <select v-model = "motherboard">
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    <option v-for = "(motherboard, index) in resources.motherboard_list" :key = "index" :value = "motherboard.id">{{motherboard.name}}</option>
                </select>
                <button @click.prevent = "errors.motherboard.clear(); deleteMotherboard()">DELETE</button>
            </form>
            <p :v-show = "errors.motherboard.show">{{errors.motherboard.text}}</p>
        </div>

        <div>
            <h2>DELETE COMPONENT</h2>

            <form @change = "errors.component.clear">
                <select v-model = "component">
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    <option v-for = "(component, index) in resources.component_list" :key = "index" :value = "component.id">{{component.name}}</option>
                </select>
                <button @click.prevent = "errors.component.clear(); deleteComponent()">DELETE</button>
            </form>
            <p :v-show = "errors.component.show">{{errors.component.text}}</p>
        </div>

        <div>
            <h2>DELETE COMPATIBLE</h2>

            <form @change = "errors.compatible.clear">
                <select v-model = "compatible">
                    <option value="" hidden selected>SELECT AN OPTION</option>
                    <option v-for = "(compatible, index) in resources.compatible_list" :key = "index" :value = "compatible.id">
                        Motherboard: {{compatible.id_motherboard}} - Component: {{compatible.id_component}}
                    </option>
                </select>
                <button @click.prevent = "errors.compatible.clear(); deleteCompatible()">DELETE</button>
            </form>
            <p :v-show = "errors.compatible.show">{{errors.compatible.text}}</p>
        </div>

        <ul v-if = "resources.error" class = 'no-dots'>
            {{resources.error_text}}
        </ul>

    </div>
</template>

<script>
export default {
    data () {
        return {
            errors: {
                motherboard: {
                    show: false,
                    text: '',
                    clear: () => {
                        this.errors.motherboard.show = false
                        this.errors.motherboard.text = ''
                    }
                },
                component: {
                    show: false,
                    text: '',
                    clear: () => {
                        this.errors.component.show = false
                        this.errors.component.text = ''
                    }
                },
                compatible: {
                    show: false,
                    text: '',
                    clear: () => {
                        this.errors.compatible.show = false
                        this.errors.compatible.text = ''
                    }
                }
            },
            resources: {
                motherboard_list: [],
                component_list: [],
                compatible_list: [],
                error: false,
                error_text: ''
            },
            motherboard: '',
            component: '',
            compatible: ''
        }
    },
    methods: {
        get_compatibles() {
            fetch('http://127.0.0.1:5000/compatibles', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                console.log(JsonResponse)
                if (JsonResponse['success'] === true){
                    this.resources.compatible_list = Object.values(JsonResponse['compatibles'])
                }
                else {
                    this.resources.error_text = JsonResponse['message']
                    this.resources.error = true
                }
            })
            .catch(() => {
                this.resources.error_text = 'Something went wrong!'
                this.resources.error = true
            })
        },
        deleteMotherboard () {
            if (this.motherboard === '') {
                this.errors.motherboard.error = true
                this.errors.motherboard.text = 'Select a motherboard to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/motherboards/' + this.motherboard, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.motherboard = ''
                        this.resources.motherboard_list = JsonResponse['motherboards']
                        this.get_compatibles()
                        alert("DELETED MOTHERBOARD SUCCESSFULLY")
                    }
                    else {
                        console.log("error backend motherboard delete")
                    }
                })
                .catch(() => {
                    console.log("error js motherboard delete")
                })
            }
        },
        deleteComponent () {
            if (this.component === '') {
                this.errors.component.error = true
                this.errors.component.text = 'Select a component to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/components/' + this.component, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.component = ''
                        this.resources.component_list = JsonResponse['components']
                        this.get_compatibles()
                        alert("DELETED COMPONENT SUCCESSFULLY")
                    }
                    else {
                        console.log("error backend components delete")
                    }
                })
                .catch(() => {
                    console.log("error js components delete")
                })
            }
        },
        deleteCompatible () {
            if (this.compatible === '') {
                this.errors.compatible.error = true
                this.errors.compatible.text = 'Select a compatible to delete'
            }
            else {
                fetch('http://127.0.0.1:5000/compatibles/' + this.compatible, {
                    method: 'DELETE',
                    headers: {
                        'Content-Type': 'application/json'
                    }
                })
                .then(response => response.json())
                .then(JsonResponse => {
                    if (JsonResponse['success'] === true) {
                        this.compatible = ''
                        this.resources.compatible_list = JsonResponse['compatibles']
                        this.get_compatibles()
                        alert("DELETED COMPATIBLES SUCCESSFULLY")
                    }
                    else {
                        console.log("error backend compatible delete")
                    }
                })
                .catch(() => {
                    console.log("error js compatible delete")
                })
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
                this.resources.error_text = JsonResponse['message']
                this.resources.error = true
            }
        })
        .catch(() => {
            this.resources.error_text = 'Something went wrong!'
            this.resources.error = true
        })
        fetch('http://127.0.0.1:5000/components', {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(JsonResponse => {
            console.log(JsonResponse)
            if (JsonResponse['success'] === true){
                this.resources.component_list = Object.values(JsonResponse['components'])
            }
            else {
                this.resources.error_text = JsonResponse['message']
                this.resources.error = true
            }
        })
        .catch(() => {
            this.resources.error_text = 'Something went wrong!'
            this.resources.error = true
        })
        this.get_compatibles()
    }
}
</script>
