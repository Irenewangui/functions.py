def welcome_student(name):
  welcome_str = "Hi {} welcome to Akirachix"
  return welcome_str.format(name)

name = input("Enter student name:")
print(welcome_student(name))
print(welcome_student("Jane"))
print(welcome_student("Ivy"))
print(welcome_student("Fatma"))


