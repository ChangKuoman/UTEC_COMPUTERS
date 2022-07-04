import { mount } from "@vue/test-utils";
import InputText from "@/components/InputText.vue";

test("input-text-1", async () => {
  const wrapper = mount(InputText, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.find("p").text()).toBe("Titulo");
});

test("input-text-2", async () => {
  const wrapper = mount(InputText, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.findAll("p")).toHaveLength(1);
});

test("input-text-3", async () => {
  const wrapper = mount(InputText, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.findAll("div")).toHaveLength(1);
});

test("input-text-4", async () => {
  const wrapper = mount(InputText, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.findAll("input")).toHaveLength(1);
});
