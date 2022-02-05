from contact import Contact
import unittest #model that helps in running the test

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
    
    
if __name__ == '__main__':
    unittest.main()
