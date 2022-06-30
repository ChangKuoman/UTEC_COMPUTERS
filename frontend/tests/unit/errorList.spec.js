import { mount } from '@vue/test-utils'
import ErrorList from '@/components/ErrorList.vue'

test('error-list', async () => {
  const wrapper = mount(ErrorList, {
    props: {
        error_list: ['error1', 'error2']
    }
  })

  //await wrapper.get('[data-test="new-todo"]').setValue('New todo')
  //await wrapper.get('[data-test="form"]').trigger('submit')

  expect(wrapper.text()).toContain('error1')
})
