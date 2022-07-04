import { mount } from "@vue/test-utils";
import PasswordStrength from "@/components/PasswordStrength.vue";

test("password-strength-1", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "aA.12345",
    },
  });

  expect(wrapper.find("p").text()).toBe("Strong password");
});

test("password-strength-2", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "aA.12345",
    },
  });

  expect(wrapper.find("b").text()).toBe("Strong password");
});

test("password-strength-3", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "aA.12345",
    },
  });

  expect(wrapper.findAll("p")).toHaveLength(1);
});

test("password-strength-4", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "aA.12345",
    },
  });

  expect(wrapper.findAll("b")).toHaveLength(1);
});

test("password-strength-5", async () => {
  const wrapper = mount(PasswordStrength, {
    props: {
      password: "password",
    },
  });

  expect(wrapper.find("p").text()).toBe("Very weak password");
});
