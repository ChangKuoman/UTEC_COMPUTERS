<template>
  <NavigComponent
    :login = "login"
    :logout = "logout"
    :register = "register"
    :admin = "admin"
  />
</template>

<script>
import NavigComponent from './components/NavigComponent.vue'

export default {
  components: { NavigComponent },
  data () {
    return {
      login: true,
      logout: false,
      register: true,
      admin: false
    }
  }
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');
  html{
    font-family: 'Lato', sans-serif;
  }
  button{
    font-family: 'Lato', sans-serif;
  }
  a:link { text-decoration: none; }
  a:visited { text-decoration: none; }
  a:hover { text-decoration: none; }
  a:active { text-decoration: none; }
  .no-dots{
    list-style-type: none;
}
</style>
