<template>
  <div class="contenedor_HOME">
    <div class="Texto_presentacion">
      <div class="error_view">
        <h2>404 - Resource Not Found</h2>
        <img class="img-500" src="@/assets/img/404_error.jpg" />
        <div class="box_boton2">
          <router-link class="mod_color" to="/simulator">BACK</router-link>
        </div>
      </div>
    </div>
  </div>
</template>

<script></script>

<style scoped>
.img-500 {
  height: 500px;
  width: 500px;
}
.error_view {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100%;

  background-color: white;
}
.mod_color {
  color: white;
}
.Texto_presentacion {
  min-height: 600px;
  min-width: 700px;
}
</style>
