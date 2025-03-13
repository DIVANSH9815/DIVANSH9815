class data:    
    def __init__(self,name,is_true):
        self.name = name
        self.is_true = True
	
class employee1(data):
    def __init__(self, name, is_true,employee_id,experience,salary):
        super().__init__(name, is_true)
        self.employee_id = employee_id
        self.experience = experience
        self.salary = salary

class employee2(data):
    def __init__(self, name, is_true,employee_id,experience,salary):
        super().__init__(name, is_true)
        self.employee_id = employee_id
        self.experience = experience
        self.salary = salary
  
class  employee3(data):
    def __init__(self, name, is_true,employee_id,experience,salary):
        super().__init__(name, is_true)
        self.employee_id = employee_id
        self.experience = experience
        self.salary = salary
    
        
employee_1 = employee1 (name="Divnash",is_true=True,employee_id= "back_end Developer",experience=3,salary=204433)
employee_2 = employee2(name="Rohit",is_true=False,employee_id="SoftWare_developer",experience=2,salary=124233)
employee_3 = employee3(name = "Sourav",is_true=True,employee_id="tech_maneger",experience=3,salary=123433)

print("wellcome to my company data")
print("This First employee")
print(f"Name: {employee_1.name}")
print(f"current_available : {employee_1.is_true}")
print(f"Role: {employee_1.employee_id}")
print(f"Experience: {employee_1.experience}")
print(f"Salary: {employee_1.salary}")


print("\nThis Second employee")
print(f"Name: {employee_2.name}")
print(f"current_available : {employee_2.is_true}")
print(f"Role: {employee_2.employee_id}")
print(f"Experience: {employee_2.experience}")
print(f"Salary: {employee_2.salary}")


print("\nThis Third employee")
print(f"Name: {employee_3.name}")
print(f"current_available : {employee_3.is_true}")
print(f"Role: {employee_3.employee_id}")
print(f"Experience: {employee_3.experience}")
print(f"Salary: {employee_3.salary}")

print("\nThis a data of my company employee")
