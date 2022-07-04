import { mount } from "@vue/test-utils";
import ErrorView from "@/views/ErrorView.vue";

test("home", async () => {
  const wrapper = mount(ErrorView);

  expect(wrapper.find("img").attributes().class).toContain("img-500");
});
