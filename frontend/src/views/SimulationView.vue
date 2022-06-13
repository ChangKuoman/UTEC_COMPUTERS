<template>
    <div>
        <p>
            YOUR SIMULATION HAS ENDED. YOUR BUILT PC WOULD BE:
        </p>

        <div v-if = "simulation">
            <img src="@/assets/img/cat_pc.jpg">

            <div>
                <div>
                    <p>
                        {{simulation.motherboard.name}}
                    </p>
                    <p>
                        S/. {{simulation.motherboard.price.toFixed(2)}}
                    </p>
                </div>

                <div v-for = "(component, index) in simulation.components" :key = "index">
                    <p>
                        {{component.name}}
                    </p>
                    <p>
                        S/. {{component.price.toFixed(2)}}
                    </p>
                </div>

            </div>
            <div>
                <div>
                    TOTAL PRICE:
                </div>
                <div>
                    S/. {{simulation.total_price.toFixed(2)}}
                </div>
            </div>
            <div v-if = "error.show">
                {{error.text}}
            </div>
        </div>
        <button @click.prevent = "goBack">
            ↩ GO HOME
        </button>
    </div>
</template>

<script>
export default {
    props: {
        id: {
            type: Number,
            required: true
        }
    },
    data () {
        return {
            simulation: null,
            error: {
                show: false,
                text: ''
            }
        }
    },
    mounted () {
        if (localStorage.getItem('token')) {
            fetch('http://127.0.0.1:5000/simulations/' + this.id, {
                method: "GET",
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true){
                    if (JsonResponse['simulation']['create_by'] !== this.$root.user_info.id) {
                        this.$router.push("/")
                    }
                    else {
                        this.simulation = JsonResponse['simulation']
                        console.log(this.simulation)
                    }
                }
                else {
                    this.error.show = true
                    this.error.text = JsonResponse['message']
                }
            })
            .catch(() => {
                this.error.show = true
                this.error.text = 'Something went wrong!'
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
