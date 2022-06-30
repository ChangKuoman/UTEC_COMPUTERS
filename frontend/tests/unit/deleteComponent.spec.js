import { mount } from '@vue/test-utils'
import DeleteComponent from '@/components/DeleteComponent.vue'

test('delete-component', async () => {
  const wrapper = mount(DeleteComponent)

  expect(wrapper.find('h2').text()).toBe('DELETE COMPONENT')
})
