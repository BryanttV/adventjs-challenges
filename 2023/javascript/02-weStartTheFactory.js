function manufacture(gifts, materials) {
  let validGifts = [...gifts];
  const materialsCharacters = materials.split("").sort();
  for (const gift of gifts) {
    const giftsCharacters = new Set(gift.split("").sort());
    for (const char of giftsCharacters) {
      if (!materialsCharacters.includes(char)) {
        validGifts.pop(gift);
        break;
      }
    }
  }
  return validGifts;
}

const gifts = ["tren", "oso", "pelota"];
const materials = "tronesa";
console.log(manufacture(gifts, materials)); // ["tren", "oso"]

const gifts2 = ["juego", "puzzle"];
const materials2 = "jlepuz";
console.log(manufacture(gifts2, materials2)); // ["puzzle"]

const gifts3 = ["libro", "ps5"];
const materials3 = "psli";
console.log(manufacture(gifts3, materials3)); // []
