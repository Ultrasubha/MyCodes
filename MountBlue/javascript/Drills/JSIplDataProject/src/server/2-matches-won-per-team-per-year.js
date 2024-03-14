const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to calculate the number of matches won per team per year
function calculateMatchesWonPerTeamPerYear(matches) {
  const matchesWonPerTeamPerYear = {};

  for (const match of matches) {
    const year = match["season"];
    const winner = match["winner"];

    matchesWonPerTeamPerYear[year] = matchesWonPerTeamPerYear[year] || {};
    matchesWonPerTeamPerYear[year][winner] =
      (matchesWonPerTeamPerYear[year][winner] || 0) + 1;
  }

  return {
    teams: new Set(
      Object.keys(matchesWonPerTeamPerYear).flatMap((year) =>
        Object.keys(matchesWonPerTeamPerYear[year])
      )
    ),
    years: Object.keys(matchesWonPerTeamPerYear).sort(),
    matchesWonPerTeamPerYear,
  };
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
function analyzeMatchesData(filePath, outputFileName) {
  const parser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing CSV:", err);
      return;
    }

    const resultData = calculateMatchesWonPerTeamPerYear(matches);
    console.log(resultData);

    const writeResultStatus = writeDataToFile(resultData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for matches data and output file name
const matchesFilePath = path.join(basePath, "data", "matches.csv");
const outputFileName = "2-matches-won-per-team-per-year.json";

// Call the function to analyze matches data
analyzeMatchesData(matchesFilePath, outputFileName);
