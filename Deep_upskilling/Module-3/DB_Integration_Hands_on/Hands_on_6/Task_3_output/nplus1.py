
# TASK 3: Steps 87 - 90

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from sqlalchemy.orm import (
    sessionmaker,
    joinedload
)

from Task_1_output.models import (
    engine,
    Enrollment
)

Session = sessionmaker(bind=engine)
session = Session()


# STEP 87 Demonstrate N+1 Problem

print("STEP 87 : N+1 Problem")

enrollments = (
    session.query(
        Enrollment
    )
    .all()
)

for enrollment in enrollments:

    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )

print("""
Observation:
Multiple SQL queries are generated.
Check terminal logs.
""")


# STEP 88: Fix Using joinedload

print("STEP 88 : joinedload")

enrollments = (
    session.query(
        Enrollment
    )
    .options(
        joinedload(
            Enrollment.student
        ),
        joinedload(
            Enrollment.course
        )
    )
    .all()
)

for enrollment in enrollments:

    print(
        enrollment.student.first_name,
        "->",
        enrollment.course.course_name
    )


# STEP 89: Observation

print("STEP 89: Observation")

print("""
Without joinedload:
1 query + N queries

With joinedload:
Single JOIN query
""")

# STEP 90: Conclusion

print("STEP 90: Conclusion")

print("""N+1 Problem Eliminated Eager Loading Implemented Performance Improved""")

session.close()
