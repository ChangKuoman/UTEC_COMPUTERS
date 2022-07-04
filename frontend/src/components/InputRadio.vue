<template>
    <div>
        <h4>{{ title }}</h4>
        <ul v-bind="$attrs">
            <li v-for="(element, index) in objects" :key="index">
                <div class="description_name">
                    <input
                        type="radio"
                        :checked="element === modelValue"
                        @click="$emit('update:modelValue', element)"
                    />
                    <label>{{element.name}}</label>
                </div>
                <div class="description_prod">
                    <p><span class="weight600">Description:</span> {{element.description}}</p>
                    <p><span class="weight600">Price:</span> S/. {{element.price.toFixed(2)}}</p>
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

<style scoped>
.description_name{
    width: auto;
    padding-top: 9px;
    padding-bottom: 9px;
}
.description_prod{
    width: auto;
    padding: 15px;
    margin-left: 18px;
    border-radius: 10px;
    box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
}
.weight600{
    font-weight: 600;
}
</style>