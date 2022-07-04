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

                    <div class="SIM_2" v-if="!errors.motherboard">
                        <h2>FIRST SELECT A MOTHERBOARD</h2>

                        <form class="motherB">
                            <InputRadio
                                class="no-dots"
                                v-model="simulation.motherboard"
                                :objects="lists.motherboard"
                                title="CHOOSE A MOTHERBOARD:"
                            />
                            <button class="buttom1" @click.prevent="choose_motherboard">CHOOSE ↪</button>
                        </form>
                    </div>
                    <div v-if="errors.motherboard">
                        <p>{{errors.motherboard}}</p>
                        <button @click.prevent="goHome">↩ Home</button>
                    </div>
                </div>

                <div v-if = "second_part">
                    <div class="SIM_3">
                        <button class="buttom1" @click.prevent="goBack">
                            ↩ BACK
                        </button>
                        <button class="buttom2" @click.prevent="resetProducts">
                            <img class = "img-20" src="@/assets/img/button_reset.png" />
                        </button>
                    </div>
                    <div class="SIM_2" v-if="!errors.component">
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

                                <InputRadio
                                    v-if="lists.ram.length"
                                    class="no-dots"
                                    v-model="simulation.ram"
                                    :objects="lists.ram"
                                    title="RAM"
                                />
                                <InputRadio
                                    v-if="lists.ssd.length"
                                    class="no-dots"
                                    v-model="simulation.ssd"
                                    :objects="lists.ssd"
                                    title="SSD"
                                />
                                <InputRadio
                                    v-if="lists.gpu.length"
                                    class="no-dots"
                                    v-model="simulation.gpu"
                                    :objects="lists.gpu"
                                    title="GPU"
                                />
                                <InputRadio
                                    v-if="lists.pc_cooling.length"
                                    class="no-dots"
                                    v-model="simulation.pc_cooling"
                                    :objects="lists.pc_cooling"
                                    title="PC COOLING"
                                />

                                <div v-if="!lists.ram.length && !lists.ssd.length && !lists.gpu.length && !lists.pc_cooling.length">
                                    We are sorry, there are no components here
                                </div>

                                <h3>COMPONENTS THAT DO NOT NEED COMPATIBILITY: </h3>
                                <InputRadio
                                    v-if="lists.hdd.length"
                                    class="no-dots"
                                    v-model="simulation.hdd"
                                    :objects="lists.hdd"
                                    title="HDD"
                                />
                                <InputRadio
                                    v-if="lists.cpu.length"
                                    class="no-dots"
                                    v-model="simulation.cpu"
                                    :objects="lists.cpu"
                                    title="CPU"
                                />
                                <InputRadio
                                    v-if="lists.psu.length"
                                    class="no-dots"
                                    v-model="simulation.psu"
                                    :objects="lists.psu"
                                    title="PSU"
                                />
                                <div v-if="lists.peripheral.length">
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
                                <div v-if="!lists.hdd.length && !lists.cpu.length && !lists.psu.length && !lists.peripheral.length">
                                    We are sorry, there are no components here
                                </div>
                            </form>
                        </div>
                        <ShoppingCart
                            :total_price="total_price"
                            :total_products="total_products"
                            @onSimulate="simulate"
                        />
                    </div>
                    <div v-if="errors.component">
                        <p>{{errors.component}}</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import {host} from '@/host.js';
import InputRadio from '@/components/InputRadio.vue'
import ShoppingCart from '@/components/ShoppingCart.vue'

export default {
    components: { InputRadio, ShoppingCart },
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
            errors: {
                motherboard: '',
                component: ''
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
            fetch(host + '/users', {
                method: 'POST',
                body: JSON.stringify({
                    'token': localStorage.getItem('token'),
                    'check_token': true
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true && JsonResponse['is_valid'] === true) {
                    this.getMotherboards()
                }
                else {
                    this.$router.push('/login')
                }
            })
            .catch(() => {
                this.$router.push('/login')
            })
        }
        else {
            this.$router.push('/login')
        }
    },
    methods: {
        choose_motherboard () {
            if (this.simulation.motherboard === null) {
                alert('You must choose a motherboard to keep going')
            }
            else {
                this.second_part = true
                this.first_part = false
                this.getComponents()
            }
        },
        goBack () {
            this.first_part = true,
            this.second_part = false
        },
        goHome () {
            this.$router.push('/')
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
            fetch(host + '/simulations', {
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
                if (JsonResponse['success'] === true){
                    this.$router.push("/simulation/" + JsonResponse['created_id'])
                }
                else {
                    alert(JsonResponse['message'])
                    this.$router.push('/')
                }
            })
            .catch(() => {
                alert('Something went wrong!')
                this.$router.push('/')
            })
        },
        getMotherboards () {
            fetch(host + '/motherboards', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.lists.motherboard = JsonResponse['motherboards']
                }
                else if (JsonResponse['code'] === 404){
                    this.errors.motherboard = 'We are sorry, there are no motherboards to show'
                }
                else {
                    this.errors.motherboard = JsonResponse['message']
                }
            })
            .catch(() => {
                this.error.motherboard.text = 'Something went wrong!'
            })
        },
        getComponents () {
            fetch(host + '/components', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    const components_array = Object.values(JsonResponse['components'])
                    this.lists.hdd = components_array.filter(component => component.component_type === "HDD")
                    this.lists.cpu = components_array.filter(component => component.component_type === "CPU")
                    this.lists.psu = components_array.filter(component => component.component_type === "PSU")
                    this.lists.peripheral = components_array.filter(component => component.component_type === "Peripheral")
                    // Above ones needs compatibility w
                    const arr = Object.values(this.simulation.motherboard.compatibles).map(motherboard => motherboard.id_component)
                    this.lists.ram = components_array.filter(component => component.component_type === "RAM" && arr.includes(component.id))
                    this.lists.ssd = components_array.filter(component => component.component_type === "SSD" && arr.includes(component.id))
                    this.lists.gpu = components_array.filter(component => component.component_type === "GPU" && arr.includes(component.id))
                    this.lists.pc_cooling = components_array.filter(component => component.component_type === "PC Cooling" && arr.includes(component.id))
                }
                else {
                    this.errors.component = JsonResponse['message']
                }
            })
            .catch(() => {
                this.errors.component = 'Something went wrong!'
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
