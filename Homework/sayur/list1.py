subjects = int(input("Enter the number of subjects: "))
total_marks = 0
subject_results = []
for i in range(subjects):
    subject_name = input(f"Enter the marks for subject {i + 1}: ")
    marks = float(subject_name)
    total_marks = total_marks + marks
    if marks < 35:
        subject_results.append("Fail")
    else:
        subject_results.append("Pass")
average = total_marks / subjects
for i in range(subjects):
    print(f"Subject {i + 1}: {subject_results[i]}")
print(f"Total Marks: {total_marks}")
print(f"Average Marks: {average:.2f}")
if "Fail" in subject_results:
    print("Overall Result: Fail")
else:
    print("Overall Result: Pass")  