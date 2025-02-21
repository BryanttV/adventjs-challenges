// 02. Framing Names.

/**
 * @param {string[]} names - Array of names to frame
 * @returns {string} The framed names
 */
function createFrame(names) {
  const width = Math.max(...names.map((name) => name.length)) + 4;
  const frame = ["*".repeat(width)];

  names.forEach((name) => {
    frame.push(`* ${name.padEnd(width - 4, " ")} *`);
  });

  frame.push("*".repeat(width));

  return frame.join("\n");
}

console.log(createFrame(["midu", "madeval", "educalvolpz"]));

// Expected result:
// ***************
// * midu        *
// * madeval     *
// * educalvolpz *
// ***************

console.log(createFrame(["midu"]));

// Expected result:
// ********
// * midu *
// ********

console.log(createFrame(["a", "bb", "ccc"]));

// Expected result:
// *******
// * a   *
// * bb  *
// * ccc *
// *******

console.log(createFrame(["a", "bb", "ccc", "dddd"]));
// ********
// * a    *
// * bb   *
// * ccc  *
// * dddd *
// ********
