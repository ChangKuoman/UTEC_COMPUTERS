<template>
    <div>
        <div v-if="simulation">
            <h2>YOUR BUILT PC WOULD BE:</h2>
            <img src="@/assets/img/cat_pc.jpg">
            <div>
                <ProductSimulation
                    :product="simulation.motherboard"
                />
                <ProductSimulation
                    v-for="(component, index) in simulation.components" :key="index"
                    :product="component"
                />
            </div>
            <div>
                <p>
                    TOTAL PRICE:
                </p>
                <p>
                    S/. {{simulation.total_price.toFixed(2)}}
                </p>
            </div>
        </div>
        <button @click.prevent = "goBack">
            ↩ GO HOME
        </button>
    </div>
</template>

<script>
import ProductSimulation from '@/components/ProductSimulation.vue'

export default {
    components: { ProductSimulation },
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data () {
        return {
            simulation: null
        }
    },
    mounted () {
        if (localStorage.getItem('token')) {
            fetch('http://127.0.0.1:5000/simulations/' + this.id, { method: "GET" })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    if (JsonResponse['simulation']['create_by'] !== this.$root.user_info.id) {
                        this.$router.push("/")
                    }
                    else {
                        this.simulation = JsonResponse['simulation']
                    }
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
        else {
            this.$router.push('/login')
        }
    },
    methods: {
        goBack() {
            this.$router.push('/')
        }
    }
}
</script>
