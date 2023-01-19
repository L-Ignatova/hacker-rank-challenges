// Link to problem: https://www.hackerrank.com/challenges/designer-pdf-viewer

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

function designerPdfViewer(h, word) {
    let highestLetter = 0;
    word.split("").forEach(letter => {
        if (h[letter.charCodeAt() - 97] > highestLetter) {
            highestLetter = currentHeight;
        }
    })
    return word.length * highestLetter;
}

function main() {
    const ws = fs.createWriteStream(process.env.OUTPUT_PATH);

    const h = readLine().replace(/\s+$/g, '').split(' ').map(hTemp => parseInt(hTemp, 10));

    const word = readLine();

    const result = designerPdfViewer(h, word);

    ws.write(result + '\n');

    ws.end();
}
