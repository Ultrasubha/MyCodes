const boardsList = require("../Data/boards_1.json");
const getBoardInformation = require("../callback1.cjs").getBoardInformation;
const callbackFunction1 = require("../callback1.cjs").callbackFunction1;

function wrappedGetBoardInformation(id) {
  getBoardInformation(id, boardsList)
    .then((boardInfo) => {
      callbackFunction1(null, boardInfo);
    })
    .catch((err) => {
      callbackFunction1(err, null);
    });
}

wrappedGetBoardInformation("abc122dc");
module.exports.wrappedGetBoardInformation = wrappedGetBoardInformation;
