const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Find the highest number of times one player has been dismissed by another player
function findHighestDismissedPlayer(deliveries) {
  const dismissArr = allDismissedPlayers(deliveries);

  // Sort(descending order) based on the count of dismissals
  dismissArr.sort((a, b) => b[1] - a[1]);
  highestArr = (dismissArr[0][0]).split("@")
  playerDismissed = highestArr[0]
  dismissedBy = highestArr[1] // Not printing
  dismissedTimes = dismissArr[0][1]

  return { playerDismissed: playerDismissed, dismissedTimes:  dismissedTimes};
}

function allDismissedPlayers(deliveries) {
  const dismissCount = {};

  for (let index = 0; index < deliveries.length; index++) {
    let dismissPlayer = deliveries[index].player_dismissed;

    if (dismissPlayer) {
      dismissPlayer += "@" + deliveries[index].bowler;
      dismissCount[dismissPlayer] = dismissCount.hasOwnProperty(dismissPlayer)
        ? dismissCount[dismissPlayer] + 1
        : 1;
    }
  }

  const dismissArr = Object.entries(dismissCount);
  return dismissArr;
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

// Function to handle the parsing and analysis of deliveries data
function analyzePlayerOfTheDeliveriesData(filePath, outputFileName) {
  const parser = parse({ columns: true }, function (err, deliveries) {
    if (err) {
      console.error("Error parsing CSV:", err);
      return;
    }

    let resultData = findHighestDismissedPlayer(deliveries);
    console.log(resultData);

    const writeResultStatus = writeDataToFile(resultData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for deliveries data and output file name
const deliveriesFilePath = path.join(basePath, "data", "deliveries.csv");
const outputFileName = "8-times-one-player-dismissed.json";

// Call the function to analyze Player of the deliveries data
analyzePlayerOfTheDeliveriesData(deliveriesFilePath, outputFileName);
