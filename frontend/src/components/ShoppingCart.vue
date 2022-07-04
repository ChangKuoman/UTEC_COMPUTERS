<template>
    <div>
        <div class="container">
            <div class="shop">
                <h2 class="tittle_shop">
                    SHOPPING CART
                    <img class="img-20" src="@/assets/img/shopping_cart.png" alt="Shopping Cart">
                </h2>
            </div>
            <!--
            <div class="list_shop">
                <ul class="no-dots list_shop">
                    <li v-for="(product, index) in total_products" :key="index">
                        <span class="weight600">{{product.name}}: </span> S/.{{product.price.toFixed(2)}}
                    </li>
                </ul>
            </div>
            -->
            <div>
                <ul class="no-dots list_shop">
                    <li v-for="(product, index) in total_products" :key="index">
                        <span class="weight600">{{product.name}}: </span> S/.{{product.price.toFixed(2)}}
                    </li>
                </ul>
            </div>

            <p><b>TOTAL PRICE: S/. {{total_price.toFixed(2)}}</b></p>
            <button class="buttom1" @click.prevent="$emit('onSimulate')">SIMULATE!</button>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ShoppingCart',
    props: {
        total_products: {
            type: Array,
            default() {
                return []
            }
        },
        total_price: {
            type: Number,
            default: 0
        }
    }
}
</script>

<style scoped>
    .img-20 {
        width: 20px;
        height: 20px;
    }
    .list_shop{

        width: 100%;
        margin-top: 5px;
        margin-bottom: 5px;
        height: 150px;
        padding: 0;

        overflow: auto;
    }
    .list_shop::-webkit-scrollbar {
        width: 4px;
    }
    .list_shop::-webkit-scrollbar-thumb {
        background: #333;
        border-radius: 5px 5px;
    }
    .shop{
        min-width:400px;
        padding: 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
    .tittle_shop{
        width: 300px;
        height: 50px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .buttom1{
        padding: 5px;
        font-size: 15px;
        margin-left: 10px;
        margin-right:10px;

        border-radius: 5px;
        cursor: pointer;
        border: none;
        color: white;
        background: #333;
    }
    .container{
        display: flex;
        flex-direction: column;
        padding: 10px;
        border-radius: 8px;
        margin-left: 30px;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
        background-color: rgb(95, 189, 226);
        color: white;
    }
</style>
