const boardsList = require("../Data/boards_1.json");
const getBoardInformation = require("../callback1.cjs").getBoardInformation;
const callbackFunction1 = require("../callback1.cjs").callbackFunction1;

getBoardInformation("abc122dc", boardsList, callbackFunction1);
