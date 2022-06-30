import { mount } from '@vue/test-utils'
import DeleteMotherboard from '@/components/DeleteMotherboard.vue'

test('delete-motherboard', async () => {
  const wrapper = mount(DeleteMotherboard)

  expect(wrapper.find('h2').text()).toBe('DELETE MOTHERBOARD')
})
