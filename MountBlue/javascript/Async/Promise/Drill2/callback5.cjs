/* 
	Problem 5: Write a function that will use the previously written functions to get the following information. You do not need to pass control back to the code that called it.

    Get information from the Thanos boards
    Get all the lists for the Thanos board
    Get all cards for the Mind and Space lists simultaneously
*/

//Q1 imports
const wrappedGetBoardInformation =
  require("./test/testCallback1.cjs").wrappedGetBoardInformation;

//Q2 imports
const wrappedGetListsForBoard =
  require("./test/testCallback2.cjs").wrappedGetListsForBoard;

//Q3 imports
const wrappedGetCardsForList =
  require("./test/testCallback3.cjs").wrappedGetCardsForList;

//All Info
function getAllInformation() {
  wrappedGetBoardInformation("mcu453ed");
  wrappedGetListsForBoard("mcu453ed");
  wrappedGetCardsForList("qwsa221");
  wrappedGetCardsForList("jwkh245");
}

module.exports.getAllInformation = getAllInformation;
