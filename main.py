import json
import os

FILE_NAME = "students.json"


# Load student data from JSON file
def load_data():
    if not os.path.exists(FILE_NAME):
        return []
    with open(FILE_NAME, "r") as file:
        return json.load(file)


# Save student data to JSON file
def save_data(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# Add a new student
def add_student(students):
    name = input("Enter student name: ")
    course = input("Enter course: ")
    marks = int(input("Enter marks: "))

    student_id = students[-1]["id"] + 1 if students else 1

    student = {
        "id": student_id,
        "name": name,
        "course": course,
        "marks": marks
    }

    students.append(student)
    save_data(students)
    print("✅ Student added successfully!")


# View all students
def view_students(students):
    if not students:
        print("⚠️ No students found.")
        return

    for student in students:
        print(
            f"ID: {student['id']} | "
            f"Name: {student['name']} | "
            f"Course: {student['course']} | "
            f"Marks: {student['marks']}"
        )


# Update student details
def update_student(students):
    student_id = int(input("Enter student ID to update: "))

    for student in students:
        if student["id"] == student_id:
            student["name"] = input("Enter new name: ")
            student["course"] = input("Enter new course: ")
            student["marks"] = int(input("Enter new marks: "))
            save_data(students)
            print("✅ Student updated successfully!")
            return

    print("❌ Student ID not found.")


# Delete a student
def delete_student(students):
    student_id = int(input("Enter student ID to delete: "))

    for student in students:
        if student["id"] == student_id:
            students.remove(student)
            save_data(students)
            print("🗑️ Student deleted successfully!")
            return

    print("❌ Student ID not found.")


# Main program
def main():
    students = load_data()

    while True:
        print("\n--- Student Management System ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            update_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            print("👋 Exiting program. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Try again.")


if __name__ == "__main__":
    main()
