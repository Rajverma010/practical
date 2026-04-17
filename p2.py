
/////u3/////
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Name": ["Raj", "Amit", "Neha", "Riya"],
    "Marks": [85, 78, 92, 88]
}

df = pd.DataFrame(data)

# Bar Chart
plt.bar(df["Name"], df["Marks"])
plt.title("Bar Chart")
plt.xlabel("Name")
plt.ylabel("Marks")
plt.show()

# Line Chart
plt.plot(df["Name"], df["Marks"], marker='o')
plt.title("Line Chart")
plt.show()

# Pie Chart
plt.pie(df["Marks"], labels=df["Name"], autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

/////u4 /////

import pandas as pd

data = {
    "Product": ["A", "B", "C"],
    "Sales": [1000, 1500, 1200],
    "Profit": [200, 300, 250]
}

df = pd.DataFrame(data)
df.to_csv("sales.csv", index=False)



import pandas as pd

data = {
    "Name": ["Raj", "Amit"],
    "Marks": [85, 78]
}

df = pd.DataFrame(data)

# CSV
df.to_csv("data.csv", index=False)

# JSON
df.to_json("data.json", orient="records", indent=4)