# Group Name: Mindstack
# Members: Estelle DuPont, Elie Antoine
# File Name: Payroll_Group_Project_Elie_Antoine.py
# Description: Payroll system for 10 employees with validation, tax calculation,
# overtime calculation, and file storage.

# -------------------------------
# CONSTANTS
# -------------------------------
STATE_TAX_RATE = 0.056
FEDERAL_TAX_RATE = 0.079
MAX_HOURS = 80
REGULAR_HOURS = 40
OVERTIME_RATE = 1.5


# -------------------------------
# MODULE 1 – EMPLOYEE INPUT
# -------------------------------
def get_employee_data():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    emp_id = input("Enter employee ID: ")
    
    dependents = int(input("Enter number of dependents: "))
    
    hours = float(input("Enter hours worked (0-80): "))
    if hours < 0 or hours > MAX_HOURS:
        print("ERROR: Invalid hours entered.")
        return None
    
    rate = float(input("Enter hourly rate: "))
    if rate <= 0:
        print("ERROR: Invalid hourly rate.")
        return None
    
    return first_name, last_name, emp_id, dependents, hours, rate


# -------------------------------
# MODULE 2 – PAYROLL CALCULATIONS
# -------------------------------
def calculate_gross(hours, rate):
    if hours <= REGULAR_HOURS:
        gross = hours * rate
    else:
        overtime_hours = hours - REGULAR_HOURS
        gross = (REGULAR_HOURS * rate) + (overtime_hours * rate * OVERTIME_RATE)
    return gross


# -------------------------------
# MODULE 3 – TAX CALCULATIONS
# -------------------------------
def calculate_taxes(gross):
    state_tax = gross * STATE_TAX_RATE
    federal_tax = gross * FEDERAL_TAX_RATE
    total_tax = state_tax + federal_tax
    net_pay = gross - total_tax
    
    return state_tax, federal_tax, net_pay


# -------------------------------
# MODULE 4 – OUTPUT & FILE STORAGE
# -------------------------------
def display_and_save(employee_data, gross, state_tax, federal_tax, net_pay):
    first_name, last_name, emp_id, dependents, hours, rate = employee_data
    
    print("\n------ PAYROLL SUMMARY ------")
    print("Employee:", first_name, last_name)
    print("Employee ID:", emp_id)
    print("Dependents:", dependents)
    print("Hours Worked:", hours)
    print("Hourly Rate:", rate)
    print("Gross Pay: $", round(gross, 2))
    print("State Tax: $", round(state_tax, 2))
    print("Federal Tax: $", round(federal_tax, 2))
    print("Net Pay: $", round(net_pay, 2))
    
    # Save to file
    with open("payroll_output.txt", "a") as file:
        file.write(f"{first_name} {last_name}, ID:{emp_id}, Gross:${gross:.2f}, Net:${net_pay:.2f}\n")


# -------------------------------
# MAIN PROGRAM
# -------------------------------
employees = []

for i in range(10):
    print(f"\nProcessing Employee {i+1}")
    
    data = get_employee_data()
    
    if data is None:
        print("Skipping invalid employee entry.")
        continue
    
    gross = calculate_gross(data[4], data[5])
    state_tax, federal_tax, net_pay = calculate_taxes(gross)
    
    display_and_save(data, gross, state_tax, federal_tax, net_pay)
    
    employees.append((data, gross, net_pay))

print("\nPayroll processing complete.")