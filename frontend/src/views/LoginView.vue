<template>
  <div>
    <div class="contenedor_HOME">
      <div class="Texto_presentacion">
        <h2>Sign In</h2>
        <form class="padding20" @change="error.clear">
          <InputText v-model="username" title="USERNAME" type="text" />
          <InputText v-model="password" title="PASSWORD" type="password" />
        </form>
        <button
          class="buttom1"
          @click.prevent="
            error.clear();
            check_form_login();
          "
        >
          LOGIN
        </button>
        <p>
          Don't have an account?
          <router-link class="buttom2" to="/register">CREATE</router-link>
        </p>
        <ErrorList class="no-dots" v-if="error" :error_list="error.list" />
      </div>
    </div>
    <FooterComponent />
  </div>
</template>

<script>
import { host } from "@/host.js";
import FooterComponent from "@/components/FooterComponent.vue";
import InputText from "@/components/InputText.vue";
import ErrorList from "@/components/ErrorList.vue";

export default {
  components: { FooterComponent, InputText, ErrorList },
  props: [],
  data() {
    return {
      error: {
        show: false,
        list: [],
        clear: () => {
          this.error.show = false;
          this.error.list = [];
        },
      },
      username: "",
      password: "",
    };
  },
  methods: {
    check_form_login() {
      if (this.username === "") {
        this.error.list.push("Username cannot be empty");
      }
      if (this.password === "") {
        this.error.list.push("Password cannot be empty");
      }
      if (this.error.list.length) {
        this.error.show = true;
      }
      if (this.error.show === false) {
        this.login();
      }
    },
    login() {
      fetch(host + "/users", {
        method: "POST",
        body: JSON.stringify({
          username: this.username,
          password: this.password,
          login: true,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            localStorage.setItem("token", JsonResponse["user"]["token"]);
            if (JsonResponse["user"]["role"] === "admin") {
              this.$root.data_session.admin = true;
            }
            this.$root.data_session.logged = true;

            this.$router.push("/simulator");
          } else {
            this.error.list.push("Username is not valid or password is wrong");
            this.error.show = true;
          }
        })
        .catch(() => {
          this.error.list.push("Something went wrong!");
          this.error.show = true;
        });
    },
  },
};
</script>

<style scoped>
input {
  border-style: groove;
  border-radius: 2px 2px;
}
.buttom1 {
  padding: 5px;
  font-size: 15px;
  margin-left: 10px;
  margin-right: 10px;

  border-radius: 5px;
  color: white;
  cursor: pointer;
  border: none;
  background: #333;
}
.buttom2 {
  cursor: pointer;
  font-size: 15px;
  border: 0;
  text-decoration: none;
  color: lightseagreen;
}
.padding20 {
  padding: 20px;
}
</style>
