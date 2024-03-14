createRandomJSONFiles = require("../problem1.cjs").createRandomJSONFiles;
deleteFiles = require("../problem1.cjs").deleteFiles;

const numberOfFiles = 5;

createRandomJSONFiles(numberOfFiles, (createErr, filePaths) => {
  if (createErr) {
    console.error("Error creating files:", createErr);
  } else {
    console.log("Files are", filePaths);

    // Deleting already created Files
    deleteFiles(filePaths, (deleteErr, deletedFilePaths) => {
      if (deleteErr) {
        console.error("Error deleting files:", deleteErr);
      } else {
        console.log("Files deleted:", deletedFilePaths);
      }
    });
  }
});

// Before running -> cd Async/Drill1/test
