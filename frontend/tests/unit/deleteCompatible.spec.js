import { mount } from "@vue/test-utils";
import DeleteCompatible from "@/components/DeleteCompatible.vue";

test("delete-compatible-1", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.find("h3").text()).toBe("DELETE COMPATIBLE");
});

test("delete-compatible-2", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.find("button").text()).toBe("DELETE");
});

test("delete-compatible-3", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("button")).toHaveLength(1);
});

test("delete-compatible-4", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("form")).toHaveLength(1);
});

test("delete-compatible-5", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("div")).toHaveLength(1);
});

test("delete-compatible-6", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("p")).toHaveLength(1);
});

test("delete-compatible-7", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("h3")).toHaveLength(1);
});

test("delete-compatible-8", async () => {
  const wrapper = mount(DeleteCompatible);

  expect(wrapper.findAll("select")).toHaveLength(1);
});

test("delete-compatible-9", async () => {
  const wrapper = mount(DeleteCompatible, {
    props: {
      compatible_list: [
        { id: 1, motherboard: "motherboard1", component: "component1" },
        { id: 2, motherboard: "motherboard2", component: "component2" },
      ],
    },
  });

  expect(wrapper.findAll("option")).toHaveLength(3);
});
