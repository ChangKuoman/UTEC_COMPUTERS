<template>
    <div>
        <h1>
            WELCOME TO THE SIMULATOR, FIRST SELECT A MOTHERBOARD
        </h1>
        <div>
            <p>CHOOSE A MOTHERBOARD:</p>
            <form @change = "error.clear">

                <ul class="no-dots">
                    <li v-for = "(motherboard, index) in motherboards" :key="index">
                        <input v-model = "chosen_motherboard" type="radio" :value = "motherboard.id" />
                        <label for=motherboard.id>{{motherboard.name}}</label>
                        <div>
                            <p>Description: {{motherboard.description}}</p>
                            <p>Price: {{motherboard.price}}</p>
                        </div>
                    </li>
                </ul>

                <button @click.prevent = "choseMotherboard">CHOOSE ↪</button>
            </form>
        </div>
        <div v-if = "error.text">
            {{error.text}}
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            error: {
                show: false,
                text: '',
                clear: () => {
                    this.error.show = false,
                    this.error.text = ''
                }
            },
            motherboards: [],
            chosen_motherboard: null
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
                    this.motherboards = JsonResponse['motherboards']
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
        }
        else {
            this.$router.push('/login')
        }
    },
    methods: {
        chooseMotherboard() {
            // TODO
            console.log('missing functionality here xd')
        }
    }
}
</script>