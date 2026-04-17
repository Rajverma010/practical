import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Raj", "Amit", "Neha", "Riya"],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)
plt.bar(df["Name"], df["Marks"])
plt.title("Student Marks")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

import pandas as pd
import numpy as np

# Create DataFrame 1
students = pd.DataFrame({
    "ID": [1, 2, 3],
    "Name": ["Raj", "Amit", "Neha"]
})

# Create DataFrame 2
marks = pd.DataFrame({
    "ID": [1, 2, 3],
    "Marks": [85, 78, 92]
})

# Merge DataFrames
df = pd.merge(students, marks, on="ID")
print("Merged Data:")
print(df)

# GroupBy (example: average marks)
print("\nAverage Marks:")
print(df["Marks"].mean())

# NumPy Matrix Multiplication
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

result = np.dot(a, b)
print("\nMatrix Multiplication:")
print(result)


////u2////

import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("students.db")

# Create table
conn.execute("CREATE TABLE IF NOT EXISTS students (id INT, name TEXT, marks INT)")

# Insert data
conn.execute("INSERT INTO students VALUES (1, 'Raj', 85)")
conn.commit()

# Read into Pandas
df = pd.read_sql_query("SELECT * FROM students", conn)
print("Original Data:")
print(df)

# Handle missing values
df["marks"].fillna(df["marks"].mean(), inplace=True)

print("\nCleaned Data:")
print(df)

conn.close()
