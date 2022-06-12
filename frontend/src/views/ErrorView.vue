<template>
    <div>
        <h2>{{error.number}} - {{error.text}}</h2>
        <img class = "img-500" :src = "require(`@/assets/img/${error.number}_error.jpg`)" />

        <router-link to="/simulator">BACK</router-link>
    </div>
</template>

<script>
export default {
    name: 'ErrorView',
    props: ['errorNumber', 'errorText'],
    mount () {
        if (this.errorNumber !== null && this.errorText !== null) {
            this.error.number = this.errorNumber
            this.error.text = this.errorText
        }
    },
    data () {
        return {
            error: {
                number: '404',
                text: 'Resource Not Found'
            }
        }
    }
}
</script>

<style scoped>
    .img-500{
        height: 500px;
        width: 500px;
    }
</style>
