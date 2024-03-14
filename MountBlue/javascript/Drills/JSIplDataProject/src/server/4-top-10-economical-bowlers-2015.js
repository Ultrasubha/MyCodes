const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to filter match IDs for a specific year
function filterMatchIdsByYear(matches, targetYear) {
  return matches
    .filter((match) => match["season"] === targetYear)
    .map((match) => parseInt(match["id"]));
}

// Function to calculate economy for each bowler
function calculateBowlerEconomy(deliveries, matchIds) {
  const bowlerToRunDict = {};

  for (const delivery of deliveries) {
    const matchId = parseInt(delivery["match_id"]);
    if (matchIds.includes(matchId)) {
      const bowler = delivery["bowler"];
      const runs = parseInt(delivery["total_runs"]);

      if (!(bowler in bowlerToRunDict)) {
        bowlerToRunDict[bowler] = [0, 0];
      }

      bowlerToRunDict[bowler][0] += 1;
      bowlerToRunDict[bowler][1] += runs;
    }
  }

  for (const [bowler, tempList] of Object.entries(bowlerToRunDict)) {
    const economy = (tempList[1] / tempList[0]) * 6;
    tempList.splice(0, tempList.length, economy);
  }

  const sortedBowlerEconomy = Object.fromEntries(
    Object.entries(bowlerToRunDict)
      .sort((a, b) => {
        return a[1][0] - b[1][0];
      })
      .slice(0, 10)
  );

  return sortedBowlerEconomy;
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

// Function to handle the parsing and analysis of matches and deliveries data
function analyzeTopEconomicalBowlersData(
  matchesFilePath,
  deliveriesFilePath,
  outputFileName,
  targetYear
) {
  const matchParser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing matches CSV:", err);
      return;
    }

    const matchIds = filterMatchIdsByYear(matches, targetYear);
    const deliveriesParser = parse(
      { columns: true },
      function (err, deliveries) {
        if (err) {
          console.error("Error parsing deliveries CSV:", err);
          return;
        }

        const resultData = calculateBowlerEconomy(deliveries, matchIds);
        console.log(resultData);

        const writeResultStatus = writeDataToFile(resultData, outputFileName);
        console.log(writeResultStatus);
      }
    );

    fs.createReadStream(deliveriesFilePath).pipe(deliveriesParser);
  });

  fs.createReadStream(matchesFilePath).pipe(matchParser);
}

// Specify the file paths for matches data, deliveries data, and output file name
const matchesFilePath = path.join(basePath, "data", "matches.csv");
const deliveriesFilePath = path.join(basePath, "data", "deliveries.csv");
const outputFileName = "4-top-10-economical-bowlers-2015.json";
const targetYear = "2015";

// Call the function to analyze top economical bowlers data
analyzeTopEconomicalBowlersData(
  matchesFilePath,
  deliveriesFilePath,
  outputFileName,
  targetYear
);
