
import { CourseParts } from '../types/types';
import { Rest } from './Rest';

export const Part = ({ part }: { part: CourseParts }) => {
  return (
    <div>
      <h2>
        {part.name} {part.exerciseCount}
      </h2>
      <Rest part={part} />
    </div>
  );
};

export default Part;