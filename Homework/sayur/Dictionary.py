subject_marks = {}
subjects = int(input("Enter the number of subjects: "))
for i in range(subjects):
    subject_name = input(f"Enter the name of subject {i + 1}: ")
    subject_code = input(f"Enter the code for subject {i + 1}: ")
    subject_marks[subject_name] = subject_code
marks = {}
for subject_name, subject_code in subject_marks.items():
    subject_marks[subject_name] = subject_code
    marks[subject_name] = int(input(f"Enter the marks for {subject_name}: "))
print("\nSubject Marks:")
for subject_name, mark in marks.items():
    print(f"{subject_name} ({subject_marks[subject_name]}) - {mark}")