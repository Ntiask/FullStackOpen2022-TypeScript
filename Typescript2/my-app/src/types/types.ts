


export interface HeaderProps {
    courseName: String
  }
  
export interface courseObject {
    name: String
    exerciseCount: number
}
  
export interface ContentProps {
    courseParts: Array<courseObject>
}

export enum CourseType {
    Normal = 'normal',
    GroupProject = 'groupProject',
    Submission = 'submission',
    Special = 'special'
  }
  
interface CoursePartBase {
    name: string;
    exerciseCount: number;
    type: CourseType;
}
  
interface CourseDescriptionPart_Base extends CoursePartBase {
    description: string;
}
  
export interface CourseNormalPart extends CourseDescriptionPart_Base {
    type: CourseType.Normal;
}

export interface CourseProjectPart extends CoursePartBase {
    type: CourseType.GroupProject;
    groupProjectCount: number;
}

export interface CourseSubmissionPart extends CourseDescriptionPart_Base {
    type: CourseType.Submission;
    exerciseSubmissionLink: string;
}

export interface CourseSpecialPart extends CourseDescriptionPart_Base {
    type: CourseType.Special;
    requirements: string[];
}

export type CourseParts = CourseNormalPart | CourseProjectPart | CourseSubmissionPart | CourseSpecialPart;