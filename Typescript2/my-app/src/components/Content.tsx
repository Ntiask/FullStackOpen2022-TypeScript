
import { CourseParts } from "../types/types"
import Part from "./Part"

export const Content = ({ courseParts }: { courseParts: CourseParts[] }) => {
    return (
      <div>
        {courseParts.map(course => <Part key={course.name} part={course} />)}
      </div>
    )
}