// 03. Organizing The Inventory.

/**
 * @param {{ name: string, quantity: number, category: string }[]} inventory
 * @returns {object} The organized inventory
 */
function organizeInventory(inventory) {
  const organizedInventory = {};

  inventory.forEach((obj) => {
    const { category, quantity, name } = obj;
    if (category in organizedInventory) {
      if (name in organizedInventory[category]) {
        organizedInventory[category][name] += quantity;
      } else {
        organizedInventory[category][name] = quantity;
      }
    } else {
      organizedInventory[category] = { [name]: quantity };
    }
  });

  return organizedInventory;
}

const inventory = [
  { name: "doll", quantity: 5, category: "toys" },
  { name: "car", quantity: 3, category: "toys" },
  { name: "ball", quantity: 2, category: "sports" },
  { name: "car", quantity: 2, category: "toys" },
  { name: "racket", quantity: 4, category: "sports" },
];

console.log(organizeInventory(inventory));

// Expected result:
// {
//   toys: {
//     doll: 5,
//     car: 5
//   },
//   sports: {
//     ball: 2,
//     racket: 4
//   }

const inventory2 = [
  { name: "book", quantity: 10, category: "education" },
  { name: "book", quantity: 5, category: "education" },
  { name: "paint", quantity: 3, category: "art" },
];

console.log(organizeInventory(inventory2));

// Expected result:
// {
//   education: {
//     book: 15
//   },
//   art: {
//     paint: 3
//   }
// }
