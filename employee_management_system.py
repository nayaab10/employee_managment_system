

employees = []  # list of dicts {"id":, "name":, "salary":, "dept":}

while True:
    print("\n--- Employee Management System ---")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Filter by Department")
    print("4. Give Salary Hike")
    print("5. Sort by Name")
    print("6. Sort by Salary")
    print("0. Exit")
    ch = input("Choice: ")

    if ch == "1":
        emp_id = input("Employee ID: ")
        name = input("Name: ")
        salary = float(input("Salary: "))
        dept = input("Department: ")
        employees.append({"id": emp_id, "name": name, "salary": salary, "dept": dept})
        print("Employee added.")

    elif ch == "2":
        if len(employees) == 0:
            print("No employees yet.")
        for emp in employees:
            print(emp)

    elif ch == "3":
        dept = input("Enter department to filter: ")
        found = False
        for emp in employees:
            if emp["dept"] == dept:
                print(emp)
                found = True
        if not found:
            print("No employees in this department.")

    elif ch == "4":
        emp_id = input("Enter employee ID: ")
        hike_percent = float(input("Enter hike percentage: "))
        updated = False
        for emp in employees:
            if emp["id"] == emp_id:
                emp["salary"] = emp["salary"] + (emp["salary"] * hike_percent / 100)
                updated = True
                print("New salary:", emp["salary"])
        if not updated:
            print("Employee not found.")

    elif ch == "5":
        # Manual bubble sort by name
        n = len(employees)
        for i in range(n):
            for j in range(0, n - i - 1):
                if employees[j]["name"] > employees[j + 1]["name"]:
                    temp = employees[j]
                    employees[j] = employees[j + 1]
                    employees[j + 1] = temp
        print("Sorted by name:")
        for emp in employees:
            print(emp)

    elif ch == "6":
        n = len(employees)
        for i in range(n):
            for j in range(0, n - i - 1):
                if employees[j]["salary"] > employees[j + 1]["salary"]:
                    temp = employees[j]
                    employees[j] = employees[j + 1]
                    employees[j + 1] = temp
        print("Sorted by salary:")
        for emp in employees:
            print(emp)

    elif ch == "0":
        print("Exiting Employee Management System.")
        break
    else:
        print("Invalid choice.")
