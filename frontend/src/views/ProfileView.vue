<template>
  <div class="contenedor_HOME">
    <div class="contenedor_app">
      <div class="PROF_1">
        <button class="buttom1" @click.prevent="change_prof(true)">
          CHANGE PASSWORD
        </button>
        <button class="buttom1" @click.prevent="change_prof(false)">
          PREVIUS SIMULATIONS
        </button>
      </div>
      <div class="PROF_2">
        <div class="PROFCont" v-if="show_CPassword">
          <h3>CHANGE PASSWORD</h3>
          <div class="menu_pass">
            <form class="pass_cont" @change="error.clear">
              <InputText
                v-model="old_password"
                title="OLD PASSWORD"
                type="password"
              />
              <InputText
                v-model="new_password"
                title="NEW PASSWORD"
                type="password"
              />
              <PasswordStrength
                v-model="password_strength"
                :password="new_password"
                v-show="new_password.length"
              />
            </form>
            <button
              class="buttom2"
              @click.prevent="
                error.clear();
                check_change_form();
              "
            >
              Change password
            </button>
          </div>
          <ErrorList
            class="no-dots"
            v-if="error.show"
            :error_list="error.list"
          />
        </div>
        <div class="PROFCont" v-if="!show_CPassword">
          <h3>YOUR PREVIOUS SIMULATIONS</h3>
          <ul v-if="!error_simulations.length" class="no-dots list_sim">
            <li v-for="(simulation, index) in simulations" :key="index">
              <div class="simElem">
                <div>
                  <p>Simulation id: {{ simulation.id }}</p>
                  <p>Total price: {{ simulation.total_price.toFixed(2) }}</p>
                </div>
                <button
                  class="buttom2"
                  @click.prevent="see_simulation(simulation.id)"
                >
                  See simulation
                </button>
              </div>
            </li>
          </ul>
          <p v-if="error_simulations.length">{{ error_simulations }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { host } from "@/host.js";
import InputText from "@/components/InputText.vue";
import PasswordStrength from "@/components/PasswordStrength.vue";
import ErrorList from "@/components/ErrorList.vue";

export default {
  components: { InputText, PasswordStrength, ErrorList },
  data() {
    return {
      old_password: "",
      new_password: "",
      error: {
        show: false,
        list: [],
        clear: () => {
          this.error.show = false;
          this.error.list = [];
        },
      },
      error_simulations: "",
      simulations: [],
      password_strength: "",
      show_CPassword: false,
    };
  },
  mounted() {
    if (localStorage.getItem("token")) {
      fetch(host + "/simulations", { method: "GET" })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            fetch(host + "/users", {
              method: "POST",
              body: JSON.stringify({
                token: localStorage.getItem("token"),
              }),
              headers: {
                "Content-Type": "application/json",
              },
            })
              .then((response2) => response2.json())
              .then((JsonResponse2) => {
                if (JsonResponse2["success"] === true) {
                  this.simulations = Object.values(
                    JsonResponse["simulations"]
                  ).filter((simulation) => {
                    return simulation.create_by === JsonResponse2["user"]["id"];
                  });
                  if (!this.simulations.length) {
                    this.error_simulations = "You do not have any simulations";
                  }
                } else {
                  this.$router.push("/");
                }
              })
              .catch(() => {
                this.$router.push("/");
              });
          } else if (JsonResponse["code"] === 404) {
            this.error_simulations = "You do not have any simulations";
          } else {
            this.error_simulations = JsonResponse["message"];
          }
        })
        .catch(() => {
          this.error_simulations = "Something went wrong!";
        });
    } else {
      this.$router.push("/login");
    }
  },
  methods: {
    see_simulation(id) {
      this.$router.push("/simulation/" + id);
    },
    check_change_form() {
      if (this.old_password === "") {
        this.error.list.push("Fill your old password");
      }
      if (this.new_password === "") {
        this.error.list.push("Fill your new password");
      } else if (this.old_password === this.new_password) {
        this.error.list.push("You cannot put the same password to change");
      } else if (this.password_strength !== "Strong password") {
        this.error.list.push("Password must be strong");
      }
      if (this.error.list.length) {
        this.error.show = true;
      }
      if (this.error.show === false) {
        this.changePassword();
      }
    },
    changePassword() {
      fetch(host + "/users", {
        method: "POST",
        body: JSON.stringify({
          token: localStorage.getItem("token"),
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response2) => response2.json())
        .then((JsonResponse2) => {
          if (JsonResponse2["success"] === true) {
            fetch(host + "/users/" + JsonResponse2["user"]["id"], {
              method: "PATCH",
              body: JSON.stringify({
                old_password: this.old_password,
                new_password: this.new_password,
              }),
              headers: {
                "Content-Type": "application/json",
              },
            })
              .then((response) => response.json())
              .then((JsonResponse) => {
                if (JsonResponse["success"] === true) {
                  alert("Password change successfully!");
                  this.old_password = "";
                  this.new_password = "";
                } else {
                  this.error.show = true;
                  this.error.list.push("Your old password does not match");
                }
              })
              .catch(() => {
                this.error.show = true;
                this.error.list.push("Something does not works!");
              });
          } else {
            this.$router.push("/");
          }
        })
        .catch(() => {
          this.$router.push("/");
        });
    },
    change_prof(value) {
      this.show_CPassword = value;
    },
  },
};
</script>
<style scoped>
.PROF_1 {
  min-height: 120px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.PROF_2 {
  min-height: 750px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;

  padding: 10px;
}
.buttom1 {
  padding: 6px;
  font-size: 18px;
  margin-left: 10px;
  margin-right: 10px;

  border-radius: 6px;
  cursor: pointer;
  border: none;
  color: white;
  background: #333;
}
.buttom2 {
  padding: 6px;
  font-size: 13px;
  margin-left: 10px;
  margin-right: 10px;

  border-radius: 6px;
  cursor: pointer;
  border: none;
  color: white;
  background: #333;
}
.PROFCont {
  min-width: 700px;
  height: 600px;
  padding: 15px;
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.list_sim {
  width: 100%;
  height: 600px;
  display: flex;
  flex-direction: column;
  justify-content: space-around;
  align-items: flex-start;
  overflow: scroll;
}
.list_sim::-webkit-scrollbar {
  width: 5px;
}
.list_sim::-webkit-scrollbar-thumb {
  background: rgb(47, 137, 172);
  border-radius: 5px 5px;
}
.simElem {
  width: 280px;
  height: 120px;
  padding: 10px;
  margin: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}
.menu_pass {
  width: 350px;
  height: 300px;
  padding: 20px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}
.pass_cont {
  padding: 10px;
}
</style>
