import { mount } from "@vue/test-utils";
import AdminNavigator from "@/components/AdminNavigator.vue";

test("admin-navigator-1", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("li")).toHaveLength(4);
});

test("admin-navigator-2", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("div")).toHaveLength(3);
});

test("admin-navigator-3", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("input")).toHaveLength(1);
});

test("admin-navigator-4", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("a")).toHaveLength(4);
});

test("admin-navigator-5", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("a")[0].text()).toBe("HOME ADMIN");
});

test("admin-navigator-6", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("div")[1].classes()).toContain("AdminNav");
});

test("admin-navigator-6", async () => {
  const wrapper = mount(AdminNavigator);

  expect(wrapper.findAll("div")[2].classes()).toContain("menu");
});
