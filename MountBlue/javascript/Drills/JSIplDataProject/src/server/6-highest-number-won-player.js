const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to find a player who has won the highest number of Player of the Match awards for each season
function findHighestPlayerOfTheMatchAwards(matches) {
  const playerOfTheMatchAwards = {};

  for (const match of matches) {
    const playerOfTheMatch = match["player_of_match"];

    if (playerOfTheMatchAwards.hasOwnProperty(playerOfTheMatch)) {
      playerOfTheMatchAwards[playerOfTheMatch] += 1;
    } else {
      playerOfTheMatchAwards[playerOfTheMatch] = 0;
    }
  }

  return findHighestValueAndKey(playerOfTheMatchAwards);
}

// Function to find the key with the highest value in an object
function findHighestValueAndKey(obj) {
  let highestValue = null;
  let highestKey = null;

  for (let key in obj) {
    if (obj.hasOwnProperty(key)) {
      if (highestValue === null || obj[key] > highestValue) {
        highestValue = obj[key];
        highestKey = key;
      }
    }
  }

  return { player: highestKey, playerOfMatchTimes: highestValue };
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
function analyzePlayerOfTheMatchData(filePath, outputFileName) {
  const parser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing CSV:", err);
      return;
    }

    const resultData = findHighestPlayerOfTheMatchAwards(matches);
    console.log(resultData);

    const writeResultStatus = writeDataToFile(resultData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for matches data and output file name
const matchesFilePath = path.join(basePath, "data", "matches.csv");
const outputFileName = "6-highest-number-won-player.json";

// Call the function to analyze Player of the Match data
analyzePlayerOfTheMatchData(matchesFilePath, outputFileName);
