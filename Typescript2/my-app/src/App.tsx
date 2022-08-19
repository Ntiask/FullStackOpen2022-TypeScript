import { Header } from "./components/Header";
import { Content } from "./components/Content";
import { Total } from "./components/Total";
import { CourseParts } from "./types/types";
import { CourseType } from "./types/types";

const App = () => {
  const courseName = "Half Stack application development";
  const courseParts1: CourseParts[] = [
    {
      name: "Fundamentals",
      exerciseCount: 10,
      description: "This is the easy course part",
      type: CourseType.Normal
    },
    {
      name: "Advanced",
      exerciseCount: 7,
      description: "This is the hard course part",
      type: CourseType.Normal
    },
    {
      name: "Using props to pass data",
      exerciseCount: 7,
      groupProjectCount: 3,
      type: CourseType.GroupProject
    },
    {
      name: "Deeper type usage",
      exerciseCount: 14,
      description: "Confusing description",
      exerciseSubmissionLink: "https://fake-exercise-submit.made-up-url.dev",
      type: CourseType.Submission
    },
    {
      name: "Backend development",
      exerciseCount: 21,
      description: "Typing the backend",
      requirements: ["nodejs", "jest"],
      type: CourseType.Special
    }
  ]


  return (
    <div>
      <Header courseName={courseName} />
      <Content courseParts={courseParts1} />
      <Total courseParts={courseParts1} />
    </div>
  );
};

export default App;