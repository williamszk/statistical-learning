// https://www.hackerrank.com/challenges/magic-square-forming/problem?isFullScreen=true


const formingMagicSquare = (s) => {

    const toFindDuplicates = arry => arry.filter((item, index) => arry.indexOf(item) !== index);
    // const arry = [1, 2, 1, 3, 4, 3, 5];
    // const arry = [5, 2, 1, 3, 4, 3, 5];
    // const duplicateElements = toFindDuplicates(arry);
    // console.log(duplicateElements);

    let arry = [];
    for (let i = 0; i < s.length; i++) {
        arry = arry.concat(...s[i])
    }
    // console.log(arry)

    let repeatedNums = toFindDuplicates(arry);

    const findMissingNums = (arry) => {
        let missingNums = [];
        for (let i = 1; i <= 9; i++ ) {
            if (!arry.includes(i)) missingNums.push(i);
        }
        return missingNums;
    }

    let missingNums = findMissingNums(arry);

    // is there any line or column or diagonal that don't have the repeated nums?
    // find them, and find the sum and compare

    console.log("repeatedNums: " + repeatedNums);
    console.log("missingNums: " + missingNums);

    return  0
}

s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]; // expected answer 7
console.log(formingMagicSquare(s) === 7);

s = [[4, 9, 2], [3, 5, 7], [8, 1, 5]]; // expected answer 1
console.log(formingMagicSquare(s) === 1);

s = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]; // expected answer 4
console.log(formingMagicSquare(s) === 4);