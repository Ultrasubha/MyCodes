/* 
	Problem 2: Write a function that will return all lists that belong to a board based on the boardID that is passed to it from the given data in lists.json. Then pass control back to the code that called it by using a callback function.
*/

function getListsForBoard(boardId, listsData) {
  return new Promise((resolve,reject)=>{
    if (listsData.hasOwnProperty(boardId)) {
      resolve(listsData[boardId] || []);
    } else {
      reject("Board not found");
    }
  });
}

function callbackFunction2(error, listsForBoard) {
  if (error) {
    console.error("Error:", error);
  } else {
    console.log(`Lists for the board:`);
    for (const list of listsForBoard) {
      console.log(`ID: ${list.id}, Name: ${list.name}`);
    }
  }
}

module.exports.getListsForBoard = getListsForBoard;
module.exports.callbackFunction2 = callbackFunction2;
