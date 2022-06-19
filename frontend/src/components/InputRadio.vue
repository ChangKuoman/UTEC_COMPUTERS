<template>
    <div>
        <h2>{{ title }}</h2>
        <ul v-bind="$attrs">
            <li v-for="(element, index) in objects" :key="index">
                <input
                    type="radio"
                    :checked="element === modelValue"
                    @click="$emit('update:modelValue', element)"
                />
                <label>{{element.name}}</label>
                <div>
                    <p>Description: {{element.description}}</p>
                    <p>Price: S/. {{element.price.toFixed(2)}}</p>
                </div>
            </li>
        </ul>
    </div>
</template>

<script>
export default {
    name: 'InputRadio',
    props: {
        objects: {
            type: Object,
            default() {
                return {}
            }
        },
        modelValue: {
            type: Object,
            default() {
                return {}
            }
        },
        title: {
            type: String,
            defaul: ''
        }
    }
}
</script>
