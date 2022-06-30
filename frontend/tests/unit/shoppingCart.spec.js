import { mount } from '@vue/test-utils'
import ShoppingCart from '@/components/ShoppingCart.vue'

test('shopping-cart', async () => {
  const wrapper = mount(ShoppingCart, {
    props: {
        total_products: [
            {'name': 'product1', 'price': 15.1},
            {'name': 'product2', 'price': 20.52}
        ],
        total_price: 35.62
    }
  })

  expect(wrapper.findAll('li')).toHaveLength(2)
})
