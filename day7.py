import pandas as pd

# Sample dataset
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Marks": [78, 85, 62, 90, 71]
}

df = pd.DataFrame(data)

# Display dataset
print("Student Data:\n", df)

# Basic analysis
average_marks = df["Marks"].mean()
highest_marks = df["Marks"].max()
lowest_marks = df["Marks"].min()

print("\nAnalysis:")
print(f"Average Marks: {average_marks}")
print(f"Highest Marks: {highest_marks}")
print(f"Lowest Marks: {lowest_marks}")

# Add grade column
def assign_grade(mark):
    if mark >= 85:
        return "A"
    elif mark >= 70:
        return "B"
    else:
        return "C"

df["Grade"] = df["Marks"].apply(assign_grade)

print("\nFinal Data with Grades:\n", df)
