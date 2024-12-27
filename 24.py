#24

class User:
  __name = None

class Salary:
  __salary = None

  def __init__(self,name,salary):
    self.__name = name
    self.__salary = salary

  def getName(self):
    return self.__name
    
  def getSalary(self):
    return self.__salary
    
users = [
	 User('john'),
	 User('eric'),
	 User('kyle'),
] 
salary = [
	 Salary('1000'),
	 Salary('1500'),
	 Salary('2000'),
] 
for user in users:
	print(user.getName())