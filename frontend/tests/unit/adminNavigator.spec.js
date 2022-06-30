import { mount } from '@vue/test-utils'
import AdminNavigator from '@/components/AdminNavigator.vue'

test('error-list', async () => {
  const wrapper = mount(AdminNavigator)

  expect(wrapper.findAll('li')).toHaveLength(4)
})
