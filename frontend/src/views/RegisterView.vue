<template>
    <div>
        <form>
            <p>USERNAME</p>
            <input type="text"/>
            <p>PASSWORD</p>
            <input type="password"/>
            <p>ENTER PASSWORD AGAIN</p>
            <input type="password"/>
            <button>REGISTER</button>
        </form>

        <div v-if = "wentWrong">
            Something went wrong!
        </div>
    </div>
    <FooterComponent/>
</template>

<script>
import FooterComponent from '../components/FooterComponent.vue'
export default {
  components: { FooterComponent },
  data () {
    return {
        wentWrong: false
    }
  }
}
</script>
