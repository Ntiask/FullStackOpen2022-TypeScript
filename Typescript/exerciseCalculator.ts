
interface MultiplyValues {
    value1: number;
    value2: number;
    value3: number;
    value4: number;
    value5: number;
    value6: number;
    value7: number;
    value8: number;
  }
  
  const parseArgs = (args: Array<string>): MultiplyValues => {
    if (args.length < 10) throw new Error('Not enough arguments');
    if (args.length > 10) throw new Error('Too many arguments');
  
    if (!isNaN(Number(args[2])) && !isNaN(Number(args[3]))) {
      return {
        value1: Number(args[2]),
        value2: Number(args[4]),
        value3: Number(args[5]),
        value4: Number(args[6]),
        value5: Number(args[7]),
        value6: Number(args[8]),
        value7: Number(args[9]),
        value8: Number(args[10])
      };
    } else {
      throw new Error('Provided values were not numbers!');
    }
  };

export const calculateExercises = (x: number[], y: number): object => {
        let sum = 0;
        let training_days = 0;
        let lackdays = 0;
        let rating = 0;
        const target = y;
        let success = false;
        let ratingDescription = "";

        x.forEach((i: number) => {
            if (i > 0){
                training_days++;
            } else {
                lackdays++;
            }

        sum = sum + i;});
        const average = sum/7;
        
        if (average > 2 && lackdays < training_days) {
            rating = 3;
            ratingDescription = "You are on point! Keep up the good work";
            success = true;
        } else if (average > 2 && lackdays > training_days) {
            rating = 2;
            ratingDescription = "Average week. Good Job!";
            success = true;
        } else {
            rating = 1;
            ratingDescription = "This week aint your best ones..";
            success = false;
        }

        const responseObject = { 

            periodLength: x.length,
            trainingDays: training_days,
            success: success,
            rating: rating,
            ratingDescription: ratingDescription,
            target: target,
            average: average

        };

    return responseObject;
};

try {
    const { value1, value2, value3, value4, value5 , value6, value7, value8 } = parseArgs(process.argv);
    console.log(calculateExercises([value1,value2,value3,value4,value5,value6, value7], value8));
  } catch (error: unknown) {
    let errorMessage = 'Something bad happened.';
    if (error instanceof Error) {
      errorMessage += ' Error: ' + error.message;
    }
    console.log(errorMessage);
  }