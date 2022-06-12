<template>
  <div class="wallpaper">
    <nav class="header">

      <!--BOX-LOGO-->
      <div class="box_LOGO">
        <router-link to="/">
          <img class="img-64" src="@/assets/img/logo.png" alt="Logo"/>
        </router-link>
      </div>
      <!--BOX-EMPRESA_NAME-->
      <div class="box_EMPRESA_NAME">
        <router-link to="/">
          <h1>UTEC COMPUTERS</h1>
        </router-link>
      </div>

      <!--CONTENEDOR_BOTONES-->
      <div class="CONTENEDOR_BOTONES">
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
  .wallpaper{
    width: auto;
    margin: 0%;
    height: auto;
    
    background-image: url(@/assets/img/fondo.jpg);
    background-size: cover;
    }
  .header{
    height: 70px;
    margin: 0, 0, 0, 0;

    display: flex;
    flex-direction: row;

    align-items: center;
    background-color: rgb(225, 248, 255);
  }
  .header:hover{
    box-shadow: 0 12px 16px 0 rgba(104, 169, 255, 0.24), 0 17px 50px 0 rgba(153, 135, 255, 0.19);
    border-bottom-style: solid;
    border-bottom-color: rgb(81, 161, 231);
    border-bottom-left-radius: 3px;
    border-bottom-right-radius: 3px;
  }
  body{
    margin-left: 0px;
    margin-right: 0px;
    margin-top: 0px;
    margin-bottom: 0px;
  }
  .mostrarContenedor{
    border: 3px solid rgb(255, 255, 255);
  }

  .box_LOGO{
    min-width: 12%;
    width: auto;
    height: 60px;
    display:flex;

    align-items: center;
    justify-content: center;
  }
  .box_EMPRESA_NAME{
    min-width: 40%;
    width: auto;
    height: 60px;
    display: flex;

    align-items: center;
    justify-content: center;

    text-decoration: none;
    font-size: 22px;
    filter: drop-shadow(5px 10px 5px #000000e8);
  }
  .CONTENEDOR_BOTONES{
    min-width: 40%;
    width: auto;
    height: 60px;
    display: flex;

    align-items: center;
    justify-content: end;
  }

    .contenedor_HOME{
    
    width: 70%;
    height: 800px;
    margin-left: 15%;
    margin-right: 15%;
    
    display: flex;
    justify-content: center;
    margin-top: 1%;
    margin-bottom: 1%;
    padding: 3%;   
    }
    .Texto_presentacion{
    width: 50%;
    height: 400px;
    padding: 5%;
    border-radius: 10px 10px;

    display: flex;
    flex-direction: column;
    
    text-align: justify;
    font-style:italic;
    font-family: 'Lato', sans-serif;
    font-size: 20px;

    background: #fffffffd;
    color: #333;
    
    }
</style>
