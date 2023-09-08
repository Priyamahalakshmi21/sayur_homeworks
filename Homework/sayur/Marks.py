subjects = int(input("How many subjects do you have in this semester? "))
total_marks = 0

for subject in range(1,subjects + 1):
    marks = int(input(f"Enter marks for subject {subject}: "))
    total_marks = total_marks + marks

average = total_marks / subjects

if average > 70:
    grade = "First Class"
elif average > 60:
    grade = "Second Class"
elif average >= 50:
    grade = "Third Class"
else:
    grade = "Fail"

print(f"Total marks: {total_marks}")
print(f"Average marks: {average:.2f}")
print(f"Grade: {grade}")