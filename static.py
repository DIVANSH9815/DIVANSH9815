class Employee:
    
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    def employee_info(self):
        return f"{self.name} = {self.position}"
    
    @staticmethod
    def get_info(name, position):
        current_available = ["Manager", "Cashier", "CEO"]
        if position in current_available:
            return f"{name} has a valid position: {position}"
        else:
            return f"{name} has an invalid position: {position}"

employee1 = Employee("Divansh", "CEO")
employee2 = Employee("Rohit", "Manager")
employee3 = Employee("Ravi", "Employee")

# Calling static method and passing name & position
print(Employee.get_info(employee1.name, employee1.position))
print(Employee.get_info(employee2.name, employee2.position))
print(Employee.get_info(employee3.name, employee3.position))
