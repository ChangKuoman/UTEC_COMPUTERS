<template>
    <div>
        <form @change = "clear">
            <p>USERNAME</p>
            <input v-model = "username" type="text"/>
            <p>PASSWORD</p>
            <input v-model = "password" type="password"/>
            <p>CONFIRM PASSWORD</p>
            <input v-model = "password_confirm" type="password"/>
            <button @click.prevent = "check_register_form">REGISTER</button>
        </form>
        <ul class = "no-dots" v-if = "error_form">
            <li v-for = "(error, index) in error_list" :key = "index">{{error}}</li>
        </ul>

        <div v-if = "error">
            {{errorText}}
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
        error_form: false,
        error_list: [],
        error: false,
        errorText: '',
        username: '',
        password: '',
        password_confirm: ''
    }
  },
  methods: {
    check_register_form () {
        this.clear()
        if (this.username === '') {
            this.error_list.push('Username cannot be empty')
        }
        if (this.password === '') {
            this.error_list.push('Password cannot be empty')
        }
        else if (this.password !== this.password_confirm) {
            this.error_list.push('Passwords do not match')
        }
        else if (this.check_difficulty() === false) {
            this.error_list.push('Password is too weak: it needs a digit, be mixed case and a length of 6 or more')
        }
        if (this.error_list.length) {
            this.error_form = true
        }
        if (this.error_form === false) {
            this.register()
        }
    },
    check_difficulty() {
        console.log('here')
        let mayusc = 0
        let minusc = 0
        let digit = 0
        let length = this.password.length
        for (let letter of this.password) {
            if (! isNaN(letter)) {
                digit += 1
            }
            else if (letter === letter.toUpperCase()) {
                mayusc += 1
            }
            else {
                minusc += 1
            }
        }
        if ((mayusc > 0) && (minusc > 0) && (digit > 0) && (length >= 6)){
                return true
            }
        return false
    },
    clear () {
        this.error_form = false
        this.error_list = []
        this.error = false
        this.errorText = ''
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
                this.errorText = JsonResponse['message']
                this.error = true
            }
        })
        .catch(() => {
            this.errorText = 'Something went wrong!'
            this.error = true
        })
    }
  }
}
</script>
