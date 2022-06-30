import { mount } from '@vue/test-utils'
import DeleteCompatible from '@/components/DeleteCompatible.vue'

test('delete-compatible', async () => {
  const wrapper = mount(DeleteCompatible)

  expect(wrapper.find('h2').text()).toBe('DELETE COMPATIBLE')
})
