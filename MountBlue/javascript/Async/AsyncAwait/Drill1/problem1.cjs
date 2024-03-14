/* 
    Q.1)Using callbacks and the fs module's asynchronous functions, do the following:
        1. Create a directory of random JSON files
        2. Delete those files simultaneously  
*/

const fs = require("fs").promises;
const path = require("path");
const { v4: uuidv4 } = require("uuid");

const directoryPath = "./randomJSONFiles";

const createRandomJSONFiles = (numberOfFiles) => {
  return fs.mkdir(directoryPath, { recursive: true }).then(() => {
    const filePaths = [];

    const createFile = (fileCount) => {
      if (fileCount < numberOfFiles) {
        const fileName = path.join(directoryPath, `file_${uuidv4()}.json`);
        const fileContent = { data: Math.random() };

        return fs.writeFile(fileName, JSON.stringify(fileContent)).then(() => {
          filePaths.push(fileName);
          return createFile(fileCount + 1);
        });
      } else {
        return filePaths;
      }
    };

    return createFile(0);
  });
};

const deleteFiles = (filePaths) => {
  return Promise.all(filePaths.map((filePath) => fs.unlink(filePath))).then(
    () => filePaths
  );
};

module.exports.createRandomJSONFiles = createRandomJSONFiles;
module.exports.deleteFiles = deleteFiles;
