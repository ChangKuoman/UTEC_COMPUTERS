import { mount } from '@vue/test-utils'
import ProductSimulation from '@/components/ProductSimulation.vue'

test('product-simulation', async () => {
  const wrapper = mount(ProductSimulation, {
    props: {
        product: {
            name: 'producto',
            price: 15.7
        }
    }
  })

  expect(wrapper.text()).toContain('15.70')
})
