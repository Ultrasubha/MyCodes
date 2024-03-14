/* 
    Q.1)Using callbacks and the fs module's asynchronous functions, do the following:
        1. Create a directory of random JSON files
        2. Delete those files simultaneously  
*/
const fs = require("fs");
const path = require("path");
const { v4: uuidv4 } = require("uuid");

const directoryPath = "./randomJSONFiles";

const createRandomJSONFiles = (numberOfFiles, callback) => {
  fs.mkdir(directoryPath, { recursive: true }, (err) => {
    if (err) {
      return callback(err);
    }

    const filePaths = [];

    for (let fileCount = 0; fileCount < numberOfFiles; fileCount++) {
      const fileName = path.join(directoryPath, `file_${uuidv4()}.json`);
      const fileContent = { data: Math.random() };

      fs.writeFile(fileName, JSON.stringify(fileContent), (err) => {
        if (err) {
          return callback(err);
        }
        filePaths.push(fileName);

        if (filePaths.length === numberOfFiles) {
          callback(null, filePaths);
        }
      });
    }
  });
};

const deleteFiles = (filePaths, callback) => {
  let deletedCount = 0;

  filePaths.forEach((filePath) => {
    fs.unlink(filePath, (err) => {
      if (err) {
        return callback(err);
      }
      deletedCount++;

      if (deletedCount === filePaths.length) {
        callback(null, filePaths);
      }
    });
  });
};

module.exports.createRandomJSONFiles = createRandomJSONFiles;
module.exports.deleteFiles = deleteFiles;
