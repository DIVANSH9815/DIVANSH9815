class student():
    
    count = 0
    count_gpa = 0
    
    def __init__(self,name,gpa):
        self.name = name
        self.gpa = gpa
        student.count += 1
        student.count_gpa += gpa

    def get_info(self):
        return f"{self.name}={self.gpa}"
    
    @classmethod
    def _get_count(cls):
        return f"The Avrage no Of student: {cls.gpa}"
   
   
    @classmethod
    def get_count_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"{cls.count_gpa /cls.count}"
student1 = student("Ram",4.6) 
student2 = student("Divansh",7.6) 
student3 = student("Rohit",3.7) 
student4 = student("Ravi",2.7)  


print(student1.get_info())
print(student.get_count_gpa())
