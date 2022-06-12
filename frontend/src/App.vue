<template>
  <div>
    <nav>

      <router-link to="/">
        <img class="img-64" src="@/assets/img/logo.png" alt="Logo"/>
      </router-link>
      <router-link to="/">
        <h1>UTEC COMPUTERS</h1>
      </router-link>

      <div>
        <router-link v-if = "data_session.login" to="/login">Login</router-link>
        <router-link v-if = "data_session.register" to="/register">Register</router-link>
        <router-link v-if = "data_session.admin" to="/admin">Admin</router-link>
        <button @click.prevent = "logout_session" v-if = "data_session.logout">Logout</button>
        <router-link v-if = "data_session.simulator" to="/simulator">Simulate!</router-link>
      </div>

    </nav>
    <router-view/>
  </div>
</template>

<script>

export default {
  name: 'navComponent',
  data () {
    return {
      data_session: {
        login: true,
        logout: false,
        register: true,
        admin: false,
        simulator: false
      },
      user_info: null
    }
  },
  methods: {
    logout_session () {
      localStorage.removeItem('token')
      this.change_data_session({
          'login': true,
          'logout': false,
          'admin': false,
          'register': true,
          'simulator': false
      })
      this.change_data_session(null)
      this.$router.push('/')
    },
    change_data_session (data = this.data_session) {
      this.data_session.login = data.login
      this.data_session.logout = data.logout
      this.data_session.register = data.register
      this.data_session.admin = data.admin
      this.data_session.simulator = data.simulator
    },
    change_user_info (data) {
      this.user_info = data
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
  .img-64 {
    height: 64px;
    width: 64px;
  }
</style>
