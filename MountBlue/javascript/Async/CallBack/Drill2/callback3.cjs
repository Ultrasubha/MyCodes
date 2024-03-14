/* 
	Problem 3: Write a function that will return all cards that belong to a particular list based on the listID that is passed to it from the given data in cards.json. Then pass control back to the code that called it by using a callback function.
*/

function getCardsForList(listId, cardsData, callback) {
  if (cardsData.hasOwnProperty(listId)) {
    callback(null, cardsData[listId] || []);
  } else {
    callback("Board not found", null);
  }
}

function callbackFunction3(error, cardsForList) {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log(`Cards for the list:`);
    for (const card of cardsForList) {
      console.log(`ID: ${card.id}, Description: ${card.description}`);
    }
  }
}

module.exports.getCardsForList = getCardsForList;
module.exports.callbackFunction3 = callbackFunction3;
