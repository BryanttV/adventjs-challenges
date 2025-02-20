function maxDistance(movements) {
  const counter = (string, char) => string.split(char).length - 1;
  const left = counter(movements, "<");
  const right = counter(movements, ">");
  const both = counter(movements, "*");
  return left >= right ? left + both - right : right + both - left;
}

const movements = ">>*<";
const result = maxDistance(movements);
console.log(result); // -> 2

const movements2 = "<<<>";
const result2 = maxDistance(movements2);
console.log(result2); // -> 2

const movements3 = ">***>";
const result3 = maxDistance(movements3);
console.log(result3); // -> 5
