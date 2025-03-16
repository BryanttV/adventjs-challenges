// Challenge #11: 🏴‍☠️ Filenames Encoded.

/**
 * @param {string} filename - The filename to decode.
 * @returns {string} The decoded filename.
 */
function decodeFilename(filename) {
  const regex = /(\d+)_([a-zA-Z_-]+.\w+)/
  return filename.match(regex)[2];
}

console.log(decodeFilename("2023122512345678_sleighDesign.png.grinchwa"));
// ➞ "sleighDesign.png"

console.log(decodeFilename("42_chimney_dimensions.pdf.hack2023"));
// ➞ "chimney_dimensions.pdf"

console.log(decodeFilename("987654321_elf-roster.csv.tempfile"));
// ➞ "elf-roster.csv"
