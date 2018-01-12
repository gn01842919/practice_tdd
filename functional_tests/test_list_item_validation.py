from selenium.webdriver.common.keys import Keys
from .base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):

        # Input an empty item
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # An error msg appears
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item!")

        # Input a valid item, it works
        self.browser.find_element_by_id('id_new_item').send_keys('Buy milk\n')
        self.wait_for_row_in_list_table('1: Buy milk')

        # Input an empty item again
        self.browser.find_element_by_id('id_new_item').send_keys(Keys.ENTER)

        # Get warning again
        self.wait_for_row_in_list_table('1: Buy milk')
        error = self.browser.find_element_by_css_selector('.has-error')

        self.assertEqual(error.text, "You can't have an empty list item!")

        # She can fix it
        self.browser.find_element_by_id('id_new_item').send_keys('Make tea\n')
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')

        self.browser.find_element_by_css_selector('.has-error')
