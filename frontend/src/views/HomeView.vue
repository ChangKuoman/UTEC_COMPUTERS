<template>
    <div>
        <div>
            <div class="contenedor_HOME">
                <div class="Texto_presentacion">
                    <p>
                        Our project is a web application made with the Flask micro Framework
                        that allows the simulated purchase of a computer taking into account
                        the motherboard and its compatibility with the different components
                        as the base piece. The information in the database is based on different
                        web pages for the purchase of specialized technology in computers
                        such as LoginStore, and proprietary brands such as MSI, AMD, Intel,
                        among others.
                    </p>

                    <img class="img-150" src="@/assets/img/cat.gif" />

                    <a href="https://github.com/ChangKuoman/UTEC_COMPUTERS" target="_target">⇨ LINK TO GITHUB </a>
                </div>
            </div>
            
            
        </div>
        <FooterComponent/>
    </div>
</template>

<script>
import FooterComponent from '../components/FooterComponent.vue'
export default {
  components: { FooterComponent },
}
</script>

<style scoped>
    .img-150 {
        width: 150px;
        height: 150px;
    }

</style>
