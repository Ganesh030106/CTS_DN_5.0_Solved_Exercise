# TASK 2: Steps 80 - 86 CRUD Operations

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import date

from sqlalchemy.orm import sessionmaker

from Task_1_output.models import (
    engine,
    Department,
    Student,
    Course,
    Enrollment
)


# STEP 80: Create Session

Session = sessionmaker(bind=engine)
session = Session()

print("STEP 80 : Session Created")


# STEP 81: Insert Departments and Students

cs = Department(
    dept_name="Computer Science",
    hod_name="Dr. Ramesh Kumar",
    budget=850000
)

ece = Department(
    dept_name="Electronics",
    hod_name="Dr. Priya Nair",
    budget=620000
)

session.add_all([cs, ece])
session.commit()

print("Departments Inserted")


s1 = Student(
    first_name="Arjun",
    last_name="Mehta",
    email="arjun.orm@college.edu",
    enrollment_year=2022,
    department=cs
)

s2 = Student(
    first_name="Priya",
    last_name="Suresh",
    email="priya.orm@college.edu",
    enrollment_year=2022,
    department=cs
)

session.add_all([s1, s2])
session.commit()

print("Students Inserted")


# STEP 82: Insert Courses and Enrollments

c1 = Course(
    course_name="Data Structures",
    course_code="CS101",
    credits=4,
    department=cs
)

session.add(c1)
session.commit()

print("Course Inserted")


e1 = Enrollment(
    student=s1,
    course=c1,
    enrollment_date=date.today(),
    grade="A"
)

session.add(e1)
session.commit()

print("Enrollment Inserted")


# STEP 83: Query Students

print("\nSTEP 83: Query Students in Computer Science Department")
students = (
    session.query(Student)
    .join(Department)
    .filter(
        Department.dept_name == "Computer Science"
    )
    .all()
)
for student in students:
    print(student.first_name, student.last_name)


# STEP 84: Read Enrollment Details

print("\nSTEP 84: Read Enrollment Details")
enrollments = session.query(Enrollment).all()
for enrollment in enrollments:
    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )


# STEP 85: Update Student

print("\nSTEP 85: Update Student")

student = (
    session.query(Student)
    .filter(
        Student.email ==
        "priya.orm@college.edu"
    )
    .first()
)

if student:
    student.enrollment_year = 2024
    session.commit()
    print("Updated Successfully")


# STEP 86: Delete Enrollment

print("\nSTEP 86: Delete Enrollment")

enrollment = (session.query(Enrollment).first())

if enrollment:
    session.delete(enrollment)
    session.commit()
    print("Enrollment Deleted")


session.close()
