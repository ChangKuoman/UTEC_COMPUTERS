<template>
    <div>
        <div class="contenedor_HOME">
            <div class="Texto_presentacion">
                <form>
                    <p>USERNAME</p>
                    <input v-model = "username" type="text"/>
                    <p>PASSWORD</p>
                    <input v-model = "password" type="password"/>
                    <p>CONFIRM PASSWORD</p>
                    <input v-model = "password_confirm" type="password"/>
                    <button @click.prevent = "register">REGISTER</button>
                </form>
            </div>
        </div>


        <div v-if = "wentWrong">
            Something went wrong!
        </div>
        <FooterComponent/>
    </div>
</template>

<script>
import FooterComponent from '../components/FooterComponent.vue'
export default {
  components: { FooterComponent },
  data () {
    return {
        wentWrong: false,
        username: '',
        password: '',
        password_confirm: ''
    }
  },
  methods: {
    register () {
        fetch('http://127.0.0.1:5000/users', {
            method: 'POST',
            body: JSON.stringify({
                'username': this.username,
                'password': this.password,
                'password_confirm': this.password_confirm
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(JsonResponse => {
            if (JsonResponse['success'] === true) {
                console.log(JsonResponse)
                this.$router.push('/login')
            }
            else {
                console.log(JsonResponse)
            }
        })
        .catch(() => {
            console.log('error')
        })
    }
  }
}
</script>
