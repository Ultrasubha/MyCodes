/* 
	Problem 1: Write a function that will return a particular board's information based on the boardID that is passed from the given list of boards in boards.json and then pass control back to the code that called it by using a callback function.
*/

function getBoardInformation(boardId, boardsList) {
  return new Promise((resolve, reject) => {
    const foundBoard = boardsList.find((board) => board.id === boardId);

    if (foundBoard) {
      resolve(foundBoard);
    } else {
      reject("Board not found");
    }
  });
}

function callbackFunction1(error, boardInfo) {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log("Board Information:");
    console.log(`ID: ${boardInfo.id}`);
    console.log(`Name: ${boardInfo.name}`);
    console.log(`Permissions: ${JSON.stringify(boardInfo.permissions)}`);
  }
}

module.exports.getBoardInformation = getBoardInformation;
module.exports.callbackFunction1 = callbackFunction1;
