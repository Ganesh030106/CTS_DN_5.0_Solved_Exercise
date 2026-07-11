import { useState } from "react";

function StudentProfile() {

    const [name, setName] = useState("");
    const [email, setEmail] = useState("");
    const [semester, setSemester] = useState("");

    return (
        <div className="profile-card">

            <h2>Student Profile</h2>

            <label>Name</label>

            <input
                type="text"
                placeholder="Enter Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />

            <label>Email</label>
            <input
                type="email"
                placeholder="Enter Email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
            />

            <label>Semester</label>
            <input
                type="number"
                placeholder="Enter Semester"
                value={semester}
                onChange={(e) => setSemester(e.target.value)}
            />

            <h4>Name: {name}</h4>
            <h4>Email: {email}</h4>
            <h4>Semester: {semester}</h4>

        </div>
    );
}

export default StudentProfile;