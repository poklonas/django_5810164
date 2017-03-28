from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()
    '''
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])
    '''
    def test_can_go_to_accounting_app(self):
        # Alan has heard about a cool new accounting app. He goes
        # to check out its homepage
        
        self.browser.get('http://localhost:8000')

        # He notices the page title mention Homepage
        self.assertIn('Home Page', self.browser.title)
        # He notices the page header mention All APP
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('All APP', header_text)
        # He saw a Accounting Link 
        a_link_text = self.browser.find_elements_by_tag_name('a')
        self.assertIn('Accounting', [row.text for row in a_link_text]) 

        # He click accounting link to access accounting web app
        accounting_link = self.browser.find_element_by_link_text("Accounting")
        accounting_link.click()

        time.sleep(0.5)   
        # He notices the page title mention Ledger App
        self.assertIn('Ledger App', self.browser.title)
        # He notices the page header mention Welcome
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Welcome', header_text)


    def test_can_go_to_add_user_page(self):
        #after alan has come to accounting app page
        self.browser.get('http://localhost:8000/accounting/')

        #he saw a link name ADD NEW USER
        a_link_text = self.browser.find_elements_by_tag_name('a')
        self.assertIn('ADD NEW USER', [row.text for row in a_link_text]) 

        # then he want to add new user page , he click that link
        accounting_link = self.browser.find_element_by_link_text("ADD NEW USER")
        accounting_link.click()

        time.sleep(0.5)
        #He notices the page title mention ADD NEW USER 
        self.assertIn('ADD NEW USER', self.browser.title)
        # He notices the page header mention Add new User
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Add new User', header_text)
        
        # He fill input box for a user name is " Alan "
        inputbox = self.browser.find_element_by_name('user_name')
        inputbox.send_keys('Alan')
        # He click enter to make new user
        # He found this browser turn to main web app page
        # He saw new user , name alan
        
        time.sleep(1)

        # He click his username
        # This browser turn to user page
        # Title is "alan"
        # and he want to create new pass book 
        # he saw a link tap name ADD NEW PASS_BOOK
        # he click on it
        # This browser turn to add_book_page
        # title is Add_Pass_Book
        # he fill pass_book_name , pass_book_name is "ATM" and then click enter
        # this browser turn to user page
        # he saw new pass_book in the lists
        # he click in that link
        
        # thie browser turn to pass_book page
        # he saw title is " alan : ATM "
        # he saw the balance of this book is 0
        # he saw a link tap name Add new List , and he want to create a new list for this pass_book
        # he clikc on it
        # thie browser turn to Add list page
        # title is "add list : ATM : Alan"

        # he fill imformation 
        # list name is "Daddy give some money"
        # detail is "that money for buy a car"
        # value is "50000"
        # type is "given"
        # date is "2017-03-18"
        # type for income

        # he click enter
        # this browser turn to pass_book detail page
        # and he saw a balance turn to 50000.0
        # he want to check history in that day (2017-03-18_)
        # he fill input in select date is 2017-03-18
        # then he click show list in date button
        # then the table below show the list , List name in the first row is Dad
        # and Type in first row is given 
        # and income in first row is 50000.0
        # and expenses is -
          
        # but he want to delete it because he want to change a value and detail of this
        # he saw a link tap name 	Delete List
        # he click on it
        # this browser turn to a DeleteLIstPage 
        # he saw a list and the date for each list and the delete button for each list
        # he click delete button in row the same of list name "Daddy give some money
        # thie browser refresh
        # and that list dispear !!!!!!
        # then he saw a link tap name Back to book menu 
        # he want to back a pass book page , he click to that link
        # this browser turn to pass book detail page
        # he saw balance is turn to 0.0
        # and the list is dispear in that day



        



    '''
        # He selects Accounting 
        # 
        # She is invited to enter a to-do item straight away
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        inputbox.send_keys('Buy peacock feathers')

    # When she hits enter, the page updates, and now the page lists
    # "1: Buy peacock feathers" as an item in a to-do list table
        inputbox.send_keys(Keys.ENTER)
        self.check_for_row_in_list_table('1: Buy peacock feathers')

    # There is still a text box inviting her to add another item. She
    # enters "Use peacock feathers to make a fly" (Edith is very
    # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

    # The page updates again, and now shows both items on her list
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

    # Edith wonders whether the site will remember her list. Then she sees


        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])

       # There is still a text box inviting her to add another item. She
        # enters "Use peacock feathers to make a fly" (Edith is very
        # methodical)
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

    # The page updates again, and now shows both items on her list
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        self.assertIn(
            '2: Use peacock feathers to make a fly' ,
             [row.text for row in rows]
        )

    # Edith wonders whether the site will remember her list. Then she sees
    # that the site has generated a unique URL for her -- there is some
    # explanatory text to that effect.
        self.fail('Finish the test!')

    # She visits that URL - her to-do list is still there.


'''


if __name__ == '__main__':  #7
    unittest.main(warnings='ignore')  #8
