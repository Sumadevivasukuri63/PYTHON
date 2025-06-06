import functions as f
contacts={}
print("\tContacts App")

while True:
  try:
       
       
       


       print("\n\nChoices :")
       print("1. Add contact")
       print("2. View all contacts")
       print("3. Delete contact")
       print("4. Find contact")
       print("5. Edit contact")
       print("6. Exit")
       choice = int(input("Enter choice : "))

       if choice == 1:
        f.add_contact(contacts)
       elif choice == 2:
        f.view_contacts(contacts)
       elif choice == 3:
        f.delete_contact(contacts)
       elif choice == 4:
        f.find_contact(contacts)
       elif choice == 5:
        f.edit_contact(contacts)
       else:
        print("Ok bye thank you!!!")
        break
  except Exception as e:
        print(f"error is {e}")
  else:
        print("no Error is there:")
  finally:
        print("ok madam!your program is done:")
    

