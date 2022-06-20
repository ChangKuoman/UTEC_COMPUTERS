<template>
    <div>
        <div>
            <h2>Change password</h2>
            <form @change = "error.clear">
                <InputText
                    v-model="old_password"
                    title="OLD PASSWORD"
                    type="password"
                />
                <InputText
                    v-model="new_password"
                    title="NEW PASSWORD"
                    type="password"
                />
                <PasswordStrength
                    v-model="password_strength"
                    :password="new_password"
                    v-show="new_password.length"
                />
                <button @click.prevent = "error.clear(); check_change_form()">Change password</button>
            </form>
            <ErrorList
                class="no-dots"
                v-if="error.show"
                :error_list="error.list"
            />
        </div>
        <div>
            <h2>SEE PREVIOUS SIMULATIONS</h2>
            <ul v-if="!error_simulations.length" class="no-dots">
                <li v-for = "(simulation, index) in simulations" :key = "index">
                    <p>Simulation id: {{simulation.id}}</p>
                    <p>Total price: {{simulation.total_price.toFixed(2)}}</p>
                    <button @click.prevent = "see_simulation(simulation.id)">See simulation</button>
                </li>
            </ul>
            <p v-if="error_simulations.length">{{error_simulations}}</p>
        </div>
    </div>
</template>

<script>
import InputText from '@/components/InputText.vue'
import PasswordStrength from '@/components/PasswordStrength.vue'
import ErrorList from '@/components/ErrorList.vue'

export default {
    components: { InputText, PasswordStrength, ErrorList },
    data () {
        return {
            old_password: '',
            new_password: '',
            error: {
                show: false,
                list: [],
                clear: () => {
                    this.error.show = false
                    this.error.list = []
                }
            },
            error_simulations: '',
            simulations: [],
            password_strength: ''
        }
    },
    mounted () {
        if (localStorage.getItem('token')) {
            fetch('http://127.0.0.1:5000/simulations', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    this.simulations = Object.values(JsonResponse['simulations']).filter(simulation => {
                        return simulation.create_by === this.$root.user_info.id
                    })
                }
                else if (JsonResponse['code'] === 404) {
                    this.error_simulations = 'You do not have any simulations'
                }
                else {
                    this.error_simulations = JsonResponse['message']
                }
            })
            .catch(() => {
                this.error_simulations = "Something went wrong!"
            })
        }
        else {
            this.$router.push('/login')
        }
    },
    methods: {
        see_simulation (id) {
            this.$router.push("/simulation/" + id)
        },
        check_change_form () {
            if (this.old_password === '') {
                this.error.list.push('Fill your old password')
            }
            if (this.new_password === '') {
                this.error.list.push('Fill your new password')
            }
            else if (this.old_password === this.new_password) {
                this.error.list.push('You cannot put the same password to change')
            }
            else if (this.password_strength !== 'Strong password') {
                this.error.list.push('Password must be strong')
            }
            if (this.error.list.length) {
                this.error.show = true
            }
            if (this.error.show === false) {
                this.changePassword()
            }
        },
        changePassword () {
            fetch('http://127.0.0.1:5000/users/' + this.$root.user_info.id, {
                method: "PATCH",
                body: JSON.stringify({
                    'old_password': this.old_password,
                    'new_password': this.new_password
                }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(response => response.json())
            .then(JsonResponse => {
                if (JsonResponse['success'] === true) {
                    alert('Password change successfully!')
                    this.old_password = ''
                    this.new_password = ''
                }
                else {
                    this.error.show = true
                    this.error.list.push('Your old password does not match')
                }
            })
            .catch(() => {
                this.error.show = true
                this.error.list.push('Something does not works!')
            })
        }
    }
}
</script>
