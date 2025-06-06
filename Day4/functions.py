def add_contact(contacts):
    name = input("Enter Contact Name :")
    mobile = int(input("Enter mobile number :"))
    contacts[name] = mobile
    file=open("./data.txt" ,"a")
    file.write(f"{name}:{mobile}\n")
    file.close()


def view_contacts(contacts):
    print("\n")
    #for i in contacts:
       # print(f"{i} : {contacts[i]}")
    file=open("./data.txt" ,"r")
    contacts=file.readlines()
    for item in contacts:
        name,mobile=item.split(":")
        print(f"name:{name} , mobile:{mobile}")
    file.close()

def delete_contact(contacts):
    name_to_delete = input("Enter contact name to delete :")
    del contacts[name_to_delete]
    print("deleted contact " , name_to_delete)
    file=open("./data.txt" , "r")
    for value in contacts:
        name,mobile=value.split(":")
    file.close()
    file=open("./data.txt" , "w")
    for name,mobile in contacts.value():
        file.write(f"{name}:{mobile}\n") 
    file.close()   

 
def find_contact(contacts):
    name_to_find = input("Enter name to Find :").lower()
    print(f"{name_to_find} : {contacts[name_to_find]}")
    found=False
    file=open("./data.txt" ,"r")
    for value in file:
        if find_contact in value.lower():
            name,mobile=value.split(":")
            print(f"name:{name},mobile:{mobile}")
            found=True
            break
        if not found:
            print("contact not found:")
    file.close()

def edit_contact(contacts):
    name_to_edit = input("Enter contact name to edit :")
    number = (input("Enter new number: "))
    contacts[name_to_edit] = number
    print("Edited contact : " , name_to_edit)
    file=open("./data.txt" ,"r")

