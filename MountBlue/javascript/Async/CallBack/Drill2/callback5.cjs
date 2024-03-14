/* 
	Problem 5: Write a function that will use the previously written functions to get the following information. You do not need to pass control back to the code that called it.

    Get information from the Thanos boards
    Get all the lists for the Thanos board
    Get all cards for the Mind and Space lists simultaneously
*/

//Q1 imports
const boardsList = require("./Data/boards_1.json");
const getBoardInformation = require("./callback1.cjs").getBoardInformation;
const callbackFunction1 = require("./callback1.cjs").callbackFunction1;


//Q2 imports
const listsData = require("./Data/lists_1.json");
const getListsForBoard = require("./callback2.cjs").getListsForBoard;
const callbackFunction2 = require("./callback2.cjs").callbackFunction2;


//Q3 imports
const cardsData = require("./Data/cards_1.json");
const getCardsForList = require("./callback3.cjs").getCardsForList;
const callbackFunction3 = require("./callback3.cjs").callbackFunction3;

//All Info
function getAllInformation() {
    getBoardInformation("mcu453ed", boardsList, callbackFunction1);
    getListsForBoard("mcu453ed", listsData, callbackFunction2);
    getCardsForList('qwsa221', cardsData, callbackFunction3);
    getCardsForList('jwkh245', cardsData, callbackFunction3);
}

module.exports.getAllInformation = getAllInformation;