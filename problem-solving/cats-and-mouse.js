// Link to problem: https://www.hackerrank.com/challenges/cats-and-a-mouse/problem
'use strict';

const fs = require('fs');

process.stdin.resume();
process.stdin.setEncoding('utf-8');

let inputString = '';
let currentLine = 0;

process.stdin.on('data', inputStdin => {
    inputString += inputStdin;
});

process.stdin.on('end', _ => {
    inputString = inputString.replace(/\s*$/, '')
        .split('\n')
        .map(str => str.replace(/\s*$/, ''));

    main();
});

function readLine() {
    return inputString[currentLine++];
}

// Complete the catAndMouse function below.
function catAndMouse(x, y, z) {
    const catOneToMouse = Math.abs(z-x);
    const catTwoToMouse = Math.abs(z-y);
    
    if (catOneToMouse === catTwoToMouse) {
        return `Mouse C`;
    } else {
        return catOneToMouse > catTwoToMouse 
            ? `Cat B`
            : `Cat A`;
    }
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const q = parseInt(readLine(), 10);

    for (let qItr = 0; qItr < q; qItr++) {
        const xyz = readLine().split(' ');

        const x = parseInt(xyz[0], 10);

        const y = parseInt(xyz[1], 10);

        const z = parseInt(xyz[2], 10);

        let result = catAndMouse(x, y, z);

        ws.write(result + "\n");
    }

    ws.end();
}
