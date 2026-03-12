
#1.	Grade Checker
score = int(input("Enter the marks: "))

if score>=90:
    print("Grade :A")
elif score >=80:
    print("Grade :B")
elif score >=70:
    print("Grade :C")
elif score>=60:
    print("Grade :D")
else:
    print("Grade :F")


#2.	Student Grades

students = {} #creates new Dictionary having key-value pairs

while True:
    print("\n1. Add Student")
    print("2. Update Student Grade")
    print("3. Show All Student Grades")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students[name] = grade
        print("New Student added successfully!")

    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print("Grade updated successfully!")
        else:
            print("Student not found.")

    elif choice == "3":
        print("\nStudent Grades:")
        for name, grade in students.items():
            print(name, ":", grade)

    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid choice.")


#3.Write to a File
file = open("test.txt", "w")  #Opens a file in write mode

file.write("Hello, this is a sample text file for file handling")

file.close()

print("File created and content written successfully.")

#4. Read from a File

file = open("test.txt", "r")

content = file.read()
print(content)

file.close()