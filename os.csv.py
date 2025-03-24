
import csv
import os

student = [["Name", "Age", "Skill"],
           ["Divansh", 21, "Python-developer"],
           ["Raj", 24, "Back-end-developer"],
           ["Sourav", 43, "Software-developer"]]

file_path = r"C:\Users\Divansh Sharma\OneDrive\Desktop\Desktop.csv" 

try: 
    with open(file_path,"w",newline="") as file:
        writer = csv.writer(file)
        writer.writerow(student)
        print("Exection file has been created sucessfully created {file_path}")
except Exception as e:
    print(f"Error as {e}")
    

# os part 

if os.path.exists(file_path):
    print("File has been exists in file store")
else:
    print("file has not lie")
