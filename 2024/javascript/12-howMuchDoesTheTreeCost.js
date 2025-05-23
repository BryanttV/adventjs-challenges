// Challenge #12: 💵 How Much Does The Tree Cost?

/** @param {string} ornaments
 * @return {number} - The price of the tree
 */
function calculatePrice(ornaments) {
  const values = { "*": 1, o: 5, "^": 10, "#": 50, "@": 100 };
  let total = 0;
  let prevValue = 0;

  for (let index = ornaments.length - 1; index >= 0; index--) {
    const value = values[ornaments[index]];
    if (!value) {
      return undefined;
    }
    total += value < prevValue ? -value : value;
    prevValue = value;
  }
  return total;
}

console.log(calculatePrice("***")); // 3 (1 + 1 + 1)
console.log(calculatePrice("*o")); // 4 (5 - 1)
console.log(calculatePrice("o*")); // 6 (5 + 1)
console.log(calculatePrice("*o*")); // 5 (-1 + 5 + 1)
console.log(calculatePrice("**o*")); // 6 (1 - 1 + 5 + 1)
console.log(calculatePrice("o***")); // 8 (5 + 3)
console.log(calculatePrice("*o@")); // 94 (-5 - 1 + 100)
console.log(calculatePrice("*#")); // 49 (-1 + 50)
console.log(calculatePrice("@@@")); // 300 (100 + 100 + 100)
console.log(calculatePrice("#@")); // 50 (-50 + 100)
console.log(calculatePrice("#@Z")); // undefined (Z is unknown)
