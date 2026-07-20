# grade_report.py

# List of student dictionaries
students = [
    {"name": "Sipho", "maths": 78, "english": 85, "science": 90},
    {"name": "Lebo", "maths": 65, "english": 72, "science": 68},
    {"name": "Aisha", "maths": 45, "english": 55, "science": 50},
    {"name": "Neo", "maths": 92, "english": 88, "science": 95},
    {"name": "Thandi", "maths": 35, "english": 48, "science": 40}
]

# Store generated results
results = []

# Store all marks for class statistics
all_marks = []

# Process each student
for student in students:
    maths = student["maths"]
    english = student["english"]
    science = student["science"]

    # Add marks to list for statistics
    all_marks.extend([maths, english, science])

    # Calculate average
    average = (maths + english + science) / 3

    # Grade logic
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

    # Status logic
    if average >= 50:
        status = "Pass"
    else:
        status = "Fail"

    # Add result dictionary
    results.append({
        "name": student["name"],
        "average": round(average, 2),
        "grade": grade,
        "status": status
    })


# Calculate class statistics
class_average = sum([result["average"] for result in results]) / len(results)
highest_mark = max(all_marks)
lowest_mark = min(all_marks)


# Display class report
print("\n========== CLASS REPORT ==========")

for result in results:
    print(f"Name: {result['name']}")
    print(f"Average: {result['average']}")
    print(f"Grade: {result['grade']}")
    print(f"Status: {result['status']}")
    print("-" * 30)

print("\n========== CLASS STATISTICS ==========")
print(f"Class Average: {round(class_average, 2)}")
print(f"Highest Mark: {highest_mark}")
print(f"Lowest Mark: {lowest_mark}")


# Student search system
while True:
    search_name = input("\nSearch for a student (or type 'exit'): ").strip()

    if search_name.lower() == "exit":
        print("Search ended.")
        break

    found = False

    for result in results:
        if result["name"].lower() == search_name.lower():
            print("\nStudent Found:")
            print(f"Name: {result['name']}")
            print(f"Average: {result['average']}")
            print(f"Grade: {result['grade']}")
            print(f"Status: {result['status']}")
            found = True
            break

    if not found:
        print("Student not found.")
        