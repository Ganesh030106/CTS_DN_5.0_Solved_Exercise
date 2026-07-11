function Header({ siteName, enrolledCount }) {
    return (
        <header>
            <h1>{siteName}</h1>

            <nav>
                <ul>
                    <li>Home</li>
                    <li>Courses</li>
                    <li>Profile</li>
                </ul>
            </nav>


            <br />
            <h4>Enrolled Courses: {enrolledCount}</h4>

        </header>
    );
}

export default Header;