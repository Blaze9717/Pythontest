from sqlalchemy import false


class Contact:
    '''
    class that generates new contact
    '''
    pass

contact_list = []#empty array
        
def __init__(self,first_name,second_name,number,email):
    '''
    __init__ method helping us define properties for our objects
    '''
    self.first_name = first_name
    self.second_name = second_name
    self.phone_number = number
    self.email = email 
    
def delete_contact(self):
    '''
    deleting contact
    '''
    
    Contact.contact_list.remove(self)
    
def save_contact(self):
    '''
    save contact method
    '''
    
    Contact.contact_list.append(self)
    
@classmethod  #decorator
def find_by_number(cls,number):
    '''
    Method that takes in a number and returns a contact that matches that number.

        Args:
            number: Phone number to search for
        Returns :
            Contact of person that matches the number.
    '''
    for contact in cls.contact_list:
        if contact.phone_number == number:
            return contact
        
@classmethod
def contact_exists(cls,number):
    '''
    Method that checks if a contact exists from the contact list.
        Args:
            number: Phone number to search if it exists
        Returns :
            Boolean: True or false depending if the contact exists
    '''
    for contact in cls,contact_list:
        if contact.phone_number == number:
            return false

def display_contacts(self):
    '''
    method that returns all list of contacts saved
    '''
    
    self.assertEqual(Contact.display_contacts(),Contact.contact_list)
    
@classmethod
def display_contacts(cls):
    '''
    method that returns the contact list
    '''
    return cls.contact_list

    
        
    
        