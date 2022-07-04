import { mount } from "@vue/test-utils";
import HomeView from "@/views/HomeView.vue";

test("home-1", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.find("img").attributes().class).toContain("img-150");
});

test("home-2", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.findAll("a")).toHaveLength(1);
});

test("home-3", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.findAll("div")[2].classes()).toContain("contenedor_HOME");
});

test("home-4", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.findAll("div")[3].classes()).toContain("Texto_presentacion");
});

test("home-5", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.findAll("p")[0].text()).toContain("Our project");
});
