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
            Something went wrong!
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            error: false,
            motherboards: [],
            chosen_motherboard: null
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
        .then(JsonReponse => {
            console.log(JsonReponse)
            if (JsonReponse['success'] === true){
                this.motherboards = JsonReponse['motherboards']
            }
            else {
                // TODO: si sale error, que haga error
                this.error = true
            }
            console.log(this.motherboards)
        })
        .catch(() =>
            this.error = true
        )
    },
    methods: {
        chooseMotherboard() {

        }
    }
}
</script>