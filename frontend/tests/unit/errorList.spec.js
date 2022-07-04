import { mount } from "@vue/test-utils";
import ErrorList from "@/components/ErrorList.vue";

test("error-list-1", async () => {
  const wrapper = mount(ErrorList, {
    props: {
      error_list: ["error1", "error2"],
    },
  });

  expect(wrapper.text()).toContain("error1");
});

test("error-list-2", async () => {
  const wrapper = mount(ErrorList, {
    props: {
      error_list: ["error1", "error2"],
    },
  });

  expect(wrapper.findAll("ul")).toHaveLength(1);
});

test("error-list-3", async () => {
  const wrapper = mount(ErrorList, {
    props: {
      error_list: ["error1", "error2"],
    },
  });

  expect(wrapper.findAll("li")).toHaveLength(2);
});

test("error-list-4", async () => {
  const wrapper = mount(ErrorList, {
    props: {
      error_list: ["error1", "error2"],
    },
  });

  expect(wrapper.findAll("li")[0].text()).toBe("error1");
});
