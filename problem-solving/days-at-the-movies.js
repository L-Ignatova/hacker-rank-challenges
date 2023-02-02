// link to problem: https://www.hackerrank.com/challenges/beautiful-days-at-the-movies

'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', function(inputStdin) {
    inputString += inputStdin;
});

process.stdin.on('end', function() {
    inputString = inputString.split('\n');

    main();
});

function readLine() {
    return inputString[currentLine++];
}

function beautifulDays(i, j, k) {
    const reversedNum = num => parseFloat(num.toString().split('').reverse().join('')) * Math.sign(num);
    
    return Array
        .from({ length:(j-i + 1) }, (v, l) => l+i)
        .filter(x => Math.abs(x - reversedNum(x)) % k === 0)
        .length;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const firstMultipleInput = readLine().replace(/\s+$/g, '').split(' ');
    const i = parseInt(firstMultipleInput[0], 10);
    const j = parseInt(firstMultipleInput[1], 10);
    const k = parseInt(firstMultipleInput[2], 10);
    const result = beautifulDays(i, j, k);

    ws.write(result + '\n');
    ws.end();
}
