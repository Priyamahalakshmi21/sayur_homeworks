subjects = int(input("Enter the number of subjects: "))
total_marks = 0
failed_subjects = []
for i in range(1, subjects + 1):
    marks = int(input(f"Enter marks for subject {i}: "))
    if marks < 35:
        failed_subjects.append(f"Subject {i}")
    total_marks += marks
print(f"Total marks: {total_marks}")
if failed_subjects:
    print(f"You failed in the subject{i} with {marks} marks.")