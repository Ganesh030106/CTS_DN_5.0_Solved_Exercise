import { Link } from "react-router-dom";
import { useContext } from "react";
import {
    useSelector
}
    from "react-redux";


function Header({ siteName }) {
    const enrolledCourses =
        useSelector(
            state =>
                state.enrollment.enrolledCourses
        );

    return (
        <header>

            <h1>{siteName}</h1>

            <nav>
                <ul>
                    <li>
                        <Link to="/">Home</Link>
                    </li>

                    <li>
                        <Link to="/courses">Courses</Link>
                    </li>

                    <li>
                        <Link to="/profile">Profile</Link>
                    </li>
                </ul>
            </nav>

            <br />

            <h3>
                Enrolled:
                {enrolledCourses.length}
            </h3>

        </header>
    );
}

export default Header;