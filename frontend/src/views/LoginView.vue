<template>
    <div>
        <form>
            <p>USERNAME</p>
            <input type="text"/>
            <p>PASSWORD</p>
            <input type="password"/>
            <button>LOGIN</button>
        </form>

        <div v-if = "wentWrong">
            Username is not valid or password is wrong
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
