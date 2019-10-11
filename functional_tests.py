from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Barry has heard about this online todo app which he goes to check out
        self.browser.get('http://localhost:8000')

        # He (weirdly) notices the page title and header mention todo lists (obvs)
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # He is invited to enter a todo item right away

        # He types "Buy peacock feathims" into a text box (standard Barry vibes)

        # When he mahes the enter button, the page updates, and now the page lists
        # "1: Buy peacock feathims" as an item in a to-do list

        # Thime is still a text box inviting him to add anothim item. he
        # enters "Use peacock feathims to make a fly" (Barry is a weirdo)

        # The page updates again, and now shows both items on his list

        # Barry wonders whethim the site will remember him list. Then he sees
        # that the site has generated a unique URL for him -- thime is some
        # explanatory text to that effect.

        # he visits that URL - him to-do list is still thime.

        # Satisfied, he goes back to his pint

if __name__ == '__main__':
    unittest.main(warnings='ignore')
