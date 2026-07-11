import { Link } from "react-router-dom";
import { useContext } from "react";

import { useDispatch }
    from "react-redux";

import {
    enroll
}
    from "../store/enrollmentSlice";

function CoursesPage() {

    const dispatch = useDispatch();


    const courses = [
        { id: 1, name: "Data Structures" },
        { id: 2, name: "Operating Systems" },
        { id: 3, name: "DBMS" }
    ];

    return (
        <div className="course-links">

            <h2>Courses</h2>

            {courses.map(course => (

                <div
                    key={course.id}
                    className="course-item"
                >

                    <Link
                        to={`/courses/${course.id}`}
                    >
                        {course.name}
                    </Link>

                    <br />

                    <button
                        onClick={() =>
                            dispatch(
                                enroll(course)
                            )
                        }
                    >
                        Enroll
                    </button>

                </div>

            ))}

        </div>
    );
}

export default CoursesPage;