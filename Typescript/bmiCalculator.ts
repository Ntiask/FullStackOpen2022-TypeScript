interface MultiplyValues {
    value1: number;
    value2: number;
  }
  
  const parseArguments = (args: Array<string>): MultiplyValues => {
    if (args.length < 4) throw new Error('Not enough arguments');
    if (args.length > 4) throw new Error('Too many arguments');
  
    if (!isNaN(Number(args[2])) && !isNaN(Number(args[3]))) {
      return {
        value1: Number(args[2]),
        value2: Number(args[3])
      };
    } else {
      throw new Error('Provided values were not numbers!');
    }
  };

export const calculateBmi = (height: number, weight: number): string => {
    const heightInMeters = height/100;
    const bmi = weight/(heightInMeters*heightInMeters);
    if (bmi <= 18.5){
        return 'Underweight';
    } else if (bmi >= 18.5 && bmi <=24.9) {
        return 'Normal (healthy Weight)';
    } else if (bmi >= 25 && bmi <= 29.9) {
        return 'Overweight';
    } else {
        return 'Obesity';
    }
};

try {
    const { value1, value2 } = parseArguments(process.argv);
    console.log(calculateBmi(value1, value2));
  } catch (error: unknown) {
    let errorMessage = 'Something bad happened.';
    if (error instanceof Error) {
      errorMessage += ' Error: ' + error.message;
    }
    console.log(errorMessage);
  }