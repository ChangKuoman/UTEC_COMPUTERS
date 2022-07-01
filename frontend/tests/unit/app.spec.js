import { mount } from '@vue/test-utils'
import navComponent from '@/App.vue'

test('nav-component', async () => {
  const wrapper = mount(navComponent)

  expect(wrapper.findAll('nav')).toHaveLength(1)
})
