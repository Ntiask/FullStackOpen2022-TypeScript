import { ContentProps } from "../types/types"

export const Total = (courseParts: ContentProps) => {
    return (
      <div>
        <p>
        Number of exercises{" "}
        {courseParts.courseParts.reduce((carry, part) => carry + part.exerciseCount, 0)}
        </p>
      </div>
    )
  }