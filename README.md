# Employee Management System

## Overview

The **Employee Management System** is a menu-driven Python program designed to manage basic employee information. It allows users to add employees, view employee records, filter employees by department, update salaries through hikes, and sort employees based on their names or salaries.

The project demonstrates the practical use of important Python concepts such as **lists, dictionaries, loops, conditional statements, functions/operations on collections, user input, and manual sorting algorithms**.

---

## Features

The Employee Management System provides the following options:

1. **Add Employee**

   * Adds a new employee to the system.
   * Stores the employee's ID, name, salary, and department.

2. **View All Employees**

   * Displays all employees currently stored in the system.
   * Displays a message if no employees have been added.

3. **Filter by Department**

   * Allows the user to enter a department name.
   * Displays only employees belonging to that department.
   * Displays a message if no employee is found in the selected department.

4. **Give Salary Hike**

   * Searches for an employee using their Employee ID.
   * Takes the hike percentage as input.
   * Calculates and updates the employee's new salary.

5. **Sort by Name**

   * Sorts employees alphabetically according to their names.
   * Uses a manually implemented **Bubble Sort** algorithm instead of Python's built-in sorting functions.

6. **Sort by Salary**

   * Sorts employees according to their salary in ascending order.
   * Also uses the manually implemented **Bubble Sort** algorithm.

7. **Exit**

   * Terminates the Employee Management System.

---

## Data Structure Used

The program uses a **list of dictionaries** to store employee information.

The main list is:

```python
employees = []
```

Each employee is stored as a dictionary containing four fields:

```python
{
    "id": emp_id,
    "name": name,
    "salary": salary,
    "dept": dept
}
```

### Example

```python
employees = [
    {
        "id": "E101",
        "name": "Amit",
        "salary": 40000,
        "dept": "IT"
    },
    {
        "id": "E102",
        "name": "Neha",
        "salary": 45000,
        "dept": "HR"
    }
]
```

Using dictionaries makes it easy to access individual employee information using meaningful keys such as `"id"`, `"name"`, `"salary"`, and `"dept"`.

---

## Program Workflow

The program continuously displays a menu using a `while True` loop.

The user selects an option by entering a number:

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

The selected option is processed using `if`, `elif`, and `else` statements.

The menu continues to appear until the user selects option `0`.

---

## Operations Explained

### 1. Adding an Employee

The user enters:

* Employee ID
* Employee name
* Salary
* Department

The information is stored as a dictionary and added to the `employees` list.

```python
employees.append({
    "id": emp_id,
    "name": name,
    "salary": salary,
    "dept": dept
})
```

---

### 2. Viewing Employees

The program checks whether the list is empty:

```python
if len(employees) == 0:
    print("No employees yet.")
```

If employees are present, a `for` loop is used to display each employee.

---

### 3. Filtering by Department

The user enters a department name.

The program checks every employee:

```python
if emp["dept"] == dept:
```

If the department matches, that employee is displayed.

A Boolean variable called `found` is used to determine whether at least one matching employee exists.

---

### 4. Giving a Salary Hike

The program asks for:

* Employee ID
* Hike percentage

The employee is searched using their ID.

The new salary is calculated using:

```text
New Salary = Current Salary + (Current Salary × Hike Percentage / 100)
```

For example, if an employee earns ₹40,000 and receives a 10% hike:

```text
Hike = 40000 × 10 / 100
     = 4000

New Salary = 40000 + 4000
           = 44000
```

---

### 5. Sorting by Name

The program uses **Bubble Sort** to arrange employees alphabetically by name.

The comparison is performed using:

```python
if employees[j]["name"] > employees[j + 1]["name"]:
```

If two employees are in the wrong order, their dictionary positions are swapped.

The program does not use Python's built-in `sort()` or `sorted()` functions.

---

### 6. Sorting by Salary

The same Bubble Sort technique is used to arrange employees according to salary.

The comparison is:

```python
if employees[j]["salary"] > employees[j + 1]["salary"]:
```

This produces an **ascending order**, meaning the employee with the lowest salary appears first.

---

## Algorithm

### Adding an Employee

1. Start the program.
2. Display the menu.
3. Select "Add Employee".
4. Input employee ID.
5. Input employee name.
6. Input salary.
7. Input department.
8. Create an employee dictionary.
9. Add the dictionary to the employee list.
10. Display confirmation.
11. Return to the menu.

### Filtering Employees

1. Ask the user for a department.
2. Set `found = False`.
3. Traverse the employee list.
4. Compare each employee's department with the entered department.
5. Display matching employees.
6. Set `found = True` when a match is found.
7. If no match is found, display "No employees in this department."

### Salary Hike

1. Ask for the employee ID.
2. Ask for the hike percentage.
3. Search for the employee.
4. Calculate the hike amount.
5. Add the hike amount to the current salary.
6. Display the updated salary.
7. If the employee does not exist, display "Employee not found."

### Sorting

1. Find the number of employees.
2. Compare adjacent employees.
3. If they are in the wrong order, swap them.
4. Repeat the process for all elements.
5. Continue until the list is sorted.
6. Display the sorted employees.

---

## Time Complexity

Let **n** represent the number of employees.

| Operation            | Time Complexity |
| -------------------- | --------------- |
| Add Employee         | O(1)            |
| View All Employees   | O(n)            |
| Filter by Department | O(n)            |
| Give Salary Hike     | O(n)            |
| Sort by Name         | O(n²)           |
| Sort by Salary       | O(n²)           |

### Space Complexity

The employee records require:

**O(n)** space, where `n` is the number of employees.

The Bubble Sort implementation uses only a small amount of additional temporary space, so its auxiliary space complexity is:

**O(1)**

---

## Concepts Demonstrated

This project demonstrates:

* Python lists
* Python dictionaries
* `while` loops
* `for` loops
* `if-elif-else`
* User input
* Type conversion using `float()`
* Dictionary access
* List methods
* Boolean variables
* Searching
* Updating data
* Manual Bubble Sort
* Swapping elements
* Basic time and space complexity

---

## Sample Output

```text
--- Employee Management System ---
1. Add Employee
2. View All Employees
3. Filter by Department
4. Give Salary Hike
5. Sort by Name
6. Sort by Salary
0. Exit

Choice: 1
Employee ID: E101
Name: Amit
Salary: 40000
Department: IT
Employee added.

Choice: 1
Employee ID: E102
Name: Neha
Salary: 45000
Department: HR
Employee added.

Choice: 2
{'id': 'E101', 'name': 'Amit', 'salary': 40000.0, 'dept': 'IT'}
{'id': 'E102', 'name': 'Neha', 'salary': 45000.0, 'dept': 'HR'}

Choice: 4
Enter employee ID: E101
Enter hike percentage: 10
New salary: 44000.0

Choice: 0
Exiting Employee Management System.
```

---

## Limitations

* Employee data is stored only while the program is running.
* Data is lost when the program is closed.
* There is no database or file storage.
* Employee IDs are not checked for duplicates.
* Department matching is case-sensitive.
* Salary and hike inputs are assumed to be valid numeric values.
* Bubble Sort has O(n²) time complexity and may be inefficient for very large employee lists.

---

## Future Improvements

The project can be further improved by adding:

* Employee deletion
* Employee record editing
* Duplicate Employee ID validation
* Case-insensitive department searching
* Input validation
* File handling using CSV or JSON
* Database integration
* Login/authentication
* Search by employee ID or name
* Sorting in both ascending and descending order
* Graphical User Interface (GUI)
* Employee attendance and performance information

---

## Conclusion

The Employee Management System is a beginner-friendly Python project that demonstrates how different data structures and programming concepts can be combined to create a practical application.

The use of a **list of dictionaries** makes employee records easy to store and manage, while the manually implemented **Bubble Sort** demonstrates the basic logic behind sorting algorithms without depending on Python's built-in sorting functions.
