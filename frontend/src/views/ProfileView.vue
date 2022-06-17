<template>
    <div>
        <div>
            <h2>Change password</h2>
            <form @change = "error.clear">
                <p>Old password</p>
                <input v-model = "old_password" type = "password"/>
                <p>New password</p>
                <input v-model = "new_password" type = "password"/>
                <p v-show = "new_password.length" :style = "password_color"><b>{{password_strength}}</b></p>
                <button @click.prevent = "error.clear(); check_change_form()">Change password</button>
            </form>
            <ul class = "no-dots" v-if = "error.show">
                <li v-for = "(error, index) in error.list" :key = "index">{{error}}</li>
            </ul>
        </div>
        <div>
            <h2>See previous simulations</h2>
            <ul v-if = "simulations" class="no-dots">
                <li v-for = "(simulation, index) in simulations" :key = "index">
                    <p>Simulation id: {{simulation.id}}</p>
                    <p>Total price: {{simulation.total_price.toFixed(2)}}</p>
                    <button @click.prevent = "see_simulation(simulation.id)">click</button>
                </li>
            </ul>
        </div>
        <router-view/>
    </div>
</template>

<script>
export default {
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
                else {
                    this.no_simulations = 'You do not have any simulations'
                }
            })
            .catch(() => {
                console.log("js error")
            })
        }
        else {
            this.$router.push('/login')
        }
    },
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
            no_simulations: '',
            simulations: []
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
                    this.error.list.push('Your password does not match')
                }
            })
            .catch(() => {
                this.error.show = true
                this.error.list.push('Something does not works!')
            })
        }
    },
    computed: {
        password_strength: function() {
            const strong = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{8,})/
            const medium2 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{6,})/
            const medium1 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})/
            if (strong.test(this.new_password)) {
                return 'Strong password'
            }
            if (medium2.test(this.new_password)) {
                return 'Medium password'
            }
            if (medium1.test(this.new_password)) {
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
}
</script>
