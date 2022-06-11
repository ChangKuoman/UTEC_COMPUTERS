<template>
    <div>
        <h2>{{errorNumber}} - {{errorText}}</h2>
        <img class = "img-500" :src = "errorImage"/>
        <router-link to="/simulator">BACK</router-link>
    </div>
</template>

<script>
export default {
    props: ['errorNumber', 'errorText'],
    data () {
        return {
            errorImage = this.errorNumber + "_error.JPG"
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