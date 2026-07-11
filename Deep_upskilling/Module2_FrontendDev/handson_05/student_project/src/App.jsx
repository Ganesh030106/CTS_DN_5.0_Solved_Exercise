import { useEffect, useState } from "react";

import Header from "./components/Header";
import Footer from "./components/Footer";
import CourseCard from "./components/CourseCard";
import StudentProfile from "./components/StudentProfile";

function App() {

  const [courses, setCourses] = useState([]);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  const [enrolledCourses, setEnrolledCourses] = useState([]);

  useEffect(() => {

    fetchCourses();

  }, []);

  useEffect(() => {
    console.log("Courses updated");
  }, [courses]);

  async function fetchCourses() {

    try {

      setLoading(true);

      await new Promise(resolve =>
        setTimeout(resolve, 2000)
      );

      const response =
        await fetch(
          "https://jsonplaceholder.typicode.com/posts"
        );

      if (!response.ok) {
        throw new Error("Failed to fetch courses");
      }

      const data = await response.json();

      const mappedCourses =
        data.slice(0, 5).map((post, index) => ({
          id: index + 1,
          name: post.title.substring(0, 20),
          code: `CS10${index + 1}`,
          credits: 3 + (index % 2),
          grade: "A"
        }));

      setCourses(mappedCourses);

    } catch (err) {

      setError(err.message);

    } finally {

      setLoading(false);

    }
  }

  const handleEnroll = (id) => {

    const selected =
      courses.find(course => course.id === id);

    setEnrolledCourses([
      ...enrolledCourses,
      selected
    ]);
  };

  if (loading) {
    return <h2>Loading...</h2>;
  }

  if (error) {
    return <h2>{error}</h2>;
  }

  return (
    <>
      <Header
        siteName="Student Portal"
        enrolledCount={enrolledCourses.length}
      />

      <main>

        <div className="course-grid">

          {courses.map(course => (

            <CourseCard
              key={course.id}
              {...course}
              onEnroll={handleEnroll}
            />

          ))}

        </div>

      </main>

      <StudentProfile />

      <Footer />
    </>
  );
}

export default App;