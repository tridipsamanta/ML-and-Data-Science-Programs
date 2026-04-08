import matplotlib.pyplot as plt

# ----------- INPUT SECTION -----------
num_subjects = int(input("Enter number of subjects: "))

subjects = []
student1_marks = []
student2_marks = []

print("\n--- Enter Subject Names ---")
for i in range(num_subjects):
    subject = input(f"Subject {i+1} name: ")
    subjects.append(subject)

print("\n--- Enter marks for Student 1 ---")
for sub in subjects:
    mark = int(input(f"{sub}: "))
    student1_marks.append(mark)

print("\n--- Enter marks for Student 2 ---")
for sub in subjects:
    mark = int(input(f"{sub}: "))
    student2_marks.append(mark)

# ----------- ANALYTICS SECTION -----------
total1 = sum(student1_marks)
total2 = sum(student2_marks)

avg1 = total1 / num_subjects
avg2 = total2 / num_subjects

topper = "Student 1" if total1 > total2 else "Student 2"

print("\n===== ANALYTICS =====")
print(f"Student 1 Total: {total1}, Average: {avg1:.2f}")
print(f"Student 2 Total: {total2}, Average: {avg2:.2f}")
print(f"Topper: {topper}")

# ----------- BAR CHART -----------
x = range(num_subjects)

plt.figure()
plt.bar(x, student1_marks)
plt.bar(x, student2_marks, bottom=student1_marks)
plt.xticks(x, subjects)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.title("Marks Comparison (Stacked Bar Chart)")
plt.show()

# ----------- PIE CHART (Student 1) -----------
plt.figure()
plt.pie(student1_marks, labels=subjects, autopct="%1.1f%%")
plt.title("Student 1 – Subject-wise Distribution")
plt.show()

# ----------- PIE CHART (Student 2) -----------
plt.figure()
plt.pie(student2_marks, labels=subjects, autopct="%1.1f%%")
plt.title("Student 2 – Subject-wise Distribution")
plt.show()
