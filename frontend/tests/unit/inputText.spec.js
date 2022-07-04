import { mount } from "@vue/test-utils";
import InputText from "@/components/InputText.vue";

test("input-text", async () => {
  const wrapper = mount(InputText, {
    props: {
      title: "Titulo",
    },
  });

  expect(wrapper.find("p").text()).toBe("Titulo");
});
