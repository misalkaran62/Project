# student_console.py
import json
import os

# Colors (Windows supported)
BLUE = ""
GREEN = ""
RED = ""
YELLOW = ""
CYAN = ""
RESET = ""

FILENAME = "students.json"

def load_data():
    if os.path.exists(FILENAME):
        try:
            with open(FILENAME, "r") as file:
                data = json.load(file)
                if isinstance(data, dict):
                    return data
                else:
                    print("JSON file corrupted! Loading default data.")
                    return {'Aaru': 100, 'Sana': 200}
        except:
            print("Error reading JSON! Loading default data.")
            return {'Aaru': 100, 'Sana': 200}
    return {'Aaru': 100, 'Sana': 200}


def save_data(data):
    with open(FILENAME, "w") as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully!")


student = load_data()

print("=================================")
print("    Student Dictionary Manager    ")
print("=================================\n")

while True:
    print("\n========== MENU ==========")
    print("1. Add Student")
    print("2. Update Marks")
    print("3. Delete Student")
    print("4. View All Students")
    print("5. Search Student")
    print("6. Highest Marks")
    print("7. Lowest Marks")
    print("8. Count Students")
    print("9. Save Data")
    print("10. Load Data")
    print("11. Exit")
    print("==========================\n")

    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        name = input("Enter student name: ").strip()
        marks = int(input("Enter marks: "))
        student[name] = marks
        print(f"{name} added successfully!")

    elif choice == '2':
        name = input("Enter student name to update: ").strip()
        if name in student:
            marks = int(input("Enter new marks: "))
            student[name] = marks
            print(f"Marks updated for {name}!")
        else:
            print("Student not found!")

    elif choice == '3':
        name = input("Enter student name to delete: ").strip()
        if name in student:
            del student[name]
            print(f"Deleted: {name}")
        else:
            print("Student not found!")

    elif choice == '4':
        print("\nStudent List:")
        for name, marks in student.items():
            print(f"{name}: {marks}")

    elif choice == '5':
        name = input("Enter student name to search: ")
        if name in student:
            print(f"Found: {name} → {student[name]}")
        else:
            print("Student not found!")

    elif choice == '6':
        name = max(student, key=student.get)
        print(f"Highest Marks: {name} → {student[name]}")

    elif choice == '7':
        name = min(student, key=student.get)
        print(f"Lowest Marks: {name} → {student[name]}")

    elif choice == '8':
        print(f"Total Students: {len(student)}")

    elif choice == '9':
        save_data(student)

    elif choice == '10':
        student = load_data()
        print("Data Loaded!")

    elif choice == '11':
        save_data(student)
        print("Exiting. Thank you!")
        break

    else:
        print("Invalid choice!")
