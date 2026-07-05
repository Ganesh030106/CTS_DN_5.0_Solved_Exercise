from fastapi import FastAPI
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status
from sqlalchemy.orm import Session
from fastapi import Response

from database import engine
from database import get_db

from models import Base
from models import Course

from schemas import (
    CourseCreate,
    CourseUpdate,
    CourseResponse
)

app = FastAPI(
    title="Course Management API"
)

Base.metadata.create_all(bind=engine)


@app.get("/")
def home():
    return {"message": "Database Connected"}


@app.post(
    "/api/courses/",
    response_model=CourseResponse,
    status_code=status.HTTP_201_CREATED
)
def create_course(
    course: CourseCreate,
    response: Response,
    db: Session = Depends(get_db)
):

    db_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)

    response.headers["Location"] = (
        f"/api/courses/{db_course.id}"
    )

    return db_course


def create_course(
    course: CourseCreate,
    response: Response,
    db: Session = Depends(get_db)
):

    db_course = Course(
        name=course.name,
        code=course.code,
        credits=course.credits,
        department_id=course.department_id
    )

    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    
    response.headers["Location"] = (
    f"/api/courses/{db_course.id}")

    return db_course


@app.get(
    "/api/courses/",
    response_model=list[CourseResponse]
)
def get_courses(
    db: Session = Depends(get_db)
):

    return db.query(Course).all()


@app.get(
    "/api/courses/{course_id}",
    response_model=CourseResponse
)
def get_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    return course


@app.put(
    "/api/courses/{course_id}",
    response_model=CourseResponse
)
def update_course(
    course_id: int,
    course_update: CourseUpdate,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = (
        course_update.model_dump(
            exclude_unset=True
        )
    )

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course

@app.patch(
    "/api/courses/{course_id}",
    response_model=CourseResponse
)
def patch_course(
    course_id: int,
    course_update: CourseUpdate,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    update_data = course_update.model_dump(
        exclude_unset=True
    )

    for key, value in update_data.items():
        setattr(course, key, value)

    db.commit()
    db.refresh(course)

    return course


@app.delete(
    "/api/courses/{course_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_course(
    course_id: int,
    db: Session = Depends(get_db)
):

    course = (
        db.query(Course)
        .filter(Course.id == course_id)
        .first()
    )

    if not course:
        raise HTTPException(
            status_code=404,
            detail="Course not found"
        )

    db.delete(course)
    db.commit()

    return