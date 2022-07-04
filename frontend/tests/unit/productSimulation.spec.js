import { mount } from "@vue/test-utils";
import ProductSimulation from "@/components/ProductSimulation.vue";

test("product-simulation-1", async () => {
  const wrapper = mount(ProductSimulation, {
    props: {
      product: {
        name: "producto",
        price: 15.7,
      },
    },
  });

  expect(wrapper.text()).toContain("15.70");
});

test("product-simulation-2", async () => {
  const wrapper = mount(ProductSimulation, {
    props: {
      product: {
        name: "producto",
        price: 10.0,
      },
    },
  });

  expect(wrapper.findAll("div")).toHaveLength(1);
});

test("product-simulation-3", async () => {
  const wrapper = mount(ProductSimulation, {
    props: {
      product: {
        name: "producto",
        price: 10.0,
      },
    },
  });

  expect(wrapper.findAll("p")).toHaveLength(1);
});

test("product-simulation-4", async () => {
  const wrapper = mount(ProductSimulation, {
    props: {
      product: {
        name: "producto",
        price: 10.0,
      },
    },
  });

  expect(wrapper.find("div").classes()).toHaveLength(0);
});
