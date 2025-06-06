class Person:
  def __init__(self, name , age):
    self.name = name
    self.age= age

  def change_name(self, new_name):
    self.name =new_name 

  def show_name(self):
    print(f"My name is {self.name}")

  def __str__(self):
    return f"{self.new_name}"

p1=Person("siri",20)
print(p1.name)
print(p1.age)
p1.name="suma"
print(p1.name)
p1.show_name()

