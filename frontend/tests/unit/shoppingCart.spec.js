import { mount } from "@vue/test-utils";
import ShoppingCart from "@/components/ShoppingCart.vue";

test("shopping-cart-1", async () => {
  const wrapper = mount(ShoppingCart, {
    props: {
      total_products: [
        { name: "product1", price: 15.1 },
        { name: "product2", price: 20.52 },
      ],
      total_price: 35.62,
    },
  });

  expect(wrapper.findAll("li")).toHaveLength(2);
});

test("shopping-cart-2", async () => {
  const wrapper = mount(ShoppingCart, {
    props: {
      total_products: [
        { name: "product1", price: 17.1 },
      ],
      total_price: 17.1,
    },
  });

  expect(wrapper.find("p").text()).toContain("17.10");
});

test("shopping-cart-3", async () => {
  const wrapper = mount(ShoppingCart, {
    props: {
      total_products: [
        { name: "product1", price: 17.1 },
        { name: "product2", price: 20.87}
      ],
      total_price: 37.97,
    },
  });

  expect(wrapper.findAll("span")).toHaveLength(2);
});

test("shopping-cart-4", async () => {
  const wrapper = mount(ShoppingCart, {
    props: {
      total_products: [
        { name: "product1", price: 17.1 },
        { name: "product2", price: 20.87}
      ],
      total_price: 37.97,
    },
  });

  expect(wrapper.find("button").text()).toBe("SIMULATE!");
});
