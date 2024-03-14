// Find the bowler with the best economy in super overs

const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Find the bowler with the best economy in super overs
function findHighestEconomyBowler(deliveries) {
  const economyMap = generateEconomyMap(deliveries);

  let bestEconomyBowler = null;
  let bestEconomy = null;

  for (const bowler in economyMap) {
    // Finding best economy bowler
    const economy = (economyMap[bowler].runs / economyMap[bowler].balls) * 6;
    if (bestEconomyBowler === null || economy < bestEconomy) {
      bestEconomyBowler = bowler;
      bestEconomy = economy.toFixed(2);
    }
  }

  return { bestEconomyBowler, bestEconomy };
}

function generateEconomyMap(deliveries) {
  const economyMap = {};

  for (let index = 0; index < deliveries.length; index++) {
    const delivery = deliveries[index];

    // Check if the delivery is part of a super over
    if (delivery.is_super_over === "1") {
      const bowler = delivery.bowler;
      const totalRuns =
        parseInt(delivery.batsman_runs) +
        parseInt(delivery.extra_runs) -
        parseInt(delivery.legbye_runs) -
        parseInt(delivery.bye_runs);
      const balls = 1; // Each delivery in a super over is considered a ball

      if (!economyMap[bowler]) {
        economyMap[bowler] = { runs: 0, balls: 0 };
      }

      economyMap[bowler].runs += totalRuns;
      economyMap[bowler].balls += balls;
    }
  }
  return economyMap;
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

    let resultData = findHighestEconomyBowler(deliveries);
    console.log(resultData);

    const writeResultStatus = writeDataToFile(resultData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for deliveries data and output file name
const deliveriesFilePath = path.join(basePath, "data", "deliveries.csv");
const outputFileName = "9-best-economy-bowler.json";

// Call the function to analyze Player of the deliveries data
analyzePlayerOfTheDeliveriesData(deliveriesFilePath, outputFileName);
