#!/usr/bin/env python3.9
from contact import Contact

def create_contacts(fname,lname,phone,email):
    '''
    function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

def save_contacts(self):
    '''
    saving contact
    '''
    Contact.save_contact()
    
def del_contact(self):
    '''
    Function to delete contact
    '''
    Contact.delete_contact()

def find_contact(number):
    '''
    function that finds number by contact and returns the contact
    '''
    return Contact.find_by_number(number)  
  

    