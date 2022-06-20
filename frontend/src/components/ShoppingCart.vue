<template>
    <div>
        <div>
            <h2>SHOPPING CART</h2>
            <img class="img-20" src="@/assets/img/shopping_cart.png" alt="Shopping Cart">
        </div>

        <ul class="no-dots">
            <li v-for="(product, index) in total_products" :key="index">{{product.name}} S/.{{product.price.toFixed(2)}}</li>
        </ul>
        <p><b>TOTAL PRICE: S/. {{total_price.toFixed(2)}}</b></p>
        <button @click.prevent="$emit('onSimulate')">SIMULATE!</button>
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
</style>
