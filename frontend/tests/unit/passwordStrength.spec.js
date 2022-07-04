import { mount } from "@vue/test-utils";
import PasswordStrength from "@/components/PasswordStrength.vue";

test("password-strength", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "aA.12345",
    },
  });

  expect(wrapper.find("p").text()).toBe("Strong password");
});
