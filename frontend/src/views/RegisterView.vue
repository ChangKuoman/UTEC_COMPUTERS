<template>
    <div>
        <div class="contenedor_HOME">
            <div class="Texto_presentacion">
                <form @change = "error.clear">
                    <p>USERNAME</p>
                    <input v-model = "username" type="text"/>
                    <p>PASSWORD</p>
                    <input v-model = "password" type="password"/>
                    <p v-show = "password.length" :style = "password_color"><b>{{password_strength}}</b></p>
                    <p>CONFIRM PASSWORD</p>
                    <input v-model = "password_confirm" type="password"/>
                    <button @click.prevent = "error.clear(); check_register_form()">REGISTER</button>
                </form>
                <ul class = "no-dots" v-if = "error_form">
                    <li v-for = "(error, index) in error_list" :key = "index">{{error}}</li>
                </ul>
                <div v-if = "error">
                    {{errorText}}
                </div>
                <ul class = "no-dots" v-if = "error.show">
                    <li v-for = "(error, index) in error.list" :key = "index">{{error}}</li>
                </ul>
            </div>
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
        error: {
            show: false,
            list: [],
            clear: () => {
                this.error.show = false
                this.error.list = []
            }
        },
        username: '',
        password: '',
        password_confirm: ''
    }
  },
  computed: {
    password_strength: function() {
        const strong = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{8,})/
        const medium2 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{6,})/
        const medium1 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})/
        if (strong.test(this.password)) {
            return 'Strong password'
        }
        if (medium2.test(this.password)) {
            return 'Medium password'
        }
        if (medium1.test(this.password)) {
            return 'Weak password'
        }
        return 'Very weak password'
    },
    password_color: function() {
        if (this.password_strength === 'Strong password') {
            return {color: "#FF0000"}
        }
        if (this.password_strength === 'Medium password') {
            return {color: "#FFA500"}
        }
        if (this.password_strength === 'Weak password') {
            return {color: "#FFCD01"}
        }
        if (this.password_strength === 'Very weak password') {
            return {color: "#008000"}
        }
        return {color: "#000000"}
    }
  },
  methods: {
    check_register_form () {
        if (this.username === '') {
            this.error.list.push('Username cannot be empty')
        }
        if (this.password === '') {
            this.error.list.push('Password cannot be empty')
        }
        else if (this.password !== this.password_confirm) {
            this.error.list.push('Passwords do not match')
        }
        else if (this.check_difficulty() === false) {
            this.error.list.push('Password is too weak: it needs a digit, be mixed case and a length of 6 or more')
        }
        if (this.error.list.length) {
            this.error.show = true
        }
        if (this.error.show === false) {
            this.register()
        }
    },
    check_difficulty() {
        const re = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,-_+&$#@()*"':;!?])/
        return re.test(this.password)
    },
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
                alert('Successful registration')
                this.$router.push('/login')
            }
            else {
                this.error.list.push(JsonResponse['message'])
                this.error.show = true
            }
        })
        .catch(() => {
            this.error.list.push('Something went wrong!')
            this.error.show = true
        })
    }
  }
}
</script>
