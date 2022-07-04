import { mount } from "@vue/test-utils";
import DeleteComponent from "@/components/DeleteComponent.vue";

test("delete-component", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.find("h3").text()).toBe("DELETE COMPONENT");
});
