import { mount } from '@vue/test-utils'
import LoginView from '@/views/LoginView.vue'

test('login', async () => {
  const wrapper = mount(LoginView)

  expect(wrapper.find('button').text()).toBe('LOGIN')
})
