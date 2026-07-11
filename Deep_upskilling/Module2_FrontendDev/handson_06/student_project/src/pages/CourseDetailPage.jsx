import { useParams } from "react-router-dom";

function CourseDetailPage() {

    const { courseId } = useParams();

    return (
        <div className="detail-card">
            <h2>Course Detail</h2>
            <br/>

            <p>Course Name: {courseId === "1" ? "Data Structures" : courseId === "2" ? "Operating Systems" : courseId === "3" ? "DBMS" : "Unknown Course"}</p>
            <br/>
            <p>Course ID: {courseId}</p>
        </div>
    );
}

export default CourseDetailPage;