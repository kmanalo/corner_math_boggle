// https://jsfiddle.net/SoonDead/rd2GN/3/

var start = [1, 1],
    goal = [5, 5],
    pathList = [],
    //solutionList = [],
    solutionCount = 0,
    width = 5,
    height = 5;


function squareInArray(square, array) {
    var i = 0,
        x = square[0],
        y = square[1];

    for (i = 0; i < array.length; i++) {
        if (x == array[i][0] && y == array[i][1]) {
            return true;
        }
    }
    return false;
}


function visit(square) {
    var i = 0,
        x = square[0],
        y = square[1],
        adjacencies = [[x - 1, y], [x + 1, y], [x, y + 1], [x, y - 1]];

    pathList.push(square);

    if (x == goal[0] && y == goal[1]) {
        var solution = pathList.slice(0); //copy trick
        //solutionList.push(solution);
        solutionCount++;
        document.write('<p>' + solutionCount + '. solution: ' + solution + '</p>');
    }
    else {
        for (i = 0; i < adjacencies.length; i++) {
            if (adjacencies[i][0] < 1 || adjacencies[i][0] > width || adjacencies[i][1] < 1 || adjacencies[i][1] > height) {
                //overflow
            }
            else {
                if (squareInArray(adjacencies[i], pathList)) {
                    //do nothing we have already been here
                }
                else {
                    visit(adjacencies[i]);
                }
            }
        }
    }
    pathList.pop();
}

visit(start);
document.write('<p>Total count: ' + solutionCount + '</p>');
