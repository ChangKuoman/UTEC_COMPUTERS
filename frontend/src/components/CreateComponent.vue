<template>
  <div>
    <h2>CREATE COMPONENT</h2>
    <form @change="clearError()">
      <InputText v-model="name" title="COMPONENT NAME" type="text" />
      <InputText
        v-model="description"
        title="COMPONENT DESCRIPTION"
        type="text"
      />
      <p>COMPONENT TYPE</p>
      <select v-model="type">
        <option value="" hidden selected>SELECT AN OPTION</option>
        <option value="RAM">RAM (Random Access Memory)</option>
        <option value="SSD">SSD (Solid State Drive)</option>
        <option value="HDD">HDD (Hard Drive Disk)</option>
        <option value="CPU">CPU (Central Processing Unit)</option>
        <option value="GPU">GPU (Graphics Processing Unit)</option>
        <option value="PSU">PSU (Power Supply Unit)</option>
        <option value="PC Cooling">PC Cooling</option>
        <option value="Peripheral">Peripheral</option>
      </select>
      <InputText
        v-model="price"
        title="COMPONENT PRICE"
        type="number"
        step="0.01"
      />
      <button
        @click.prevent="
          clearError();
          checkFormComponent();
        "
      >
        CREATE
      </button>
    </form>
    <ErrorList class="no-dots" v-if="error" :error_list="error_list" />
  </div>
</template>

<script>
import { host } from "@/host.js";
import InputText from "@/components/InputText.vue";
import ErrorList from "@/components/ErrorList.vue";

export default {
  name: "CreateComponent",
  components: { InputText, ErrorList },
  data() {
    return {
      name: "",
      description: "",
      price: 0,
      type: "",
      error_list: [],
      error: false,
    };
  },
  methods: {
    clearError() {
      this.error_list = [];
      this.error = false;
    },
    checkFormComponent() {
      if (this.name === "") {
        this.error_list.push("Component name is required.");
      }
      if (this.description === "") {
        this.error_list.push("Component description is required");
      }
      if (this.type === "") {
        this.error_list.push("Component type is required");
      }
      if (this.price === 0) {
        this.error_list.push("Component price cannot de 0");
      } else if (this.price < 0) {
        this.error_list.push("Component price cannot be negative");
      }
      if (this.error_list.length) {
        this.error = true;
      }
      if (this.error === false) {
        this.createComponent();
      }
    },
    createComponent() {
      fetch(host + "/components", {
        method: "POST",
        body: JSON.stringify({
          name: this.name,
          description: this.description,
          price: this.price,
          type: this.type,
          token: localStorage.getItem("token"),
        }),
        headers: {
          "Content-Type": "application/json",
        },
      })
        .then((response) => response.json())
        .then((JsonResponse) => {
          if (JsonResponse["success"] === true) {
            const components_array = Object.values(JsonResponse["components"]);
            this.$emit("update:modelValue", [
              ...components_array.filter(
                (component) => component.component_type === "RAM"
              ),
              ...components_array.filter(
                (component) => component.component_type === "SSD"
              ),
              ...components_array.filter(
                (component) => component.component_type === "GPU"
              ),
              ...components_array.filter(
                (component) => component.component_type === "PC Cooling"
              ),
            ]);
            this.name = "";
            this.description = "";
            this.price = 0;
            this.type = "";
            alert("COMPONENT ADDED SUCCESSFULLY");
          } else {
            this.error = true;
            this.error_list.push(JsonResponse["message"]);
          }
        })
        .catch(() => {
          this.error = true;
          this.error_list.push("Something went wrong!");
        });
    },
  },
};
</script>
