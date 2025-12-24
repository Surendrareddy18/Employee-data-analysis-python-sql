

import sqlite3
import matplotlib.pyplot as plt

conn = sqlite3.connect("employees.db")
cursor = conn.cursor()

# Total number of employees
cursor.execute("SELECT COUNT(*) FROM employees")
total_employees = cursor.fetchone()[0]

# Average salary
cursor.execute("SELECT AVG(salary) FROM employees")
avg_salary = cursor.fetchone()[0]

# Department-wise employee count
cursor.execute("""
SELECT department, COUNT(*) 
FROM employees 
GROUP BY department
""")
dept_counts = cursor.fetchall()

conn.close()

print("EMPLOYEE DATA ANALYSIS REPORT")
print("-----------------------------")
print("Total Employees:", total_employees)
print("Average Salary:", round(avg_salary, 2))

print("\nEmployees per Department:")
for dept, count in dept_counts:
    print(dept, ":", count)

# --------- MATPLOTLIB VISUALIZATION ---------
departments = [dept for dept, count in dept_counts]
counts = [count for dept, count in dept_counts]

plt.bar(departments, counts)
plt.xlabel("Department")
plt.ylabel("Number of Employees")
plt.title("Employees per Department")
plt.show()
