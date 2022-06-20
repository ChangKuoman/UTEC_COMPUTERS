<template>
    <div>
        <p>
            {{product.name}}
        </p>
        <p>
            S/. {{product.price.toFixed(2)}}
        </p>
    </div>
</template>

<script>
export default {
    name: 'ProductSimulation',
    props: {
        product: {
            type: Object,
            default() {
                return {}
            }
        }
    }
}
</script>
