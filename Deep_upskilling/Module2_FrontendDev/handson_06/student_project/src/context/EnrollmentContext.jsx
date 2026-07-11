import { createContext, useState } from "react";

export const EnrollmentContext = createContext();

function EnrollmentProvider({ children }) {

    const [enrolledCourses, setEnrolledCourses] = useState([]);

    const enrollCourse = (course) => {
        setEnrolledCourses([
            ...enrolledCourses,
            course
        ]);
    };

    return (
        <EnrollmentContext.Provider
            value={{
                enrolledCourses,
                enrollCourse
            }}
        >
            {children}
        </EnrollmentContext.Provider>
    );
}

export default EnrollmentProvider;