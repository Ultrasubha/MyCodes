const fs = require("fs").promises;

function execute() {
  fs.readFile("./lipsum_1.txt", "utf8")
    .then((data) => {
      const upperContent = data.toUpperCase();
      return fs.writeFile("file1.txt", upperContent);
    })
    .then(() => {
      console.log("file1.txt created successfully.");
      return fs.readFile("file1.txt", "utf8");
    })
    .then((upperData) => {
      const lowerContent = upperData.toLowerCase();
      const sentences = lowerContent.split(".");
      const formattedContent = sentences.join(".\n");
      return fs.writeFile("file2.txt", formattedContent);
    })
    .then(() => {
      console.log("file2.txt created successfully.");
      return Promise.all([
        fs.readFile("file1.txt", "utf8"),
        fs.readFile("file2.txt", "utf8")
      ]);
    })
    .then(([data1, data2]) => {
      const sortedContent = data1.concat(data2).split("\n").sort().join("\n");
      return fs.writeFile("file3.txt", sortedContent);
    })
    .then(() => {
      console.log("file3.txt created successfully.");
      return fs.writeFile(
        "filenames.txt",
        "file1.txt\nfile2.txt\nfile3.txt\n"
      );
    })
    .then(() => {
      console.log("filenames.txt updated successfully.");
      return fs.readFile("filenames.txt", "utf8");
    })
    .then((filenames) => {
      const filesToDelete = filenames
        .split("\n")
        .filter((filename) => filename.trim() !== "");
      return Promise.all(
        filesToDelete.map((file) => fs.unlink(file).then(() => file))
      );
    })
    .then((deletedFiles) => {
      deletedFiles.forEach((file) => {
        console.log(`${file} deleted successfully.`);
      });
    })
    .catch((err) => {
      console.error(err);
    });
}

module.exports.execute = execute;
