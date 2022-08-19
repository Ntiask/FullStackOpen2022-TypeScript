import { assertNever } from "../utils/utils";
import { CourseParts, CourseType } from "../types/types";

export const Rest = ({ part }: { part: CourseParts }) => {
    switch (part.type) {
      case CourseType.Normal:
        return (
          <div>
            <strong>{part.description}</strong>
          </div>
        );
      case CourseType.GroupProject:
        return (
          <div>
            <strong>project exercises {part.groupProjectCount}</strong>
          </div>
        );
      case CourseType.Submission:
        return (
          <div>
            <strong>{part.description}</strong>
            <div>
              submit to <a href={part.exerciseSubmissionLink}>{part.exerciseSubmissionLink}</a>
            </div>
          </div>
        );
      case CourseType.Special:
        return (
          <div>
            <strong>{part.description}</strong>
            <h3>Required skills:</h3>
            <ul>
              {part.requirements.map((r) => (
                <li key={r}>{r}</li>
              ))}
            </ul>
          </div>
        );
      default:
        return assertNever(part);
    }
  };