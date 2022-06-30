import { mount } from '@vue/test-utils'
import InputRadio from '@/components/InputRadio.vue'

test('input-radio', async () => {
  const wrapper = mount(InputRadio, {
    props: {
        title: 'Titulo'
    }
  })

  expect(wrapper.find('h2').text()).toBe('Titulo')
})
