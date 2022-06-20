<template>
    <ul>
        <li v-bind="$attrs" v-for = "(error, index) in error_list" :key = "index">{{error}}</li>
    </ul>
</template>

<script>
export default {
    name: 'ErrorList',
    props: {
        error_list: {
            type: Array,
            default() {
                return []
            }
        }
    }
}
</script>