<template>
    <div>
        <h1>
            WELCOME TO THE SIMULATOR, FIRST SELECT A MOTHERBOARD
        </h1>
        <div>
            <p>CHOOSE A MOTHERBOARD:</p>
            <form>

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
        <div v-if = "error">
            {{errorText}}
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            error: false,
            errorText: '',
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
                    this.errorText = JsonResponse['message']
                    this.error = true
                }
            })
            .catch(() => {
                this.errorText = 'Something went wrong!'
                this.error = true
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