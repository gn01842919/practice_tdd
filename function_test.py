from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        # self.browser = webdriver.Firefox()
        self.browser = webdriver.PhantomJS(executable_path='C:\\Program Files\\phantomjs-2.1.1-windows\\bin\\phantomjs.exe')

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        print(rows)
        self.assertIn(row_text, [row.text for row in rows])

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

        # He type Enter, and the pages refreshes and show: "1. buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')

        # There is a input area
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('make a fly')
        inputbox.send_keys(Keys.ENTER)

        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: may a fly')



        # He type "Make a fly"

        # Now the page shows two items

        # ............
        self.fail("To be finished...")

if __name__ == '__main__':
    unittest.main()
