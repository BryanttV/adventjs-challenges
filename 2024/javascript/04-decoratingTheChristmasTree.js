// 04. Decorating The Christmas Tree.

/**
 * @param {number} height - Height of the tree
 * @param {string} ornament - Symbol to draw
 * @returns {string} Drawn tree
 */
function createXmasTree(height, ornament) {
  const xmasTree = [];
  const width = height * 2 - 1;

  for (let i = 1; i <= width + 1; i += 2) {
    const spaces = "_".repeat((width - i) / 2);
    const level = ornament.repeat(i);
    xmasTree.push(spaces + level + spaces);
  }

  const trunkSpaces = "_".repeat(width / 2);
  const trunk = `${trunkSpaces}#${trunkSpaces}`;
  xmasTree.push(trunk, trunk);

  return xmasTree.join("\n");
}

const tree = createXmasTree(5, "*");
console.log(tree);
/*
____*____
___***___
__*****__
_*******_
*********
____#____
____#____
*/

const tree2 = createXmasTree(3, "+");
console.log(tree2);
/*
__+__
_+++_
+++++
__#__
__#__
*/

const tree3 = createXmasTree(6, "@");
console.log(tree3);
/*
_____@_____
____@@@____
___@@@@@___
__@@@@@@@__
_@@@@@@@@@_
@@@@@@@@@@@
_____#_____
_____#_____
*/
