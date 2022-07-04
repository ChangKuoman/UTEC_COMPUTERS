import { mount } from "@vue/test-utils";
import DeleteComponent from "@/components/DeleteComponent.vue";

test("delete-component-1", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.find("h3").text()).toBe("DELETE COMPONENT");
});

test("delete-component-2", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.find("button").text()).toBe("DELETE");
});

test("delete-component-3", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("select")).toHaveLength(1);
});

test("delete-component-4", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("p")).toHaveLength(1);
});

test("delete-component-5", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("form")).toHaveLength(1);
});

test("delete-component-6", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("button")).toHaveLength(1);
});

test("delete-component-7", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("h3")).toHaveLength(1);
});

test("delete-component-8", async () => {
  const wrapper = mount(DeleteComponent);

  expect(wrapper.findAll("div")).toHaveLength(1);
});

test("delete-component-9", async () => {
  const wrapper = mount(DeleteComponent, {
    props: {
      component_list: [
        { id: 1, name: "component1" },
        { id: 2, name: "component2" },
      ],
    },
  });

  expect(wrapper.findAll("option")).toHaveLength(3);
});
