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


#MAIN FUNCTION
def main():
    print("Hallow welcome to my portal.What is your name?")
    user_name = input()
    
    print(f"Hello {user_name}. What would you like to do?")
    print('\n')
    
    while True:
        print("Use these short codes : cc - create a new contact, dc - display contacts, fc -find a contact, ex -exit the contact list ")
        
        short_code = input().lower()
        if short_code == 'cc':
            print("New contact")
            print('-'*10)
            
            print ("First name")
            f_name = input()
            
            print("last name")
            l_name =input()
            
            print ("phonenumber")
            p_number = input()
            
            print ("Email address")
            e_address = input()
            
            save_contacts(create_contacts(f_name,l_name,p_number,e_address))# create and save new contact.
            print ('\n')
            print(f"New Contact {f_name} {l_name} created")
            print ('\n')
            
        elif short_code == 'dc':
            if display_contacts():
                print("Here is a list of all your contacts")
                print('\n')
                

                for contact in display_contacts():
                        print(f"{contact.first_name} {contact.last_name} .....{contact.phone_number}")

                print('\n')
            else:
                print('\n')
                print("You dont seem to have any contacts saved yet")
                print('\n')
        
        elif short_code == 'fc':
    
            print("Enter the number you want to search for")

            search_number = input()
            if check_existing_contacts(search_number):
                    search_contact = find_contact(search_number)
                    print(f"{search_contact.first_name} {search_contact.last_name}")
                    print('-' * 20)

                    print(f"Phone number.......{search_contact.phone_number}")
                    print(f"Email address.......{search_contact.email}")
            else:
                print("That contact does not exist")
           
        elif short_code == "ex":
            print("Bye .......")
            break
        else:
            print("I really didn't get that. Please use the short codes")      

if __name__ == '__main__':
    main()
    
    