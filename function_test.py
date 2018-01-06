from selenium import webdriver
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

        # He enters a todo list item

        # He inputs "buy peacock feathers"

        # He type Enter, and the pages refreshes and show: "1. buy peacock feathers"

        # There is a input area

        # He type "Make a fly"

        # Now the page shows two items

        # ............


if __name__ == '__main__':
    unittest.main()
