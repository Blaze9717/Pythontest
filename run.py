#!/usr/bin/env python3.9
from contact import Contact

   #creating new contact
def create_contacts(fname,lname,phone,email):
    '''
    function to create a new contact
    '''
    new_contact = Contact(fname,lname,phone,email)
    return new_contact

    #saving contact
def save_contacts(self):
    '''
    saving contact
    '''
    Contact.save_contact()
    
    #deleting contact
def del_contact(self):
    '''
    Function to delete contact
    '''
    Contact.delete_contact()

   #finding contact
def find_contact(number):
    '''
    function that finds number by contact and returns the contact
    '''
    return Contact.find_by_number(number)  
  
  #checking existing contacts
def check_existing_contacts(number):
    '''
    function that checks if a contact exists and finds it b number
    '''
    return Contact.contact_exist(number)

   #Display all contactS
def display_contacts():
    '''
    Function that returns all saved contacts
    '''
    return Contact.display_contacts()

   

    