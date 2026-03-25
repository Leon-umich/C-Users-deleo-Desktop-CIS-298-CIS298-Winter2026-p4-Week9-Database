# from https://www.py4e.com/html3/15-database

import sqlite3

connection = sqlite3.connect('registration.sqlite')
cursor = connection.cursor()

choice = ""

while choice != "QUIT":
    choice = input("Enter a choice: 1 - Manage Faculty, 2 - Manage Courses, 3 - Manage Enrollments, 4 - Manage Sections, 5 - Manage Students, 6 - Show Transcript, QUIT - Exit: ")

    if choice == "1":
        action = input("Enter 1 for List Faculty, 2 for Add Faculty, 3 for Update Faculty")

        if action == "1":
            cursor.execute('SELECT * FROM Faculty')
            print("id, name, email")
            for row in cursor:
                print(row)
        elif action == "2":
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('INSERT INTO faculty (name, email) VALUES (?, ?)',(name, email))
            connection.commit()
        elif action == "3":
            id = int(input("Enter the ID to update"))
            name = input("Enter name")
            email = input("Enter email")
            cursor.execute('update faculty set name = ?, email = ? WHERE id = ?', (name, email, id) )
            connection.commit()

    if choice == "2":
        action = input("Enter 1 for List Courses, 2 for Add Course, 3 for Update Course: ")

        if action == "1":
            cursor.execute('SELECT * FROM Course')
            print("id, department, number, credits, description")
            for row in cursor:
                print(row)

        elif action == "2":
            department = input("Enter department: ")
            number = input("Enter course number: ")
            credits = int(input("Enter credits: "))
            description = input("Enter description: ")

            cursor.execute(
                'INSERT INTO Course (Department, Number, Credits, Description) VALUES (?, ?, ?, ?)',
                (department, number, credits, description)
            )
            connection.commit()

        elif action == "3":
            id = int(input("Enter the ID to update: "))
            department = input("Enter department: ")
            number = input("Enter course number: ")
            credits = int(input("Enter credits: "))
            description = input("Enter description: ")

            cursor.execute(
                'UPDATE Course SET Department = ?, Number = ?, Credits = ?, Description = ? WHERE ID = ?',
                (department, number, credits, description, id)
            )
            connection.commit()


    if choice == "3":
        action = input("Enter 1 for List Enrollments, 2 for Add Enrollment, 3 for Update Enrollment, 4 for Delete Enrollment: ")

        if action == "1":
            cursor.execute('SELECT * FROM Enrollment')
            print("id, student_id, section_id, grade")
            for row in cursor:
                print(row)

        elif action == "2":
            student_id = int(input("Enter student ID: "))
            section_id = int(input("Enter section ID: "))
            grade = int(input("Enter grade: "))

            cursor.execute(
                'INSERT INTO Enrollment (Student_ID, Section_ID, Grade) VALUES (?, ?, ?)',
                (student_id, section_id, grade)
            )
            connection.commit()

        elif action == "3":
            id = int(input("Enter the ID to update: "))
            student_id = int(input("Enter student ID: "))
            section_id = int(input("Enter section ID: "))
            grade = int(input("Enter grade: "))

            cursor.execute(
                'UPDATE Enrollment SET Student_ID = ?, Section_ID = ?, Grade = ? WHERE ID = ?',
                (student_id, section_id, grade, id)
            )
            connection.commit()

        elif action == "4":
            id = int(input("Enter the enrollment ID to delete: "))

            cursor.execute(
                'DELETE FROM Enrollment WHERE ID = ?',
                (id,)
            )
            connection.commit()


    if choice == "4":
            action = input("Enter 1 for List Sections, 2 for Add Section, 3 for Update Section: ")

            if action == "1":
                cursor.execute('SELECT * FROM Section')
                print("id, course_id, faculty_id, semester, day, time")
                for row in cursor:
                    print(row)

            elif action == "2":
                course_id = int(input("Enter course ID: "))
                faculty_id = int(input("Enter faculty ID: "))
                semester = input("Enter semester: ")
                day = input("Enter day: ")
                time = input("Enter time: ")

                cursor.execute(
                    'INSERT INTO Section (Course_ID, Faculty_ID, Semester, Day, Time) VALUES (?, ?, ?, ?, ?)',
                    (course_id, faculty_id, semester, day, time)
                )
                connection.commit()

            elif action == "3":
                id = int(input("Enter the ID to update: "))
                course_id = int(input("Enter course ID: "))
                faculty_id = int(input("Enter faculty ID: "))
                semester = input("Enter semester: ")
                day = input("Enter day: ")
                time = input("Enter time: ")

                cursor.execute(
                    'UPDATE Section SET Course_ID = ?, Faculty_ID = ?, Semester = ?, Day = ?, Time = ? WHERE ID = ?',
                    (course_id, faculty_id, semester, day, time, id)
                )
                connection.commit()


    if choice == "5":
        action = input("Enter 1 for List Students, 2 for Add Student, 3 for Update Student: ")

        if action == "1":
            cursor.execute('SELECT * FROM Student')
            print("id, name, major")
            for row in cursor:
                print(row)

        elif action == "2":
            name = input("Enter name: ")
            major = input("Enter major: ")

            cursor.execute(
                'INSERT INTO Student (Name, Major) VALUES (?, ?)',
                (name, major)
            )
            connection.commit()

        elif action == "3":
            id = int(input("Enter the ID to update: "))
            name = input("Enter name: ")
            major = input("Enter major: ")

            cursor.execute(
                'UPDATE Student SET Name = ?, Major = ? WHERE ID = ?',
                (name, major, id)
            )
            connection.commit()

# to get a transcript for a given student

if choice == "6":
    student = int(input("Enter student ID: "))

    cursor.execute('''
        SELECT Course.Department, Course.Number, Course.Credits, Enrollment.Grade
        FROM Enrollment
        INNER JOIN Student ON Student.ID = Enrollment.Student_ID
        INNER JOIN Section ON Section.ID = Enrollment.Section_ID
        INNER JOIN Course ON Course.ID = Section.Course_ID
        WHERE Student_ID = ?
    ''', (student,))

    print("department, course number, credits, grade")
    for row in cursor:
        print(row)

connection.close()
