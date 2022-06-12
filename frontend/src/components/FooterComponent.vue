<template>
    <div>
        <footer>
        <img class="img-200" src="@/assets/img/left-dog.jpg">
        <div class="footer_box">
            <h3>
                PARTNERS:
            </h3>
            <p>Samanta Susana Chang Kuoman</p>
            <p>Anderson David Cárcamo Vargas</p>
        </div>
        <div class="footer_box">
            <h3>
                CONTACT:
            </h3>
            <p>samanta.chang@utec.edu.pe</p>
            <p>anderson.carcamo@utec.edu.pe</p>
        </div>
        <img class="img-200" src="@/assets/img/right-dog.jpeg">
    </footer>
    </div>
</template>

<script>
export default {
  name: 'FooterComponent'
}
</script>

<style scoped>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap');
    div {
        font-family: 'Lato', sans-serif;
    }

    .img-200 {
        width: 200px;
        height: 200px;
    }

    footer {
    width: auto;
    height: 25%;

    padding: 2%;
    background: #ffff;
    border: 3px solid white;

    display: flex;
    flex-direction: row;
    justify-content: center;
    }

    .footer_box{
    display: flex;
    flex-direction: column;

    font-style: italic;

    margin-left: 15px;
    margin-right: 15px;
    padding: 5px;
    }

</style>
