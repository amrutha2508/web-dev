//To see how the final website should work, run "node solution.js".
//Make sure you have installed all the dependencies with "npm i".
//The password is ILoveProgramming
import bodyParser from "body-parser";
import express from 'express';
import { dirname } from 'path';
import { fileURLToPath } from 'url';

const __dirname = dirname(fileURLToPath(import.meta.url));

const app = express();
const port = 3000;
var userIsAuthorized = false;

function logger(req,res,next){
    console.log('request method: ',req.method);
    console.log('request url: ',req.url);
    console.log('body: ',req.body);
    next();
}

app.use(bodyParser.urlencoded({ extended: true }));
app.use(logger);

function passwordCheck(req, res, next){
    console.log('in password check')
    const password = req.body['password'];
    if (password == "ILoveProgramming"){
        userIsAuthorized = true;
        console.log('password is correct');
    }  
    console.log('password is incorrect');
    next();
}

app.use(passwordCheck);

app.get('/',(req, res) => {
    console.log('in get');
    res.sendFile(__dirname + '/public/index.html');
})

app.post('/check',(req, res) => {
    if (userIsAuthorized){
        console.log('directing to secret');
        res.sendFile(__dirname + "/public/secret.html");
    } else {
        console.log('directing to index.html')
        res.sendFile(__dirname + "/public/index.html");
    }
});

app.listen(port, () => {
    console.log(`Listening on port ${port}`);
})
