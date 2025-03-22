class Student:
    def __init__(self, name, age):
        self._name = name  # Using _name as a convention for private attributes
        self._age = age

    @property
    def name(self):  # Getter
        return self._name

    @name.setter
    def name(self, new_name):  # Setter
        if isinstance(new_name, str) and new_name.isalpha():
            self._name = new_name
        else:
            raise ValueError("Name must be a valid string")

    @name.deleter
    def name(self):  # Deleter
        print("Deleting name...")
        del self._name

# Creating an object
student = Student("Divansh", 21)

# Accessing the property using getter
print(student.name)  # Output: Divansh

# Setting a new name using setter
student.name = "Rahul"
print(student.name)  # Output: Rahul

# Deleting the name
del student.name  # Output: Deleting name...
