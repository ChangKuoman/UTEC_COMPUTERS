<template>
    <p :style="password_color"><b>{{password_strength}}</b></p>
</template>

<script>
export default {
    name: 'PasswordStrength',
    props: {
        password: {
            type: String,
            default: ''
        },
        strength: {
            type: String,
            default: ''
        }
    },
    computed: {
        password_strength: function() {
            const strong = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{8,})/
            const medium2 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[.,\-_+&$#@()*"':;!?])(?=.{6,})/
            const medium1 = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.{6,})/
            if (strong.test(this.password)) {
                this.$emit('update:modelValue', 'Strong password')
                return 'Strong password'
            }
            if (medium2.test(this.password)) {
                this.$emit('update:modelValue', 'Medium password')
                return 'Medium password'
            }
            if (medium1.test(this.password)) {
                this.$emit('update:modelValue', 'Weak password')
                return 'Weak password'
            }
            this.$emit('update:modelValue', 'Very weak password')
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
    }
}
</script>
