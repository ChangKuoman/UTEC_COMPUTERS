<template>
  <div class="contenedor_HOME">
    <div class="contenedor_app">
      <div v-if="simulation">
        <h2>YOUR BUILT PC WOULD BE:</h2>
        <img src="@/assets/img/cat_pc.jpg" />
        <div class="description_shop">
          <div class="list_shop">
            <ProductSimulation :product="simulation.motherboard" />
            <ProductSimulation
              v-for="(component, index) in simulation.components"
              :key="index"
              :product="component"
            />
          </div>
          <div>
            <p>
              <b>TOTAL PRICE: S/. {{ simulation.total_price.toFixed(2) }}</b>
            </p>
          </div>
        </div>
      </div>
      <div>
        <button class="buttom1" @click.prevent="goBack">↩ GO HOME</button>
        <button class="buttom1" @click.prevent="goSimulations">
          ↩ SIMULATIONS
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import { host } from "@/host.js";
import ProductSimulation from "@/components/ProductSimulation.vue";

export default {
  components: { ProductSimulation },
  props: {
    id: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      simulation: null,
    };
  },
  mounted() {
    if (localStorage.getItem("token")) {
      fetch(host + "/simulations/" + this.id, { method: "GET" })
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
                  if (
                    JsonResponse2["user"]["id"] !==
                    JsonResponse["simulation"]["create_by"]
                  ) {
                    this.$router.push("/");
                  } else {
                    this.simulation = JsonResponse["simulation"];
                  }
                } else {
                  this.$router.push("/");
                }
              })
              .catch(() => {
                this.$router.push("/");
              });
          } else {
            alert(JsonResponse["message"]);
            this.$router.push("/");
          }
        })
        .catch(() => {
          this.$router.push({ name: "errorPage" });
        });
    } else {
      this.$router.push("/login");
    }
  },
  methods: {
    goBack() {
      this.$router.push("/");
    },
    goSimulations() {
      this.$router.push("/profile");
    },
  },
};
</script>
<style scoped>
.buttom1 {
  padding: 5px;
  font-size: 15px;
  margin-left: 10px;
  margin-right: 10px;

  border-radius: 5px;
  cursor: pointer;
  border: none;
  color: white;
  background: #333;
}
.description_shop {
  width: auto;
  padding: 15px;
  margin-left: 18px;
  margin-top: 20px;
  margin-bottom: 20px;
  border-radius: 10px;
  box-shadow: 0 8px 15px rgba(0, 0, 0, 0.2);
}
.list_shop {
  width: auto;
  max-height: 220px;

  margin: 0;
  padding: 0;
  overflow: auto;
}
.list_shop::-webkit-scrollbar {
  width: 4px;
}
.list_shop::-webkit-scrollbar-thumb {
  background: #333;
  border-radius: 5px 5px;
}
</style>
