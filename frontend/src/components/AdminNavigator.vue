<template>
    <div>
        <router-link to="/admin">HOME ADMIN</router-link>
        <router-link to="/admin/create">CREATE PRODUCTS</router-link>
        <router-link to="/admin/delete">DELETE PRODUCTS</router-link>
        <router-link to="/admin/update">UPDATE PRODUCTS</router-link>
        <router-view/>
  </div>
</template>

<script>
export default {
    name: 'AdminNavigator'
}
</script>
