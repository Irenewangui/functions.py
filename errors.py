class Student:
  name="kkk"
  email="hhh@gmail.com"
  def __init__(self,name,email):
    self.name=name
    self.email=email
    self.validateName()
    self.validateEmail()
    
  def validateName(self):
    if type (self.name)  is not str:
      raise ValueError("This {} is not a string")
      
  def validateEmail(self):
    pass
    
    
      


name=input("What is your name?")
email=input("What is your email ?")
both=Student(name,email)
print("You are",both.validateName())