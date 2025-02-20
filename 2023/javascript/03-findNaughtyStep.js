function findNaughtyStep(original, modified) {
  if (original === modified) return "";
  const originalLen = original.length;
  const modifiedLen = modified.length;
  for (let i = 0; i < originalLen; i++) {
    if (original[i] !== modified[i]) {
      if (originalLen > modifiedLen) {
        return original[i];
      }
      return modified[i];
    }
  }
  return modified[original.length];
}

const original = "abcd";
const modified = "abcde";
console.log(findNaughtyStep(original, modified)); // 'e'

const original2 = "stepfor";
const modified2 = "stepor";
console.log(findNaughtyStep(original2, modified2)); // 'f'

const original3 = "abcde";
const modified3 = "abcde";
console.log(findNaughtyStep(original3, modified3)); // ''

const original4 = "xxxx";
const modified4 = "xxoxx";
console.log(findNaughtyStep(original4, modified4)); // 'o'
