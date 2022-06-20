<template>
    <div>
  <div class="contenedor_HOME">
      <div class="contenedor_app">
        <div v-if="first_part">
            <div v-if="!errors.motherboard.show">
                <h1>
                    WELCOME TO THE SIMULATOR, FIRST SELECT A MOTHERBOARD
                </h1>
                <form>
                    <InputRadio
                        class="no-dots"
                        v-model="simulation.motherboard"
                        :objects="lists.motherboard"
                        title="CHOOSE A MOTHERBOARD:"
                    />
                    <button @click.prevent="choose_motherboard">CHOOSE ↪</button>
                </form>
            </div>
            <div v-if="errors.motherboard.show">
                <p>{{errors.motherboard.text}}</p>
                <button @click.prevent="goHome">↩ Home</button>
            </div>
        </div>
        <div v-if="second_part">
            <button @click.prevent="goBack">↩ BACK</button>

                <div>
                    <div v-if="!errors.component.show">
                        <h1>NOW, CHOOSE THE COMPONENTS</h1>
                        <div>
                            <div>
                                <h2>YOUR MOTHERBOARD: {{simulation.motherboard.name}}</h2>
                                <p>MotherBoard Price: S/. {{simulation.motherboard.price.toFixed(2)}}</p>
                            </div>
                            <button @click.prevent="resetProducts">
                                <img class="img-20" src="@/assets/img/button_reset.png" />
                            </button>
                        </div>

                        <form>
                            <h1>COMPONENTS THAT NEED COMPATIBILITY:</h1>
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
                            <h1>COMPONENTS THAT DO NOT NEED COMPATIBILITY:</h1>
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
                                <h2>PERIPHERALS</h2>
                                <ul class="no-dots">
                                    <li v-for="(peripheral, index) in lists.peripheral" :key="index">
                                        <input v-model="simulation.peripheral" type="checkbox" :value="peripheral" />
                                        <label>Name: {{peripheral.name}}</label>
                                        <div>
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
                    <div v-if="errors.component.show">
                        <p>{{errors.component.text}}</p>
                    </div>
                </div>
                <ShoppingCart
                    :total_price="total_price"
                    :total_products="total_products"
                    @onSimulate="simulate"
                />
</div>
</div>
        </div>
    </div>
</template>

<script>
import InputRadio from '@/components/InputRadio.vue'
import ShoppingCart from '@/components/ShoppingCart.vue'

export default {
    components: { InputRadio, ShoppingCart },
    data () {
        return {
            first_part: true,
            second_part: false,
            errors: {
                motherboard: {
                    show: false,
                    text: ''
                },
                component: {
                    show: false,
                    text: ''
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
            fetch('http://127.0.0.1:5000/motherboards', { method: 'GET' })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    this.lists.motherboard = JsonResponse['motherboards']
                }
                else if (JsonResponse['code'] === 404){
                    this.errors.motherboard.text = 'We are sorry, there are no motherboards to show'
                    this.errors.motherboard.show = true
                }
                else {
                    this.errors.motherboard.text = JsonResponse['message']
                    this.errors.motherboard.show = true
                }
            })
            .catch(() => {
                this.error.motherboard.text = 'Something went wrong!'
                this.error.motherboard.show = true
            })
        }
        else {
            this.$router.push('/login')
        }
    },
    computed: {
        total_price: function() {
            return  this.total_products.reduce((accumulator, object) => {
                return accumulator + object.price;
            }, 0);
        },
        total_products: function() {
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
    methods: {
        choose_motherboard () {
            if (this.simulation.motherboard === null) {
                this.error.show = true
                this.error.text = 'You must choose a motherboard to keep going'
            }
            else {
                this.second_part = true
                this.first_part = false
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
                        // Above ones needs compatibility w
                        const arr = Object.values(this.simulation.motherboard.compatibles).map(motherboard => motherboard.id_component)
                        this.lists.ram = components_array.filter(component => component.component_type === "RAM" && arr.includes(component.id))
                        this.lists.ssd = components_array.filter(component => component.component_type === "SSD" && arr.includes(component.id))
                        this.lists.gpu = components_array.filter(component => component.component_type === "GPU" && arr.includes(component.id))
                        this.lists.pc_cooling = components_array.filter(component => component.component_type === "PC Cooling" && arr.includes(component.id))
                    }
                    else {
                        this.errors.component.text = JsonResponse['message']
                        this.errors.component.show = true
                    }
                })
                .catch(() => {
                    this.errors.component.text = 'Something went wrong!'
                    this.errors.component.show = true
                })
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
