
import qr from 'qr-image';
import fs from 'fs';
import inquirer from "inquirer";


// 1.'fs' is a native node module for working with FileSystems
// const fs = require("fs");

// fs.writeFile('message.txt', "hello from node.js", (err)=>{
//     if (err) throw err;
//     console.log('The file has been saved!');
// })

// fs.readFile('./message.txt','utf-8',(err,data)=>{
//     if (err) throw err;
//     console.log(data)
// })

// // 2. how to use npm package cjs common javascript format

// var generateName = require('sillyname'); // module.exports = generateStupidName; require() loads the module and returns its exported function.
// var sillyname = generateName();

// console.log(`May name is ${sillyname}`)

// // 3. ecma script format to be consistent format with front and backend
// import generateName from "sillyname";
// var sillyname = generateName();
// console.log(`May name is ${sillyname}`)

// import {randomSuperhero} from "superheroes";

// const name = randomSuperhero();
// console.log(`I am ${name}!`);

// 4. QR code generator 2 packages - inquirer, qr-image

// get user input using inquirer
inquirer
    .prompt([{
        type: 'input',
        name: 'url',
        message: 'Enter the URL',
    }
    ])
    .then((answer)=>{
        const url = answer.url;
        var qr_svg = qr.image(url,{type:'png'});
        qr_svg.pipe(fs.createWriteStream('qr_image.png'));
        fs.writeFile("url.txt",url,(err)=>{
            if (err) throw err;
            console.log('The file has been saved!');
        })
        console.log('Your input: ',answer.url)
    })
    .catch((error)=>{
        if (error.isTtyError){
            console.log("couldn't render")
        } else{
            console.log('Other kind of error ',error)
        }
    })




// var svg_string = qr.imageSync('I love QR!', { type: 'svg' });