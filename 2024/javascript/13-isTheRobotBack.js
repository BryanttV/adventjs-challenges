/** @param {string} moves
 * @returns {true|[number, number]} Return true if robot returns or position
 */
function isRobotBack(moves) {
  const pairs = { R: "L", L: "R", U: "D", D: "U" };
  const movesList = Array.from(moves);
  let x = 0;
  let y = 0;

  const finalMoves = [];
  let index = 0;

  while (index < movesList.length) {
    const move = movesList[index];
    if (move === "*") {
      finalMoves.push(movesList[index + 1]);
    } else if (move === "!") {
      finalMoves.push(pairs[movesList.splice(index + 1, 1)]);
    } else if (move === "?") {
      const nextValue = movesList.splice(index + 1, 1)[0];
      if (!finalMoves.includes(nextValue)) {
        finalMoves.push(nextValue);
      }
    } else {
      finalMoves.push(move);
    }
    index++;
  }

  finalMoves.forEach((move) => {
    if (move === "R") {
      x += 1;
    } else if (move === "L") {
      x -= 1;
    } else if (move === "U") {
      y += 1;
    } else if (move === "D") {
      y -= 1;
    }
  });

  return x || y ? [x, y] : true;
}

console.log(isRobotBack("R")); // [1, 0]
console.log(isRobotBack("RL")); // true
console.log(isRobotBack("RLUD")); // true
console.log(isRobotBack("*RU")); // [2, 1]
console.log(isRobotBack("R*U")); // [1, 2]
console.log(isRobotBack("LLL!R")); // [-4, 0]
console.log(isRobotBack("R?R")); // [1, 0]
console.log(isRobotBack("U?D")); // true
console.log(isRobotBack("R!L")); // [2, 0]
console.log(isRobotBack("U!D")); // [0, 2]
console.log(isRobotBack("R?L")); // true
console.log(isRobotBack("U?U")); // [0, 1]
console.log(isRobotBack("*U?U")); // [0, 2]
console.log(isRobotBack("U?D?U")); // true

// Step-by-step examples:
console.log(isRobotBack("R!U?U")); // [1, 0]
// 'R'  -> moves to the right
// '!U' -> inverts and becomes 'D'
// '?U' -> moves upwards, because the 'U' movement hasn't been done yet

console.log(isRobotBack("UU!U?D")); // [0, 1]
// 'U'  -> moves upwards
// 'U'  -> moves upwards
// '!U' -> inverts and becomes 'D'
// '?D' -> does not move, since the 'D' movement has already been done
