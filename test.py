from contact import Contact
import unittest #model that helps in running the test
import pyperclip

class TestContact(unittest.TestCase):
    '''
    test class that defines test case
    '''

def setUp(self):
    '''
    setup method to run before each test
    '''
    self.new_contact = Contact("James","Muriuki","0702901315","shawnnjoga@gmail.com")
    
    #FIRST-TEST
def test_init(self):
    '''
    checking if the objects are initialized correctly
    '''
    self.assertEqual(self.new_contact.first_name,"James")
    self.assertEqual(self.new_contact.second_name,"Muriuki")
    self.asserEqual(self.new_contact.phone_number,"0702901315")
    self.assertEqual(self.new_contact.email,"shawnnjoga@gmail.com") 
    
    #SECOND-TEST(SAVING )
def test_save_contact(self):
    '''
    test for saving a contact
    '''
    self.new_contact.save_contact()#how we save 
    self.asserEqual(len(Contact.contact_list),1) 
    
    #THIRD-TEST(SAVINGMULTIPLECONTACT)
def test_save_multiple_contact(self):
    '''
    saving multiple contacts
    '''
    self.new_contact.save_contact()
    test_contact = Contact("Test","User","0722348613","test@gmail.com")
    test_contact.save_contact()
    self.assertEqual(len(Contact.contact_list),2)
    
    #(tearDown method that does clean up after each test case has run.)
def tearDown(self):
    '''
    tearDown method that does clean up after each test case has run.
    '''
    Contact.contact_list = []

    #FOURTH-TEST(DELETING)
def test_delete_contact(self):
    '''
    method that delets contacts
    '''
    self.new_contact.save_contact()
    test_contact = Contact("Test","User","0722348613","test@gmail.com")
    test_contact.save_contact()
    
    self.new_contact.delete_contact()#deleting a contact
    self.assertEqual(len(Contact.contact_list),1)
    
def test_contact_exist(self):
    '''method to test i a contact exits
    '''
    self.new_contact.save_contact()
    test_contact = Contact("Test","User","0722348613","test@gmail.com")
    test_contact.save_contact()
    
    contact_exists = Contact.contact_exists("0722348613")
    
    self.assertTrue(contact_exists)
    
def test_copy_email(self):
    '''
    Test to confirm that we are copying the email address from a found contact
    '''
    self.new_contact.save_contact()
    Contact.copy_email("0702901315")
    self.assertEqual(self.new_contact.email,pyperclip.paste())
    
    
    
    
if __name__ == '__main__':
    unittest.main()
