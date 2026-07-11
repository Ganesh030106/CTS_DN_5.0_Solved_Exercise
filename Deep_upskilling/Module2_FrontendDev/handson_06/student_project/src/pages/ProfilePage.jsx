import {
    useDispatch,
    useSelector
}
    from "react-redux";

import {
    unenroll
}
    from "../store/enrollmentSlice";
function ProfilePage() {
    const dispatch =
        useDispatch();

    const enrolledCourses =
        useSelector(
            state =>
                state.enrollment.enrolledCourses
        );
    return (
        <div className="profile-card">

            <h2>
                Enrolled Courses
            </h2>

            <br/>

            {enrolledCourses.map(course => (

                <div key={course.id}>

                    {course.name}

                    <br/>

                    <button style={{ color: "red", marginTop: "10px" }}
                        onClick={() =>
                            dispatch(
                                unenroll(course.id)
                            )
                        }
                    >
                        Remove
                    </button>
                    
                    <br/>

                </div>

            ))}

        </div>
    );
}

export default ProfilePage;