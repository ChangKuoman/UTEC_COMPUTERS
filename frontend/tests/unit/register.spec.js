import { mount } from '@vue/test-utils'
import RegisterView from '@/views/RegisterView.vue'

test('register', async () => {
  const wrapper = mount(RegisterView)

  expect(wrapper.find('button').text()).toBe('REGISTER')
})
