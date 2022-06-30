<template>
    <div>
        <div class="AdminNav">
            <input type="checkbox">
            <span></span>
            <span></span>
            <div class="menu">
                <li>
                    <router-link to="/admin"><a>HOME ADMIN</a></router-link>
                </li>
                <li>
                    <router-link class="part_menu" to="/admin/create"><a>CREATE PRODUCTS</a></router-link>
                </li>
                <li>
                    <router-link class="part_menu" to="/admin/delete"><a>DELETE PRODUCTS</a></router-link>
                </li>
                <li>
                    <router-link class="part_menu" to="/admin/update"><a>UPDATE PRODUCTS</a></router-link>
                </li>
            </div>
        </div>
        <router-view/>
  </div>
</template>

<script>
export default {
    name: 'AdminNavigator'
}
</script>

<style scoped>
    .AdminNav, .menu{
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .AdminNav{
        position: relative;
        background-color: #fff;
        padding: 20px;
        transition: 0.5s;
        border-radius: 50px;
        overflow: hidden;
        box-shadow: 0 8px 15px rgba(0, 0, 0, .2);
    }
    .menu{
        margin: 0;
        padding: 0;
        width: 0;
        overflow: hidden;
        transition: 0.5s;
        flex-direction: row;
    }
    .AdminNav input:checked ~ .menu{
        width: 450px;
    }
    .menu li {
        list-style: none;
        margin: 0 10px;
    }
    .menu li a{
        text-decoration: none;
        color: #666;
        text-transform: uppercase;
        font-weight: 600;
        transition: 0.5s;
    }
    .menu li part_menu:hover{
        color:#161919;
    }
    .AdminNav input {
        width: 40px;
        height: 40px;
        cursor: pointer;
        opacity: 0;
    }
    .AdminNav span {
        position:absolute;
        left:30px;
        width:30px;
        height: 4px;
        border-radius: 50px;
        background-color: #666;
        pointer-events: none;
        transition: 0.5s;
    }
    .AdminNav input:checked ~ span{
        background-color: #f974a1;
    }
    .AdminNav span:nth-child(2) {
        transform: translateY(-8px);
    }
    .AdminNav input:checked ~ span:nth-child(2) {
        transform: translateY(0) rotate(-45deg);
    }
    .AdminNav span:nth-child(3) {
        transform: translateY(8px);
    }
    .AdminNav input:checked ~ span:nth-child(3) {
        transform: translateY(0) rotate(45deg);
    }
</style>