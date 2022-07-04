<template>
  <div class="contenedor_HOME">
    <div class="contenedor_app">
      <div class="AD_1">
        <AdminNavigator />
      </div>
      <div class="AD_2">
        <div class="AD_2_1">
          <h2>
            WHEN A MOTHERBOARD OR COMPONENT IS DELETED, COMPATIBILITIES AND
            SIMULATIONS RELATED ARE ALSO REMOVED
          </h2>
        </div>
        <div class="AD_2_2">
          <div class="AD_2_2_1">
            <div>
              <DeleteMotherboard
                v-if="!errors.motherboard.text"
                :motherboard_list="resources.motherboard_list"
                @onUpdateMotherboards="getMotherboards()"
                @onUpdateCompatibles="getCompatibles()"
              />
              <div v-if="errors.motherboard.text">
                There are no motherboards to show
              </div>

              <DeleteComponent
                v-if="!errors.component.text"
                :component_list="resources.component_list"
                @onUpdateComponents="getComponents()"
                @onUpdateCompatibles="getCompatibles()"
              />
              <div v-if="errors.component.text">
                There are no components to show
              </div>

              <DeleteCompatible
                v-if="!errors.compatible.text"
                :compatible_list="resources.compatible_list"
                @onUpdateCompatibles="getCompatibles()"
              />
            </div>
          </div>
        </div>

        <div v-if="errors.compatible.text">
          There are no compatibles to show
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { host } from "@/host.js";
import AdminNavigator from "@/components/AdminNavigator.vue";
import DeleteMotherboard from "@/components/DeleteMotherboard.vue";
import DeleteComponent from "@/components/DeleteComponent.vue";
import DeleteCompatible from "@/components/DeleteCompatible.vue";

export default {
  components: {
    AdminNavigator,
    DeleteMotherboard,
    DeleteComponent,
    DeleteCompatible,
  },
  data() {
    return {
      resources: {
        motherboard_list: [],
        component_list: [],
        compatible_list: [],
      },
      errors: {
        motherboard: {
          text: "",
          clear: () => {
            this.errors.motherboard.text = "";
          },
        },
        component: {
          text: "",
          clear: () => {
            this.errors.component.text = "";
          },
        },
        compatible: {
          text: "",
          clear: () => {
            this.errors.compatible.text = "";
          },
        },
      },
      error: false,
      error_list: [],
    };
  },
  methods: {
    getCompatibles() {
      this.errors.compatible.clear();
      fetch(host + "/compatibles", { method: "GET" })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            this.resources.compatible_list = Object.values(
              JsonResponse["compatibles"]
            );
          } else {
            this.errors.compatible.text = JsonResponse["message"];
          }
        })
        .catch(() => {
          this.errors.compatible.text = "Something went wrong!";
        });
    },
    getMotherboards() {
      this.errors.motherboard.clear();
      fetch(host + "/motherboards", { method: "GET" })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            this.resources.motherboard_list = JsonResponse["motherboards"];
          } else {
            this.errors.motherboard.text = JsonResponse["message"];
          }
        })
        .catch(() => {
          this.errors.motherboard.text = "Something went wrong!";
        });
    },
    getComponents() {
      this.errors.component.clear();
      fetch(host + "/components", { method: "GET" })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            this.resources.component_list = Object.values(
              JsonResponse["components"]
            );
          } else {
            this.errors.component.text = JsonResponse["message"];
          }
        })
        .catch(() => {
          this.errors.component.text = "Something went wrong!";
        });
    },
  },
  mounted() {
    if (localStorage.getItem("token")) {
      fetch(host + "/users", {
        method: "POST",
        body: JSON.stringify({
          token: localStorage.getItem("token"),
          admin: true,
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            this.getComponents();
            this.getCompatibles();
            this.getMotherboards();
          } else {
            this.$router.push("/");
          }
        })
        .catch(() => {
          this.$router.push("/login");
        });
    } else {
      this.$router.push("/login");
    }
  },
};
</script>
<style scoped>
.AD_1 {
  min-height: 120px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.AD_2 {
  min-height: 750px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  padding: 10px;
}
.AD_2_1 {
  width: 100%;
  height: 10%;
  text-align: center;
  display: flex;
  justify-content: center;
  align-items: center;
}
.AD_2_2 {
  width: 100%;
  height: 80%;
  display: flex;
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
}
.AD_2_2_1 {
  min-width: 500px;
  width: auto;
  height: 500px;
  padding: 20px;
  overflow: scroll;

  display: flex;
  justify-content: center;

  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}
.AD_2_2_1::-webkit-scrollbar {
  width: 7px;
}

.AD_2_2_1::-webkit-scrollbar-thumb {
  background: rgb(47, 137, 172);
  border-radius: 5px 5px;
}
</style>
