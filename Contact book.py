contact={}


def display_contact():
    print("name\t\tcontact Number")
    for key in contact :
        print("{}\t\t{}".format(key,contact.get(key)))




while True:
    choice=int(input("1.Add new contact \n 2.Search contact \n 3.Display contact \n 4.Edit contact  \n 5.Delete contact \n 6.Exit \n Enter the choice \n "))
    if choice==1:
        name=input("Enter the contact name : ")
        phone=input("Enter the mobile number :  ")
        contact[name]= phone
    elif choice==2:
        search__name=input("enter the contact name ")
        if search__name in contact:
            print(search__name,"'s contact number is ",contact[search__name])
            
        else:
            print("Name is not found in contact book ")
    elif choice==3:
        if not contact:
            print("empty contact book")
        else:
            display_contact    
    elif choice==4:
        edit_contact=input("enter the contact to be edited") 
        if edit_contact in contact:
            phone=input("Enter the mobile number ")
            contact[edit_contact]=phone
            display_contact
        else:
            print("Name is not found in contact book ")
    elif choice==5:
        del_contact=input("enter the contact to be deleted ") 
        if del_contact in contact :
            confirm=input("Do you want to delete  the contact yes or no " )
            if confirm=="Y" or confirm=="y":
               contact.pop(del_contact)           
            display_contact
        else:
            print(" There the name is not found in the contact list ")
    else:
        break     
    
    
                