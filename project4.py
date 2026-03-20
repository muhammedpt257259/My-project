import pandas as pd
import matplotlib.pyplot as plt


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 75:
        return "A"
    elif percentage >= 60:
        return "B"
    elif percentage >= 50:
        return "C"
    elif percentage >= 40:
        return "D"
    else:
        return "F"

subjects = []
marks = []

n = int(input("Enter number of subjects: "))

for i in range(n):
    sub = input(f"Enter subject {i+1} name: ")
    mark = float(input(f"Enter marks for {sub}: "))
    
    subjects.append(sub)
    marks.append(mark)


df = pd.DataFrame({
    "Subject": subjects,
    "Marks": marks
})


total = sum(marks)
percentage = total / n
grade = calculate_grade(percentage)


status = "Pass" if percentage >= 40 else "Fail"


print("\n----- RESULT -----")
print(df)
print(f"\nTotal Marks: {total}")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade: {grade}")
print(f"Status: {status}")


plt.figure()
plt.bar(df["Subject"], df["Marks"])
plt.title("Marks Distribution")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.xticks(rotation=30)

plt.show()