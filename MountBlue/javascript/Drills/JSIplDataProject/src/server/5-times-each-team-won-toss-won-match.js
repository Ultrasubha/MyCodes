const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to find the number of times each team won the toss and also won the match
function findTossAndMatchWinners(matches) {
  const tossAndMatchWinners = {};

  for (const match of matches) {
    const tossWinner = match["toss_winner"];
    const matchWinner = match["winner"];

    if (tossAndMatchWinners.hasOwnProperty(tossWinner)) {
      if (matchWinner === tossWinner) {
        tossAndMatchWinners[tossWinner] += 1;
      }
    } else {
      tossAndMatchWinners[tossWinner] = 0;
    }
  }

  return tossAndMatchWinners;
}

// Function to write data to a file and handle errors
const writeDataToFile = (result, outputFileName) => {
  try {
    const resultFilePath = path.join(
      basePath,
      "public",
      "output",
      outputFileName
    );
    fs.writeFileSync(resultFilePath, JSON.stringify(result, null, 2), "utf8");
    return "Output file successfully written";
  } catch (error) {
    console.error("Error writing to file:", error.message);
    return "Error writing to file";
  }
};

// Function to handle the parsing and analysis of matches data
function analyzeTossAndMatchWinnersData(filePath, outputFileName) {
  const parser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing CSV:", err);
      return;
    }

    const resultData = findTossAndMatchWinners(matches);
    console.log(resultData);

    const writeResultStatus = writeDataToFile(resultData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for matches data and output file name
const matchesFilePath = path.join(basePath, "data", "matches.csv");
const outputFileName = "5-times-each-team-won-toss-won-match.json";

// Call the function to analyze toss and match winners data
analyzeTossAndMatchWinnersData(matchesFilePath, outputFileName);
