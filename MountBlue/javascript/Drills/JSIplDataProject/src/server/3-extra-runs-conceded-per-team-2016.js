const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to filter match IDs for a specific year
function filterMatchIdsByYear(matches, targetYear) {
  return matches
    .filter((match) => parseInt(match["season"]) === targetYear)
    .map((match) => match["id"]);
}

// Function to calculate extra runs conceded per team in a specific year
function calculateExtraRunsConcededByTeam(deliveries, matchIds) {
  const extraRunsByTeam = {};

  for (const delivery of deliveries) {
    const team = delivery["bowling_team"];
    const extraRun = parseInt(delivery["extra_runs"]);

    if (matchIds.includes(delivery["match_id"])) {
      extraRunsByTeam[team] = (extraRunsByTeam[team] || 0) + extraRun;
    }
  }

  return extraRunsByTeam;
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
function analyzeExtraRunsConcededData(
  matchesFilePath,
  deliveriesFilePath,
  outputFileName,
  targetYear
) {
  const matchParser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing CSV:", err);
      return;
    }

    const matchIds = filterMatchIdsByYear(matches, targetYear);
    const deliveriesParser = parse(
      { columns: true },
      function (err, deliveries) {
        if (err) {
          console.error("Error parsing CSV:", err);
          return;
        }

        const resultData = calculateExtraRunsConcededByTeam(
          deliveries,
          matchIds
        );
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
const outputFileName = "3-extra-runs-conceded-per-team-2016.json";
const targetYear = 2016;

// Call the function to analyze extra runs conceded data
analyzeExtraRunsConcededData(
  matchesFilePath,
  deliveriesFilePath,
  outputFileName,
  targetYear
);
