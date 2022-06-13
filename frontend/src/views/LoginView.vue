<template>
    <div>
        <div class="contenedor_HOME">
            <div class="Texto_presentacion">
                <form @change = "error.clear">
                    <p>USERNAME</p>
                    <input v-model = "username" type="text"/>
                    <p>PASSWORD</p>
                    <input v-model = "password" type="password"/>
                    <button @click.prevent = "error.clear(); check_form_login()">LOGIN</button>
                </form>
            </div>
        </div>
        <ul class = "no-dots" v-if = "error">
            <li v-for = "(error, index) in error.list" :key = "index">{{error}}</li>
        </ul>
        <FooterComponent/>
    </div>
</template>

<script>
import FooterComponent from '../components/FooterComponent.vue'
export default {
  components: { FooterComponent },
  props: [],
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
        password: ''
    }
  },
  methods: {
    check_form_login () {
        if (this.username === '') {
            this.error.list.push('Username cannot be empty')
        }
        if (this.password === '') {
            this.error.list.push('Password cannot be empty')
        }
        if (this.error.list.length) {
            this.error.show = true
        }
        if (this.error.show === false) {
            this.login()
        }
    },
    login () {
        fetch('http://127.0.0.1:5000/users', {
            method: 'POST',
            body: JSON.stringify({
                'username': this.username,
                'password': this.password,
                'login': true
            }),
            headers: {
                'Content-Type': 'application/json'
            }
        })
        .then(response => response.json())
        .then(JsonResponse => {
            if (JsonResponse['success'] === true) {
                console.log(JsonResponse)
                localStorage.setItem('token', JsonResponse['token'])

                let admin = false
                if (JsonResponse['user']['role'] === 'admin') {
                    admin = true
                }

                this.$root.change_user_info(JsonResponse['user'])
                this.$root.change_data_session({
                    'login': false,
                    'logout': true,
                    'admin': admin,
                    'register': false,
                    'simulator': true
                })

                this.$router.push('/simulator')
            }
            else {
                this.error.list.push('Username is not valid or password is wrong')
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
