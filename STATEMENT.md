# Employee Management System – Problem Statement

## Problem Statement

Design and implement a **menu-driven Employee Management System using Python** to store and manage basic employee information.

The system should maintain employee records containing:

* Employee ID
* Employee Name
* Salary
* Department

The employee records should be stored using a **list of dictionaries**.

The program should provide the user with a menu containing different operations for managing employee information.

---

## Required Operations

### 1. Add Employee

The program should allow the user to enter:

* Employee ID
* Employee Name
* Salary
* Department

The entered information should be stored as a dictionary and added to the employee list.

---

### 2. View All Employees

The program should display all employee records currently stored in the system.

If there are no employee records, the program should display an appropriate message.

---

### 3. Filter by Department

The program should allow the user to enter a department name.

It should search through all employee records and display only the employees belonging to the specified department.

If no employee belongs to the entered department, the program should display an appropriate message.

---

### 4. Give Salary Hike

The program should allow the user to provide:

* Employee ID
* Salary hike percentage

The program should search for the employee using the Employee ID and calculate the updated salary using:

```text
New Salary = Current Salary + (Current Salary × Hike Percentage / 100)
```

The updated salary should then be stored in the employee's record.

If the Employee ID does not exist, the program should display an appropriate error message.

---

### 5. Sort by Name

The program should arrange all employee records in **alphabetical order according to employee name**.

The sorting operation should be implemented manually using the **Bubble Sort algorithm**.

Python's built-in `sort()` and `sorted()` functions should not be used.

---

### 6. Sort by Salary

The program should arrange employee records according to their salary in **ascending order**.

This sorting operation should also be implemented manually using the **Bubble Sort algorithm** without using built-in sorting functions.

---

### 7. Exit

The program should terminate when the user selects the Exit option.

---

## Data Structure Requirement

The program must use a **list of dictionaries**.

Example:

```python
employees = [
    {
        "id": "E101",
        "name": "Amit",
        "salary": 40000,
        "dept": "IT"
    }
]
```

The list stores multiple employee records, while each dictionary stores the details of one employee.

---

## Programming Requirements

The program should demonstrate the use of:

* Lists
* Dictionaries
* Loops
* Conditional statements
* User input
* Type conversion
* Searching
* Updating dictionary values
* Bubble Sort
* Swapping elements

The system should be **menu-driven** and continue running until the user chooses the Exit option.

---

## Expected Menu

```text
--- Employee Management System ---
1. Add Employee
2. View All Employees
3. Filter by Department
4. Give Salary Hike
5. Sort by Name
6. Sort by Salary
0. Exit
```

---

## Expected Outcome

The completed program should provide a simple command-line system through which users can:

* Add employee records
* Display employee records
* Search employees by department
* Update employee salaries
* Sort employees alphabetically
* Sort employees by salary
* Exit the application

The project should demonstrate the practical application of Python data structures and basic algorithms in a real-world management system.
