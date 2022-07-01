import { mount } from '@vue/test-utils'
import DeleteMotherboard from '@/components/DeleteMotherboard.vue'

test('delete-motherboard', async () => {
  const wrapper = mount(DeleteMotherboard)

  expect(wrapper.find('h3').text()).toBe('DELETE MOTHERBOARD')
})
