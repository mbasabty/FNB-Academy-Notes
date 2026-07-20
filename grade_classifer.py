# grade_classifier.py

# Collect learner information
learner_name = input("Enter learner's name: ")

subject1 = float(input("Enter mark for Subject 1: "))
subject2 = float(input("Enter mark for Subject 2: "))
subject3 = float(input("Enter mark for Subject 3: "))

# Calculate the average
average = (subject1 + subject2 + subject3) / 3

# Assign letter grade
if average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

# Assign pass/fail status
if average >= 50:
    status = "Pass"
else:
    status = "Fail"

# Display report card
print("\n========== STUDENT REPORT CARD ==========")
print(f"Learner Name : {learner_name}")
print(f"Subject 1    : {subject1}")
print(f"Subject 2    : {subject2}")
print(f"Subject 3    : {subject3}")
print(f"Average      : {round(average, 2)}")
print(f"Grade        : {grade}")
print(f"Status       : {status}")

# Check for intervention
print("\nIntervention Report:")
intervention = False

if subject1 < 40:
    print("- Subject 1 needs intervention.")
    intervention = True

if subject2 < 40:
    print("- Subject 2 needs intervention.")
    intervention = True

if subject3 < 40:
    print("- Subject 3 needs intervention.")
    intervention = True

if not intervention:
    print("No intervention required.")

print("=========================================")