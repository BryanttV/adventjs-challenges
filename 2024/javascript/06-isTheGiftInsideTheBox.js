// Challenge #6: 📦 Is The Gift Inside The Box?

/** @param {string[]} box
 *  @returns {boolean} True if the gift is inside the box
 */
function inBox(box) {
  box = box.slice(1, -1);

  for (const line of box) {
    if (
      line.includes("*") &&
      line.indexOf("*") > 0 &&
      line.indexOf("*") < line.length - 1
    ) {
      return true;
    }
  }

  return false;
}

console.log(inBox(["###", "#*#", "###"])); // ➞ true
console.log(inBox(["####", "#* #", "#  #", "####"])); // ➞ true
console.log(inBox(["#####", "#   #", "#  #*", "#####"])); // ➞ false
console.log(inBox(["#####", "#   #", "#   #", "#   #", "#####"])); // ➞ false
