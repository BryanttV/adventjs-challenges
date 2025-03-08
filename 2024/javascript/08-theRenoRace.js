// 08. The Reno Race

/**
 * @param {number[]} indices - The reno indices
 * @param {number} length - The length of the race
 * @returns {string} The reno race
 */
function drawRace(indices, length) {
  const reindeers = indices.length;
  const race = indices.map((value, index) => {
    let line = [..."~".repeat(length)];
    if (value !== 0) {
      const position = value > 0 ? value : length + value;
      line[position] = "r";
    }
    const spaces = " ".repeat(reindeers - index - 1);
    return [spaces, ...line, ` /${index + 1}`].join("");
  });
  return race.join("\n");
}

console.log(drawRace([0, 5, -3], 10));
/*
  ~~~~~~~~~~ /1
 ~~~~~r~~~~ /2
~~~~~~~r~~ /3
*/

console.log(drawRace([2, -1, 0, 5], 8));
/*
   ~~r~~~~~ /1
  ~~~~~~~r /2
 ~~~~~~~~ /3
~~~~~r~~ /4
*/

console.log(drawRace([3, 7, -2], 12));
/*
  ~~~r~~~~~~~~ /1
 ~~~~~~~r~~~~ /2
~~~~~~~~~~r~ /3
*/
