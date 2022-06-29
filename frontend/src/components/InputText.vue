<template>
    <div>
        <p>{{ title }}</p>
        <input
            v-bind="$attrs"
            :value="modelValue"
            @input="$emit('update:modelValue', $event.target.value)"
        />
    </div>
</template>

<script>
export default {
    name: 'InputText',
    props: {
        title: {
            type: String,
            default: ''
        },
        modelValue: {
            type: [String, Number],
            default: ''
        }
    }
}
</script>