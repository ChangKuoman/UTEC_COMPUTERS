<template>
    <div class="error_view">
        <h2>{{error.number}} - {{error.text}}</h2>
        <img class = "img-500" :src = "require(`@/assets/img/${error.number}_error.jpg`)" />
        <div class="box_boton2">
            <router-link class="mod_color" to="/simulator">BACK</router-link>
        </div>

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
    .error_view{
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        width: 100%;
        height: 100%;

        background-color: white;
    }
    .mod_color{
        color:white
    }
</style>
