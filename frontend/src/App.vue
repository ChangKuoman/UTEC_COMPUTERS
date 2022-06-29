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
          <h1 class="milky">UTEC COMPUTERS</h1>
        </router-link>
      </div>

      <!--CONTENEDOR_BOTONES-->

      <!--CUANDO NO ESTA LOGEADO-->
      <div class="CONTENEDOR_BOTONES" v-if = "!data_session.logged">

        <div class="box_boton">
          <router-link class="h_1" v-if = "!data_session.logged" to="/login">LOGIN</router-link>
        </div>
        <div class="box_boton">
          <router-link class="h_1" v-if = "!data_session.logged" to="/register">REGISTER</router-link>
        </div>

      </div>

      <!--CUANDO ESTA LOGEADO-->
      <div class="CONTENEDOR_BOTONES" v-if = "data_session.logged">

        <button @click="show_despliegue" class="box_boton">
            <i id="boton_despliegue" class='bx bxs-user-circle'></i>
        </button>
        
        <div v-if = "despliegue">
          <!--CUANDO ESTA LOGEADO Y NO ES ADMIN-->
          <div class="CONTENEDOR_BOTONES_LOGIN" v-if = "!data_session.admin">
            <div class="boton_3">
              <router-link class="text_white" v-if = "data_session.logged" to="/simulator">SIMULATE!</router-link>
            </div>
            <div class="boton_3">
              <router-link class="text_white" v-if = "data_session.logged" to="/profile">PROFILE</router-link>
            </div>
            <div class="boton_3">
              <button class="text_white" id="cursor_pointer" @click.prevent = "logout_session" v-if = "data_session.logged">LOGOUT</button>
            </div>
          </div>
          <!--CUANDO ESTA LOGEADO Y ES ADMIN-->
          <div class="CONTENEDOR_BOTONES_LOGIN" v-if = "data_session.admin">
            <div class="boton_3">
              <router-link class="text_white" v-if = "data_session.admin" to="/admin">ADMIN</router-link>
            </div>
        
            <div class="boton_3">
              <router-link class="text_white" v-if = "data_session.logged" to="/simulator">SIMULATE!</router-link>
            </div>
            <div class="boton_3">
              <router-link class="text_white" v-if = "data_session.logged" to="/profile">PROFILE</router-link>
            </div>
            <div class="boton_3">
              <button class="text_white" id="cursor_pointer" @click.prevent = "logout_session" v-if = "data_session.logged">LOGOUT</button>
            </div>

          </div>
        </div>

      </div>

    
    </nav>
    <router-view :user_info="user_info"/>
  </div>
</template>

<script>

export default {
  name: 'navComponent',
  data () {
    return {
      data_session: {
        logged: false,
        admin: false,

      },
      user_info: null,
      despliegue: false
    }
  },
  mounted () {
    if (localStorage.getItem('token')){
      localStorage.removeItem('token')
    }
  },
  methods: {
    logout_session () {
      localStorage.removeItem('token')
      this.data_session.logged = false
      this.data_session.admin = false
      this.user_info = null
      this.$router.push('/')

    },
    show_despliegue() {
      this.despliegue = !this.despliegue

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

    /*background-image: url(@/assets/img/fondo.jpg);*/
    background-size: cover;
    }
  .header{
    height: 70px;
    margin: 0, 0, 0, 0;

    display: flex;
    flex-direction: row;

    align-items: center;
    
    background: linear-gradient(to bottom,  rgb(255, 255, 255) 0%,rgb(249, 254, 255) 100%);
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
    text-align:center;
  }
  .milky {
    font-family: "Arial Rounded MT Bold", "Helvetica Rounded", Arial, sans-serif;;
    text-transform: uppercase;
    display: block;
    font-size: 50px;
    color: #585756;
    text-shadow: 0 8px 9px #c4b59d, 0px -2px 1px #fff;
    font-weight: bold;
    letter-spacing: -4px;
    text-align: center;
    padding: 10px 20px;
    border-radius: 20px;
  }

  .box_boton{
    width: 10%;
    min-width: 100px;
    display: inline-block;
    

    border-radius: 5px 5px;
    border: none;
    margin-top: 5px;
    margin-bottom: 5px;
    margin-left: 1%;
    margin-right: 1%;
    padding: 1%;

    background: rgba(34, 132, 139, 0.932);

    text-decoration: none;
    text-align: center;

    cursor: pointer;
  }
  .box_boton:hover{
    box-shadow: 0 12px 16px 0 rgba(0,0,0,0.24), 0 17px 50px 0 rgba(0,0,0,0.19);
  }
  .h_1{
    display: inline-block;
    width: 100%;
    height: 100%;
    color: aliceblue;
    font-size: 15px;
    font-weight: 700;
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

    width: 100%;
    height: 950px;


    display: flex;
    justify-content: center;
    /*
    margin-top: 1%;
    margin-bottom: 1%;
    padding: 3%;
*/
    display: flex;
    justify-content: center;
    align-items: center;
  }
  .contenedor_app{
    width: 80%;
    height: 95%;
    
    margin-top: 2%;
    margin-bottom: 2%;
    padding: 1%;

    background: #fffffffd;
  }
  .Texto_presentacion{
    width: 50%;
    height: 400px;
    padding: 5%;
    border-radius: 10px 10px;

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;
    text-align: justify;
    font-style:italic;
    font-family: 'Lato', sans-serif;
    font-size: 20px;

    background: #fffffffd;
    color: #333;
  }

  .box_boton2{
    min-width: 100px;
    display: inline-block;

    border-radius: 5px 5px;
    border: none;
    margin-top: 5px;
    margin-bottom: 5px;
    margin-left: 1%;
    margin-right: 1%;
    padding: 5px 2px 5px 2px;

    background: rgba(43, 44, 44, 0.932);

    text-decoration: none;
    text-align: center;
  }
  .CONTENEDOR_BOTONES_LOGIN{
    display: flex;
    flex-direction: column;
    position: absolute;
    transform: translate(-100%,30px);

    width: 70px;
    height: 120px;
    padding-left: 15px;
    padding-right: 15px;
    
    align-items: center;
    justify-content: center;

    border-radius: 5%;
    background: #333;
    color: white;
  }

  .text_white{
    color:white;
    background: none;
    border: none;
  }
  .boton_3 {
    background: none;
    border: none;

    width: 100%;
    cursor: pointer;

    border-bottom-style: solid;
    border-bottom-width: 2px;
    border-bottom-color: whitesmoke;

    padding-top: 2px;
    padding-bottom: 2px;

  }

  #boton_despliegue {
    widows: 100%;
    height: 100%;

    color: white;
    background:none;
    border: none;
    font-size: 25px;
  }
  #cursor_pointer{
    cursor:pointer;
  }
</style>
