// 07. The Grinch's Attack

/** @param {string} packages with parentheses
 *  @returns {string} Fixed and sorted packages
 */
function fixPackages(packages) {
  const regex = /\(\w+\)/;

  while (regex.test(packages)) {
    packages = packages.replace(regex, (match) =>
      [...match].slice(1, -1).reverse().join("")
    );
  }
  return packages;
}

console.log(fixPackages("a(cb)de"));
// ➞ "abcde"
// We reverse "cb" inside the parentheses

console.log(fixPackages("a(bc(def)g)h"));
// ➞ "agdefcbh"
// 1st we reverse "def" → "fed", then we reverse "bcfedg" → "gdefcb"

console.log(fixPackages("abc(def(gh)i)jk"));
// ➞ "abcighfedjk"
// 1st we reverse "gh" → "hg", then "defhgi" → "ighfed"

console.log(fixPackages("a(b(c))e"));
// ➞ "acbe"
// 1st we reverse "c" → "c", then "bc" → "cb"
