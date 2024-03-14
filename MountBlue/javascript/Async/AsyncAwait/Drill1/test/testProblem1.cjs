const { createRandomJSONFiles, deleteFiles } = require("../problem1.cjs");

const numberOfFiles = 5;

createRandomJSONFiles(numberOfFiles)
  .then((filePaths) => {
    console.log("Files are", filePaths);

    // Deleting already created Files
    return deleteFiles(filePaths);
  })
  .then((deletedFilePaths) => {
    console.log("Files deleted:", deletedFilePaths);
  })
  .catch((error) => {
    console.error("Error:", error);
  });
