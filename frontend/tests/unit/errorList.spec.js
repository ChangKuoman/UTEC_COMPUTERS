import { mount } from '@vue/test-utils'
import ErrorList from '@/components/ErrorList.vue'

test('error-list', async () => {
  const wrapper = mount(ErrorList, {
    props: {
        error_list: ['error1', 'error2']
    }
  })

  expect(wrapper.text()).toContain('error1')
})
