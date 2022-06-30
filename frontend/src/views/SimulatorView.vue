<template>
    <div>
        <div class="contenedor_HOME">
            <div class="contenedor_app">
                <div v-if = "first_part">
                    <div class="SIM_1">
                        <h1>
                            WELCOME TO THE SIMULATOR
                        </h1>
                    </div>

                    <div class="SIM_2">
                        <h2>FIRST SELECT A MOTHERBOARD</h2>
                        <p>CHOOSE A MOTHERBOARD:</p>

                        <form class="motherB" @change = "error.clear">

                            <ul class="no-dots">
                                <li v-for = "(motherboard, index) in lists.motherboard" :key = "index">
                                    <div class="description_name">
                                        <input v-model = "simulation.motherboard" type="radio" :value = "motherboard" />
                                        <label for = "motherboard">{{motherboard.name}}</label>
                                    </div>
                                    <div class="description_prod">
                                        <p><slan class="weight600">Description:</slan> {{motherboard.description}}</p>
                                        <p><slan class="weight600">Price:</slan> S/. {{motherboard.price.toFixed(2)}}</p>
                                    </div>
                                </li>
                            </ul>
                        </form>
                        <button class="buttom1" @click.prevent = "choose_motherboard">CHOOSE ↪</button>
                    </div>
                </div>
                <div v-if = "second_part">
                    <div class="SIM_3">
                        <button class="buttom1" @click.prevent = "goBack">
                            ↩ BACK
                        </button>
                        <button class="buttom2" @click.prevent = "resetProducts">
                            <img class = "img-20" src="@/assets/img/button_reset.png" />
                        </button>
                    </div>
                    <div class="SIM_2">
                        <h2 class="SIM_4">
                            NOW, CHOOSE THE COMPONENTS
                        </h2>
                        <div>
                            <div>
                                <div>
                                    <h3>YOUR MOTHERBOARD:  {{simulation.motherboard.name}}</h3>
                                    <p>MotherBoard Price:  S/. {{simulation.motherboard.price.toFixed(2)}}</p>
                                </div>
                            </div>
                            <form class="Component">
                                    <h3>
                                        COMPONENTS THAT NEED COMPATIBILITY:
                                    </h3>

                                    <div>
                                        <h4>RAM</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(ram, index) in lists.ram" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.ram" type = "radio" :value = "ram" />
                                                    <label for = "ram">Name: {{ram.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{ram.price.toFixed(2)}}</p>
                                                    <p>Description: {{ram.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h4>SSD</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(ssd, index) in lists.ssd" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.ssd" type = "radio" :value = "ssd" />
                                                    <label for = "ssd">Name: {{ssd.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{ssd.price.toFixed(2)}}</p>
                                                    <p>Description: {{ssd.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h4>GPU</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(gpu, index) in lists.gpu" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.gpu" type = "radio" :value = "gpu" />
                                                    <label for = "gpu">Name: {{gpu.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{gpu.price.toFixed(2)}}</p>
                                                    <p>Description: {{gpu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h4>PC Cooling</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(pc_cooling, index) in lists.pc_cooling" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.pc_cooling" type = "radio" :value = "pc_cooling" />
                                                    <label for = "pc_cooling">Name: {{pc_cooling.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{pc_cooling.price.toFixed(2)}}</p>
                                                    <p>Description: {{pc_cooling.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <h3>COMPONENTS THAT DO NOT NEED COMPATIBILITY: </h3>
                                    <div>
                                        <h4>HDD</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(hdd, index) in lists.hdd" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.hdd" type = "radio" :value = "hdd" />
                                                    <label for = "hdd">Name: {{hdd.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{hdd.price.toFixed(2)}}</p>
                                                    <p>Description: {{hdd.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h4>CPU</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(cpu, index) in lists.cpu" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.cpu" type = "radio" :value = "cpu" />
                                                    <label for = "cpu">Name: {{cpu.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{cpu.price.toFixed(2)}}</p>
                                                    <p>Description: {{cpu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <div>
                                        <h4>PSU</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(psu, index) in lists.psu" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.psu" type = "radio" :value = "psu" />
                                                    <label for = "psu">Name: {{psu.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{psu.price.toFixed(2)}}</p>
                                                    <p>Description: {{psu.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>

                                    <h3>PERIPHERALS</h3>

                                    <div>
                                        <h4>Peripheral</h4>
                                        <ul class="no-dots">
                                            <li v-for = "(peripheral, index) in lists.peripheral" :key = "index">
                                                <div class="description_name">
                                                    <input v-model = "simulation.peripheral" type="checkbox" :value = "peripheral" />
                                                    <label for = "peripheral">Name: {{peripheral.name}}</label>
                                                </div>
                                                <div class="description_prod">
                                                    <p>Price: S/. {{peripheral.price.toFixed(2)}}</p>
                                                    <p>Description: {{peripheral.description}}</p>
                                                </div>
                                            </li>
                                        </ul>
                                    </div>
                            </form>
                        </div>
                        <div>
                            <div class="shop">
                                <div class="tittle_shop">
                                    <h2>SHOPPING CART  <img class = "img-20" src="@/assets/img/shopping_cart.png" alt="Shopping Cart">
                                    </h2>
                                </div>
                                <div class="list_shop">
                                    <ul class = "no-dots">
                                        <li v-for = "(product, index) in total_products" :key = "index"><slan class="weight600">{{product.name}}: </slan> S/.{{product.price.toFixed(2)}}</li>
                                    </ul>
                                </div>
                                <p><b>TOTAL PRICE: S/. {{total_price.toFixed(2)}}</b></p>
                                <button class="buttom1" @click.prevent = "simulate">SIMULATE!</button>
                            </div>
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

    .SIM_1{
        min-width: 700px;
        width: 95%;
        padding-left: 2.5%;
        padding-right: 2.5%;

        height: 18%;
        padding-top: 1%;
        padding-bottom:1%;
        min-height: 100px;

        text-align: center;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    .SIM_2{
        min-width: 700px;
        width: 95%;
        padding-left: 2.5%;
        padding-right: 2.5%;

        height: 78%;
        padding-top: 1%;
        padding-bottom:1%;
        min-height: 700px;

        display:flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    .SIM_3{
        min-width: 700px;
        width: 95%;
        padding-left: 2.5%;
        padding-right: 2.5%;

        height: 2%;
        padding-top: 1%;
        padding-bottom:1%;
        min-height: 30px;

        display:flex;
        align-items: center;
        align-content: center;
        justify-content: flex-start;
    }
    .SIM_4{
        min-width: 700px;
        width: 95%;
        padding-left: 2.5%;
        padding-right: 2.5%;
        margin: 0;

        height: 2%;
        padding-top: 1%;
        padding-bottom:1%;
        min-height: 50px;

        display:flex;
        justify-content: center;
        align-items: center;
    }
    .motherB{
        width: 100%;
        height: 600px;

        overflow: scroll;
    }
    .Component{
        min-width: 700px;
        width: 100%;
        height: 450px;

        overflow: scroll;
    }
    .list_shop{
        width: 300px;
        height: 70px;
        padding: 0;

        overflow: scroll;
    }
    .motherB::-webkit-scrollbar {
        width: 7px;
    }
    .motherB::-webkit-scrollbar-thumb {
        background: rgb(47, 137, 172);
        border-radius: 5px 5px;
    }
    .Component::-webkit-scrollbar{
        width: 7px;
    }
    .Component::-webkit-scrollbar-thumb {
        background: rgb(47, 137, 172);
        border-radius: 5px 5px;
    }
    .list_shop::-webkit-scrollbar {
        width: 4px;
    }
    .list_shop::-webkit-scrollbar-thumb {
        background: #333;
        border-radius: 5px 5px;
    }
    .shop{
        min-width:400px;
        padding: 10px;
        border-radius: 7px;
        background-color: rgb(95, 189, 226);
        color: white;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .description_name{
        width: auto;
        padding-top: 9px;
        padding-bottom: 9px;
    }
    .description_prod{
        width: auto;
        padding: 15px;
        margin-left: 18px;
        border-radius: 10px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .weight600{
        font-weight: 600;
    }
    .tittle_shop{
        width: 300px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .buttom1{
        padding: 5px;
        font-size: 15px;
        margin-left: 10px;
        margin-right:10px;

        border-radius: 5px;
        cursor: pointer;
        border: none;
        color: white;
        background: #333;
    }
    .buttom2{
        font-size: 15px;
        margin-left: 10px;
        margin-right:10px;

        background: none;
        border: none;
        cursor: pointer;
    }
</style>
