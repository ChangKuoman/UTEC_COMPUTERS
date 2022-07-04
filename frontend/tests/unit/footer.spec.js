import { mount } from "@vue/test-utils";
import FooterComponent from "@/components/FooterComponent.vue";

test("footer-1", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.find("img").attributes().class).toContain("img-200");
});

test("footer-2", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("div")).toHaveLength(3);
});

test("footer-3", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("img")).toHaveLength(2);
});

test("footer-4", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("h3")).toHaveLength(2);
});

test("footer-5", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("footer")).toHaveLength(1);
});

test("footer-6", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("h3")[0].text()).toBe("PARTNERS:");
});

test("footer-7", async () => {
  const wrapper = mount(FooterComponent);

  expect(wrapper.findAll("p")[0].text()).toContain("Chang");
});
