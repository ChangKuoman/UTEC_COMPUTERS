import { mount } from "@vue/test-utils";
import LoginView from "@/views/LoginView.vue";

test("login-1", async () => {
  const wrapper = mount(LoginView);

  expect(wrapper.find("button").text()).toBe("LOGIN");
});

test("login-2", async () => {
  const wrapper = mount(LoginView);

  expect(wrapper.find("button").classes()).toContain("buttom1");
});

test("login-3", async () => {
  const wrapper = mount(LoginView);

  expect(wrapper.findAll("div")[1].classes()).toContain("contenedor_HOME");
});

test("login-4", async () => {
  const wrapper = mount(LoginView);

  expect(wrapper.findAll("div")[2].classes()).toContain("Texto_presentacion");
});
