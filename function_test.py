from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):

        # Kyan goes to the homepage
        self.browser.get('http://localhost:8000')

        # And the title and header shows 'To-do'
        assert 'To-Do' in self.browser.title
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)


        # He enters a todo list item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        # He inputs "buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.Enter)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1. Buy peacock feathers' for row in rows)
        )

        # He type Enter, and the pages refreshes and show: "1. buy peacock feathers"

        # There is a input area

        # He type "Make a fly"

        # Now the page shows two items

        # ............
        self.fail("To be finished...")

if __name__ == '__main__':
    unittest.main()
