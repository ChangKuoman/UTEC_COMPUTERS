<template>
    <div>
        <div class="contenedor_HOME">
            <div class="contenedor_app">
                <div v-if = "first_part">
                    <div>
                         <h1>
                            WELCOME TO THE SIMULATOR, FIRST SELECT A MOTHERBOARD
                        </h1>
                    </div>

                   
                    <div>
                        <p>CHOOSE A MOTHERBOARD:</p>
                        <form @change = "error.clear">

                            <ul class="no-dots">
                                <li v-for = "(motherboard, index) in lists.motherboard" :key = "index">
                                    <input v-model = "simulation.motherboard" type="radio" :value = "motherboard" />
                                    <label for = "motherboard">{{motherboard.name}}</label>
                                    <div>
                                        <p>Description: {{motherboard.description}}</p>
                                        <p>Price: S/. {{motherboard.price.toFixed(2)}}</p>
                                    </div>
                                </li>
                            </ul>
                            <button @click.prevent = "choose_motherboard">CHOOSE ↪</button>

                        </form>
                    </div>
                </div>
                <div v-if = "second_part">
                    <button @click.prevent = "goBack">
                        ↩ BACK
                    </button>

                        <div>
                            <h1>
                                NOW, CHOOSE THE COMPONENTS
                            </h1>

                            <div>
                                <div>
                                    <div>
                                        <h2>YOUR MOTHERBOARD: {{simulation.motherboard.name}}</h2>
                                        <p>MotherBoard Price: S/. {{simulation.motherboard.price.toFixed(2)}}</p>
                                    </div>

                                    <button @click.prevent = "resetProducts">
                                        <img class = "img-20" src="@/assets/img/button_reset.png" />
                                    </button>
                                </div>

                                <form>
                                    <h1>
                                        COMPONENTS THAT NEED COMPATIBILITY:
                                    </h1>

                                    <div>
                                        <h2>RAM</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(ram, index) in lists.ram" :key = "index">
                                                <input v-model = "simulation.ram" type = "radio" :value = "ram" />
                                                <label for = "ram">Name: {{ram.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{ram.price.toFixed(2)}}</p>
                                                    <p>Description: {{ram.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h2>SSD</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(ssd, index) in lists.ssd" :key = "index">
                                                <input v-model = "simulation.ssd" type = "radio" :value = "ssd" />
                                                <label for = "ssd">Name: {{ssd.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{ssd.price.toFixed(2)}}</p>
                                                    <p>Description: {{ssd.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h2>GPU</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(gpu, index) in lists.gpu" :key = "index">
                                                <input v-model = "simulation.gpu" type = "radio" :value = "gpu" />
                                                <label for = "gpu">Name: {{gpu.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{gpu.price.toFixed(2)}}</p>
                                                    <p>Description: {{gpu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h2>PC Cooling</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(pc_cooling, index) in lists.pc_cooling" :key = "index">
                                                <input v-model = "simulation.pc_cooling" type = "radio" :value = "pc_cooling" />
                                                <label for = "pc_cooling">Name: {{pc_cooling.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{pc_cooling.price.toFixed(2)}}</p>
                                                    <p>Description: {{pc_cooling.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <h1>COMPONENTS THAT DO NOT NEED COMPATIBILITY: </h1>
                                    <div>
                                        <h2>HDD</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(hdd, index) in lists.hdd" :key = "index">
                                                <input v-model = "simulation.hdd" type = "radio" :value = "hdd" />
                                                <label for = "hdd">Name: {{hdd.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{hdd.price.toFixed(2)}}</p>
                                                    <p>Description: {{hdd.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h2>CPU</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(cpu, index) in lists.cpu" :key = "index">
                                                <input v-model = "simulation.cpu" type = "radio" :value = "cpu" />
                                                <label for = "cpu">Name: {{cpu.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{cpu.price.toFixed(2)}}</p>
                                                    <p>Description: {{cpu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h2>PSU</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(psu, index) in lists.psu" :key = "index">
                                                <input v-model = "simulation.psu" type = "radio" :value = "psu" />
                                                <label for = "psu">Name: {{psu.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{psu.price.toFixed(2)}}</p>
                                                    <p>Description: {{psu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <h1>PERIPHERALS</h1>

                                    <div>
                                        <h2>Peripheral</h2>
                                        <ul class="no-dots">
                                            <li v-for = "(peripheral, index) in lists.peripheral" :key = "index">
                                                <input v-model = "simulation.peripheral" type="checkbox" :value = "peripheral" />
                                                <label for = "peripheral">Name: {{peripheral.name}}</label>
                                                <div>
                                                    <p>Price: S/. {{peripheral.price.toFixed(2)}}</p>
                                                    <p>Description: {{peripheral.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                                </form>

                            </div>
                        </div>

                        <div>
                            <div>
                                <div>
                                    <h2>SHOPPING CART</h2>
                                    <img class = "img-20" src="@/assets/img/shopping_cart.png" alt="Shopping Cart">
                                </div>

                                <ul class = "no-dots">
                                    <li v-for = "(product, index) in total_products" :key = "index">{{product.name}} S/.{{product.price.toFixed(2)}}</li>
                                </ul>
                                <p><b>TOTAL PRICE: S/. {{total_price.toFixed(2)}}</b></p>
                                <button @click.prevent = "simulate">SIMULATE!</button>

                            </div>
                        </div>

                </div>
                <div v-if = "error.show">
                        {{error.text}}
                </div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    computed: {
        total_price: function() {
            return  this.total_products.reduce((accumulator, object) => {
                return accumulator + object.price;
            }, 0);
        },
        total_products: function () {
            return [
                this.simulation.motherboard,
                this.simulation.ram,
                this.simulation.ssd,
                this.simulation.gpu,
                this.simulation.pc_cooling,
                this.simulation.hdd,
                this.simulation.cpu,
                this.simulation.psu,
                ...this.simulation.peripheral
            ].filter(product => product !== null)
        }
    },
    data () {
        return {
            first_part: true,
            second_part: false,
            error: {
                show: false,
                text: '',
                clear: () => {
                    this.error.show = false,
                    this.error.text = ''
                }
            },
            lists: {
                motherboard: [],
                ram: [],
                ssd: [],
                gpu: [],
                pc_cooling: [],
                hdd: [],
                cpu: [],
                psu: [],
                peripheral: []
            },
            simulation: {
                motherboard: null,
                ram: null,
                ssd: null,
                gpu: null,
                pc_cooling: null,
                hdd: null,
                cpu: null,
                psu: null,
                peripheral: []
            },
        }
    },
    mounted () {
        if (localStorage.getItem('token')){
            fetch('http://127.0.0.1:5000/motherboards', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.lists.motherboard = JsonResponse['motherboards']
                }
                else {
                    this.error.text = JsonResponse['message']
                    this.error.show = true
                }
            })
            .catch(() => {
                this.error.text = 'Something went wrong!'
                this.error.show = true
            })
            fetch('http://127.0.0.1:5000/components', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    const components_array = Object.values(JsonResponse['components'])
                    this.lists.hdd = components_array.filter(component => component.component_type === "HDD")
                    this.lists.cpu = components_array.filter(component => component.component_type === "CPU")
                    this.lists.psu = components_array.filter(component => component.component_type === "PSU")
                    this.lists.peripheral = components_array.filter(component => component.component_type === "Peripheral")
                    // TODO: these need compatibility w
                    this.lists.ram = components_array.filter(component => component.component_type === "RAM")
                    this.lists.ssd = components_array.filter(component => component.component_type === "SSD")
                    this.lists.gpu = components_array.filter(component => component.component_type === "GPU")
                    this.lists.pc_cooling = components_array.filter(component => component.component_type === "PC Cooling")
                }
                else {
                    console.log('error back')
                    this.error.text = JsonResponse['message']
                    this.error.show = true
                }
            })
            .catch(() => {
                console.log('error js')
                this.error.text = 'Something went wrong!'
                this.error.show = true
            })
        }
        else {
            this.$router.push('/login')
        }
    },
    methods: {
        choose_motherboard () {
            if (this.simulation.motherboard === null) {
                this.error.show = true
                this.error.text = 'You must choose a motherboard to keep going'
            }
            else {
                this.second_part = true
                this.first_part = false
            }
        },
        goBack () {
            this.first_part = true,
            this.second_part = false
        },
        resetProducts () {
            this.simulation.ram = null,
            this.simulation.ssd = null,
            this.simulation.gpu = null,
            this.simulation.pc_cooling = null,
            this.simulation.hdd = null,
            this.simulation.cpu = null,
            this.simulation.psu = null,
            this.simulation.peripheral = []
        },
        simulate () {
            // TODO: crear la simulacion, redirigir a simulation
            console.log("falta redirigir a simulation")

            fetch('http://127.0.0.1:5000/simulations', {
                method: 'POST',
                body: JSON.stringify({
                    'id_motherboard': this.simulation.motherboard.id,
                    'total_price': this.total_price,
                    'components_id': this.total_products.filter(product => product.component_type !== undefined).map((product) => {
                        return product.id
                    }),
                    'create_by': this.$root.user_info.id
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                console.log(JsonResponse)
                if (JsonResponse['success'] === true){
                    console.log(JsonResponse['simulations'])
                    console.log('success')
                    this.$router.push("/simulation/" + JsonResponse['created_id'])
                }
                else {
                    console.log('back error')
                }
            })
            .catch(() => {
                console.log('js error')
            })
        }
    }
}
</script>

<style scoped>
    .img-20 {
        width: 20px;
        height: 20px;
    }
</style>
