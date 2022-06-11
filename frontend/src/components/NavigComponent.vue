<template>
  <nav>

    <router-link to="/">
      <img class="img-64" src="@/assets/img/logo.png" alt="Logo"/>
    </router-link>
    <router-link to="/">
      <h1>UTEC COMPUTERS</h1>
    </router-link>

    <div>
      <router-link v-if = "login" to="/login">Login</router-link>
      <router-link v-if = "register" to="/register">Register</router-link>
      <router-link v-if = "admin" to="/admin">Admin</router-link>
      <button v-if = "logout">Logout</button>
    </div>

  </nav>
  <router-view/>
</template>

<script>
export default {
  name: 'NavigComponent',
  props: ['login', 'logout', 'register', 'admin']
}
</script>

<style scoped>
  .img-64 {
    height: 64px;
    width: 64px;
  }
</style>