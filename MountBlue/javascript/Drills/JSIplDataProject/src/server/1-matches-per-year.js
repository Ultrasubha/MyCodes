const { parse } = require("csv-parse");
const fs = require("fs");
const path = require("path");

// Specify the base path
const basePath =
  "/home/urahara/Documents/javascript/Drills/JSIplDataProject/src";

// Function to calculate the number of matches played per year
function calculateMatchesPerYear(matches) {
  const years = {};

  for (const match of matches) {
    const year = match["season"];

    if (years.hasOwnProperty(year)) {
      years[year] += 1;
    } else {
      years[year] = 1; // Initialize for the first match in the year
    }
  }

  return years;
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

    const yearsData = calculateMatchesPerYear(matches);
    console.log(yearsData);

    const writeResultStatus = writeDataToFile(yearsData, outputFileName);
    console.log(writeResultStatus);
  });

  fs.createReadStream(filePath).pipe(parser);
}

// Specify the file path for matches data and output file name
const matchesFilePath = path.join(basePath, "data", "matches.csv");
const outputFileName = "1-matches-per-year.json";

// Call the function to analyze matches data
analyzeMatchesData(matchesFilePath, outputFileName);
