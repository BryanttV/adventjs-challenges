// Challenge #9: 🚂 The Magic Train.

/**
 * @param {string[]} board - Represent the train situation
 * @param {'U' | 'D' | 'R' | 'L' } mov - Movement direction
 * @returns {'none' | 'crash' | 'eat'}
 */
function moveTrain(board, mov) {
  const width = board[0].length - 1;
  const height = board.length - 1;
  const movements = {
    o: "crash",
    "*": "eat",
    "·": "none",
  };

  for (let index = 0; index < board.length; index++) {
    const position = board[index].indexOf("@");
    if (position !== -1) {
      const directions = {
        U: index > 0 ? board[index - 1][position] : "o",
        D: index < height ? board[index + 1][position] : "o",
        R: position < width ? board[index][position + 1] : "o",
        L: position > 0 ? board[index][position - 1] : "o",
      };
      return movements[directions[mov]];
    }
  }
}

const board = ["·····", "*····", "@····", "o····", "o····"];

console.log(moveTrain(board, "U"));
// ➞ 'eat'
// Because the train moves up and finds a magical fruit

console.log(moveTrain(board, "D"));
// ➞ 'crash'
// The train moves down and the head crashes into itself

console.log(moveTrain(board, "L"));
// ➞ 'crash'
// The train moves to the left and crashes into the wall

console.log(moveTrain(board, "R"));
// ➞ 'none'
// The train moves to the right and there is empty space on the right
