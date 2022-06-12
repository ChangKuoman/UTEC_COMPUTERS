<template>
    <div>
        <form>
            <p>USERNAME</p>
            <input v-model = "username" type="text"/>
            <p>PASSWORD</p>
            <input v-model = "password" type="password"/>
            <button @click.prevent = "login">LOGIN</button>
        </form>

        <div v-if = "wentWrong">
            Username is not valid or password is wrong
        </div>
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
        wentWrong: false,
        username: '',
        password: ''
    }
  },
  methods: {
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
