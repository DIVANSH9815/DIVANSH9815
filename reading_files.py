# reading files .txt json and .csv
import json
import csv
file_path = "c:/Users/Divansh Sharma/OneDrive/Desktop/employee_data.csv"


try:
    with open (file_path,"r") as file:
        content = csv.reader(file)
        for line in content:
            print(line)
except FileNotFoundError:
    print("this file was not found here")
except PermissionError:
    print("you dont have a permision")
    
    
