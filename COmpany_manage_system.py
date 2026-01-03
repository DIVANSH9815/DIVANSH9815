import pandas as pd

# =====================================
# DEFAULT (AUTO) EMPLOYEE DATA
# =====================================

employees_data = [
    {
        "Name": "Rahul Sharma",
        "Email": "rahul@gmail.com",
        "Phone": "9876543210",
        "DOB": "1998-05-12",
        "Location": "Delhi",
        "Position": "Developer",
        "Salary": 60000,
        "WFH": "Yes"
    },
    {
        "Name": "Anita Verma",
        "Email": "anita@gmail.com",
        "Phone": "9123456780",
        "DOB": "1997-08-22",
        "Location": "Mumbai",
        "Position": "HR",
        "Salary": 45000,
        "WFH": "No"
    }
]

# =====================================
# DEFAULT (AUTO) PROFIT & LOSS DATA
# =====================================

profits = [120000, 150000]
losses = [40000, 30000]


# =====================================
# FUNCTIONS
# =====================================

def show_employees():
    df = pd.DataFrame(employees_data)
    print("\n===== EMPLOYEE DETAILS =====\n")
    print(df)


def add_employee_manual():
    print("\n--- Add Employee (Manual) ---")

    emp = {
        "Name": input("Name: "),
        "Email": input("Gmail: "),
        "Phone": input("Phone: "),
        "DOB": input("DOB (YYYY-MM-DD): "),
        "Location": input("Location: "),
        "Position": input("Position: "),
        "Salary": int(input("Salary (INR): ")),
        "WFH": input("Work From Home (Yes/No): ")
    }

    employees_data.append(emp)
    print("Employee added successfully!")


def show_finance():
    print("\n===== COMPANY FINANCE =====")
    print("Profit entries:", profits)
    print("Loss entries  :", losses)
    print("Total Profit  :", sum(profits))
    print("Total Loss    :", sum(losses))


def add_finance_manual():
    print("\n--- Add Finance Data (Manual) ---")
    profit = int(input("Enter Profit Amount: "))
    loss = int(input("Enter Loss Amount: "))

    profits.append(profit)
    losses.append(loss)

    print("Finance data added!")


def company_summary():
    total_salary = sum(emp["Salary"] for emp in employees_data)
    total_profit = sum(profits)
    total_loss = sum(losses)

    print("\n===== COMPANY SUMMARY =====")
    print("Total Employees :", len(employees_data))
    print("Total Salary    : INR", total_salary)
    print("Total Profit    : INR", total_profit)
    print("Total Loss      : INR", total_loss)

    if total_profit > total_loss:
        print("Company Status  : PROFIT")
    else:
        print("Company Status  : LOSS")


# =====================================
# MAIN MENU
# =====================================

def main_menu():
    while True:
        print("\n==============================")
        print(" COMPANY MANAGEMENT SYSTEM ")
        print("==============================")
        print("1. View Employees (Auto + Manual)")
        print("2. Add Employee (Manual)")
        print("3. View Profit & Loss")
        print("4. Add Profit & Loss (Manual)")
        print("5. Company Summary")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            show_employees()
        elif choice == "2":
            add_employee_manual()
        elif choice == "3":
            show_finance()
        elif choice == "4":
            add_finance_manual()
        elif choice == "5":
            company_summary()
        elif choice == "6":
            print("System closed.")
            break
        else:
            print("Invalid choice!")


# =====================================
# PROGRAM START
# =====================================

main_menu()
