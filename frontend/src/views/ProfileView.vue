<template>
    <div>
        <div>
            <h2>Change password</h2>
            <div>
                <p>Old password</p>
                <input type = "password"/>
                <p>New password</p>
                <input type = "password"/>
                <p v-show = "password.length" :style = "password_color"><b>{{password_strength}}</b></p>
            </div>
        </div>
        <div>
            <h2>See previous simulations</h2>
        </div>
    </div>
</template>

<script>
export default {
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
}
</script>
