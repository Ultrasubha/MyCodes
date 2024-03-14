const listsData = require("../Data/lists_1.json");
const getListsForBoard = require("../callback2.cjs").getListsForBoard;
const callbackFunction2 = require("../callback2.cjs").callbackFunction2;

// Call the function with a board ID and the callback function
getListsForBoard("abc122dc", listsData)
  .then((listData) => {
    callbackFunction2(null, listData);
  })
  .catch((err) => {
    callbackFunction2(err, null);
  });
