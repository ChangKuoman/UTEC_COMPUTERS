import { mount } from '@vue/test-utils'
import FooterComponent from '@/components/FooterComponent.vue'

test('footer', async () => {
  const wrapper = mount(FooterComponent)

  expect(wrapper.find('img').attributes().class).toContain('img-200')
})
