import { mount } from "@vue/test-utils";
import HomeView from "@/views/HomeView.vue";

test("home", async () => {
  const wrapper = mount(HomeView);

  expect(wrapper.find("img").attributes().class).toContain("img-150");
});
