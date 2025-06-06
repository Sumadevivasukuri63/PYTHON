import func as fun
gradebook={}

while True:
    print("choices:")
    print("1.add student:")
    print("2.view student:")
    print("3.update student:")
    print("4.search student:")
    print("5.remove student:")
    print("6.Exit:")
    choice=int(input("Enter choice:"))

    if choice==1:
        fun.add_student(gradebook)
    elif choice==2:
        fun.view_student(gradebook)
    elif choice==3:
        fun.update_student(gradebook)
    elif choice==4:
        fun.search_student(gradebook)
    elif choice==5:
        fun.remove_student(gradebook)
    elif choice==6:
        print("...Exiting..:")
    else:
        print("Thank you:")
        break

    