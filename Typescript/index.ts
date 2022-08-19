import express from 'express';
import { calculateBmi } from './bmiCalculator';
import bodyParser from 'body-parser';
import { calculateExercises } from './exerciseCalculator';


const app = express();

const jsonParser = bodyParser.json();


app.get('/hello', (_req, res) =>{
    res.send('Hello Full Stack!');
});

app.get('/bmi', (req, res) =>{

    let value1 = 0;
    let value2 = 0;

    if (!isNaN(Number(req.query.height)) && !isNaN(Number(req.query.weight)) ) {
        value1 = Number(req.query.height);
        value2 = Number(req.query.weight);
        res.send(calculateBmi(value1, value2));
    } else {
        res.send({error: "malformatted parameters"});
    }
});

app.post('/exercises', jsonParser, (req, res) =>{
    // eslint-disable-next-line @typescript-eslint/no-unsafe-assignment
    const { daily_exercises, target } = req.body;
    let malform = false;
    let target1 = 0;
    const params = [];
    // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
    for (let i = 0; i< daily_exercises.length; i++) {
        // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
        // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
        if (!isNaN(Number(daily_exercises[i]))) {
            // eslint-disable-next-line @typescript-eslint/no-unsafe-member-access
            params.push(Number(daily_exercises[i]));
        } else {
            malform = true;
        }
    }

    if (params.length < 7 || target === undefined) {
        return res.send({error: "Parameters Missing"});
    }
    if (isNaN(Number(target))){
        malform = true;
    } else {
        target1 = Number(target);
    }
    if (malform) {
        return res.send({error: "malformed parameters"});
    }
    
    return res.send(calculateExercises(params, target1));

});

const PORT = 3003;

app.listen(PORT, () => {
    console.log(`Server Running on port ${PORT}`);
});