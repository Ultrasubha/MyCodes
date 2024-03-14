const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Extracting id:year from matches
function matchIdAndSeasons(matches) {
  return matches.reduce((acc, match) => {
    acc[match.id] = match.season;
    return acc;
  }, {});
}

function generateBatsmanStrikeRate(matches, deliveries) {
  const batsmanStrikeRate = {};
  for (delivery of deliveries) {
    const batsman = delivery.batsman;
    const matchId = delivery.match_id;
    const season = matchIdAndSeasons(matches)[matchId];
    const totalRuns = parseInt(delivery.total_runs);
    const isWide = delivery.wide_runs !== "0";
    const isNoBall = delivery.noball_runs !== "0";

    if (!isWide && !isNoBall) {
      if (!batsmanStrikeRate[season]) {
        batsmanStrikeRate[season] = {};
      }

      if (!batsmanStrikeRate[season][batsman]) {
        batsmanStrikeRate[season][batsman] = { runs: 0, balls: 0 };
      }

      batsmanStrikeRate[season][batsman].runs += totalRuns;
      batsmanStrikeRate[season][batsman].balls += 1;
    }
  }
  return batsmanStrikeRate;
}

// Find the strike rate of a batsman for each season
function batsmanStrikeRate(matches, deliveries) {
  perSeasonStrikeRate = generateBatsmanStrikeRate(matches, deliveries);
  const strikeRates = {};

  for (const season in perSeasonStrikeRate) {
    strikeRates[season] = {};

    for (const batsman in perSeasonStrikeRate[season]) {
      const batsmanData = perSeasonStrikeRate[season][batsman];
      const strikeRate =
        batsmanData.balls > 0
          ? ((batsmanData.runs / batsmanData.balls) * 100).toFixed(2)
          : 0;
      strikeRates[season][batsman] = parseFloat(strikeRate);
    }
  }

  return strikeRates;
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
  outputFileName
) {
  const matchParser = parse({ columns: true }, function (err, matches) {
    if (err) {
      console.error("Error parsing matches CSV:", err);
      return;
    }

    const deliveriesParser = parse(
      { columns: true },
      function (err, deliveries) {
        if (err) {
          console.error("Error parsing deliveries CSV:", err);
          return;
        }

        const resultData = batsmanStrikeRate(matches, deliveries);
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
const outputFileName = "7-batsman-strike-rate.json";

// Call the function to analyze top economical bowlers data
analyzeTopEconomicalBowlersData(
  matchesFilePath,
  deliveriesFilePath,
  outputFileName
);
