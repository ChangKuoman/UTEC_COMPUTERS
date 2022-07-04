import { mount } from "@vue/test-utils";
import DeleteMotherboard from "@/components/DeleteMotherboard.vue";

test("delete-motherboard-1", async () => {
  const wrapper = mount(DeleteMotherboard);

  expect(wrapper.find("h3").text()).toBe("DELETE MOTHERBOARD");
});

test("delete-motherboard-2", async () => {
  const wrapper = mount(DeleteMotherboard);

  expect(wrapper.find("button").text()).toBe("DELETE");
});

test("delete-motherboard-2", async () => {
  const wrapper = mount(DeleteMotherboard);

  expect(wrapper.findAll("form")).toHaveLength(1);
});

test("delete-motherboard-3", async () => {
  const wrapper = mount(DeleteMotherboard, {
    props: {
      motherboard_list: [
        { id: 1, name: "motherboard1" },
        { id: 2, name: "motherboard2" },
      ],
    },
  });

  expect(wrapper.findAll("option")).toHaveLength(3);
});

test("delete-motherboard-4", async () => {
  const wrapper = mount(DeleteMotherboard, {
    props: {
      motherboard_list: [
        { id: 1, name: "motherboard1" },
        { id: 2, name: "motherboard2" },
      ],
    },
  });

  expect(wrapper.findAll("select")).toHaveLength(1);
});

test("delete-motherboard-5", async () => {
  const wrapper = mount(DeleteMotherboard, {
    props: {
      motherboard_list: [
        { id: 1, name: "motherboard1" },
        { id: 2, name: "motherboard2" },
      ],
    },
  });

  expect(wrapper.findAll("p")).toHaveLength(1);
});
