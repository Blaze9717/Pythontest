class Contact:
    '''
    class that generates new contact
    '''
    pass

contact_list = []#empty array

def save_contact(self):
    '''
    save contact method
    '''
    
    Contact.contact_list.append(self)
    
def delete_contact(self):
    '''
    deleting contact
    '''
    
    Contact.contact_list.remove(self)
    
    
def __init__(self,first_name,second_name,number,email):
    '''
    __init__ method helping us define properties for our objects
    '''
    self.first_name = first_name
    self.second_name = second_name
    self.phone_number = number
    self.email = email 
    
    