import { mount } from "@vue/test-utils";
import ErrorView from "@/views/ErrorView.vue";

test("error-1", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.find("img").attributes().class).toContain("img-500");
});

test("error-2", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.findAll("div")).toHaveLength(2);
});

test("error-3", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.findAll("img")).toHaveLength(1);
});

test("error-4", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.findAll("h2")).toHaveLength(1);
});

test("error-5", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.find("h2").text()).toBe("404 - Resource Not Found");
});
