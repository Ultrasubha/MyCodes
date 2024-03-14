const fs = require("fs");

function execute() {
  // Step 1: Read lipsum.txt
  fs.readFile("./lipsum_1.txt", "utf8", (err, data) => {
    if (err) {
      console.error(err);
      return;
    }

    // Step 2: Converted to uppercase & written to file1.txt
    const upperContent = data.toUpperCase();
    fs.writeFile("file1.txt", upperContent, (err) => {
      if (err) {
        console.error(err);
        return;
      }

      console.log("file1.txt created successfully.");

      // Step 3: Read file1.txt, Converted to lowercase, split into sentences, and written to file2.txt
      fs.readFile("file1.txt", "utf8", (err, upperData) => {
        if (err) {
          console.error(err);
          return;
        }

        const lowerContent = upperData.toLowerCase();
        const sentences = lowerContent.split(".");
        const formattedContent = sentences.join(".\n");

        fs.writeFile("file2.txt", formattedContent, (err) => {
          if (err) {
            console.error(err);
            return;
          }

          console.log("file2.txt created successfully.");

          // Step 4: Read file1.txt, file2.txt,     sort content,    and written to file3.txt
          fs.readFile("file1.txt", "utf8", (err, data1) => {
            if (err) {
              console.error(err);
              return;
            }

            fs.readFile("file2.txt", "utf8", (err, data2) => {
              if (err) {
                console.error(err);
                return;
              }

              const sortedContent = data1
                .concat(data2)
                .split("\n")
                .sort()
                .join("\n");
              fs.writeFile("file3.txt", sortedContent, (err) => {
                if (err) {
                  console.error(err);
                  return;
                }

                console.log("file3.txt created successfully.");

                // Step 5: Store the names of file1.txt, file2.txt,file3.txt in filenames.txt
                fs.appendFile(
                  "filenames.txt",
                  "file1.txt\nfile2.txt\nfile3.txt\n",
                  (err) => {
                    if (err) {
                      console.error(err);
                      return;
                    }

                    console.log("filenames.txt updated successfully.");

                    // Step 6: Read filenames.txt and delete file1.txt, file2.txt,file3.txt
                    fs.readFile("filenames.txt", "utf8", (err, filenames) => {
                      if (err) {
                        console.error(err);
                        return;
                      }

                      const filesToDelete = filenames
                        .split("\n")
                        .filter((filename) => filename.trim() !== "");
                      filesToDelete.forEach((file) => {
                        fs.unlink(file, (err) => {
                          if (err) {
                            console.error(err);
                            return;
                          }
                          console.log(`${file} deleted successfully.`);
                        });
                      });
                    });
                  }
                );
              });
            });
          });
        });
      });
    });
  });
}

module.exports.execute = execute;
