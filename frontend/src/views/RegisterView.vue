<template>
    <div>
        <div class="contenedor_HOME">
            <div class="Texto_presentacion">
                <h2>Register</h2>
                <form class="padding20" @change = "error.clear">
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
                    <PasswordStrength
                        v-model="password_strength"
                        :password="password"
                        v-show="password.length"
                    />
                    <InputText
                        v-model="password_confirm"
                        title="CONFIRM PASSWORD"
                        type="password"
                    />
                </form>
                <button class="buttom1" @click.prevent = "error.clear(); check_register_form()">REGISTER</button>
                <ErrorList
                    class="no-dots"
                    v-if="error.show"
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
import PasswordStrength from '@/components/PasswordStrength.vue'

export default {
  components: { FooterComponent, InputText, ErrorList, PasswordStrength },
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
        password_confirm: '',
        password_strength: ''
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
        else if (this.password_strength !== 'Strong password') {
            this.error.list.push('Password must be strong')
        }
        if (this.error.list.length) {
            this.error.show = true
        }
        if (this.error.show === false) {
            this.register()
        }
    },
    register () {
        fetch('http://127.0.0.1:5000/users', {
            method: 'POST',
            body: JSON.stringify({
                'username': this.username,
                'password': this.password
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
<style scoped>
    .buttom1{
        padding: 5px;
        font-size: 15px;
        margin-left: 10px;
        margin-right:10px;

        border-radius: 5px;
        cursor: pointer;
        border: none;
        color: white;
        background: #333;
    }
    .padding20{
        padding: 20px;
    }
</style>