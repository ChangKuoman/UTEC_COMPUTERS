<template>
    <div>
        <div class="contenedor_HOME">
            <div class="Texto_presentacion">
                <form @change = "error.clear">
                    <InputText
                        v-model="username"
                        title="USERNAME"
                        type="text"
                    />
                    <InputText
                        v-model="password"
                        title="PASSWORD"
                        type="password"
                    />
                    <button @click.prevent = "error.clear(); check_form_login()">LOGIN</button>
                </form>
                    <ErrorList
                    class="no-dots"
                    v-if="error"
                    :error_list="error.list"
                />
            </div>
        </div>
        <FooterComponent/>
    </div>
</template>

<script>
import FooterComponent from '@/components/FooterComponent.vue'
import InputText from '@/components/InputText.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
  components: { FooterComponent, InputText, ErrorList },
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
                localStorage.setItem('token', JsonResponse['token'])

                if (JsonResponse['user']['role'] === 'admin') {
                    this.$root.data_session.admin = true
                }
                this.$root.data_session.logged = true
                this.$root.user_info = JsonResponse['user']

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


<style scoped>
    input{
        border-style:groove;
        border-radius: 2px 2px;
    }
</style>