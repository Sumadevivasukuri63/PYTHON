def add_student(gradebook):
    name=input("Enter name of the student:")
    marks=input("Enter marks separated spaces:")
    mark_list=list(map(int, marks.split()))
    gradebook[name]= mark_list
    print(f"{name} student added.")
def view_student(gradebook):
    if  not  gradebook:
        print("no students found:")
        return
    print("..students")
    for name,marks in gradebook.items():
        avg = sum(marks) / len(marks)
        print(f"{name} - Marks : {marks} | Avg:{avg}")
def update_student(gradebook):
    name=input("Enter name to update marks:")
    if name in gradebook:
      marks=input("Enter marks separated spaces:")
      mark_list=list(map(int, marks.split()))
      gradebook[name]=mark_list
      print(f"{name} marks updated")
    else:
        print("student not found:")
def search_student(gradebook):
    search_name=input("Enter name to search:").lower()
    found=False
    for name,marks in gradebook.items():
        if search_name in name.lower():
             avg = sum(marks) / len(marks)
             print(f"found:{name} - marks:{marks} | Avg:{avg}")
             found=True
        else:
            print("student not found:")
def remove_student(gradebook):
    name=input("Enter name to remove:")
    if name  in gradebook:
        del gradebook[name]
        print(f"{name} removed from the gradebook:")
    else:
        print("student not found:")





