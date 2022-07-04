import { mount } from "@vue/test-utils";
import RegisterView from "@/views/RegisterView.vue";

test("register-1", async () => {
  const wrapper = mount(RegisterView);

  expect(wrapper.find("button").text()).toBe("REGISTER");
});

test("register-2", async () => {
  const wrapper = mount(RegisterView);

  expect(wrapper.findAll("form")).toHaveLength(1);
});

test("register-3", async () => {
  const wrapper = mount(RegisterView);

  expect(wrapper.find("button").classes()).toContain("buttom1");
});

test("register-4", async () => {
  const wrapper = mount(RegisterView);

  expect(wrapper.findAll("div")[1].classes()).toContain("contenedor_HOME");
});
