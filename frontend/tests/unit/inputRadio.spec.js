import { mount } from "@vue/test-utils";
import InputRadio from "@/components/InputRadio.vue";

test("input-radio-1", async () => {
  const wrapper = mount(InputRadio, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.find("h4").text()).toBe("Titulo");
});

test("input-radio-2", async () => {
  const wrapper = mount(InputRadio, {
    props: {
      title: "Titulo",
      objects: [
        {
          name: "product1",
          description: "description1",
          price: 15.8
        },
        {
          name: "product2",
          description: "description2",
          price: 48.5
        }
      ],
      modelValue: {
        name: "product1",
        description: "description1",
        price: 15.8
      }
    },
  });

  expect(wrapper.findAll("li")).toHaveLength(2);
});
