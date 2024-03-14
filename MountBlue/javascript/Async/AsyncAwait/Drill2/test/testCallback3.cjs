const cardsData = require("../Data/cards_1.json");
const getCardsForList = require("../callback3.cjs").getCardsForList;
const callbackFunction3 = require("../callback3.cjs").callbackFunction3;

// Call the function with a list ID and the callback function
getCardsForList("qwsa221", cardsData)
  .then((cardData) => {
    callbackFunction3(null, cardData);
  })
  .catch((err) => {
    callbackFunction3(err, null);
  });
