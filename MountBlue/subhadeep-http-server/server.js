const http = require("http");

const server = http.createServer((req, res) => {
  const { method, url } = req;

  // Handling different endpoints
  if (method === "GET" && url === "/html") {
    const htmlContent = `
      <!DOCTYPE html>
      <html>
        <head>
        </head>
        <body>
            <h1>Any fool can write code that a computer can understand. Good programmers write code that humans can understand.</h1>
            <p> - Martin Fowler</p>
        </body>
      </html>
    `;
    res.writeHead(200, { "Content-Type": "text/html" });
    res.end(htmlContent);

  } else if (method === "GET" && url === "/json") {
    const jsonData = {
      slideshow: {
        author: "Yours Truly",
        date: "date of publication",
        slides: [
          {
            title: "Wake up to WonderWidgets!",
            type: "all",
          },
          {
            items: [
              "Why <em>WonderWidgets</em> are great",
              "Who <em>buys</em> WonderWidgets",
            ],
            title: "Overview",
            type: "all",
          },
        ],
        title: "Sample Slide Show",
      },
    };
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(jsonData));

  } else if (method === "GET" && url === "/uuid") {
    const uuid = require("uuid").v4();
    const response = { uuid };
    res.writeHead(200, { "Content-Type": "application/json" });
    res.end(JSON.stringify(response));

  } else if (url.startsWith("/status/")) {
    const statusCode = parseInt(url.split("/")[2]);
    //console.log(statusCode);
    res.writeHead(statusCode, { "Content-Type": "text/plain" });
    res.end(`Response with status code: ${statusCode}`);

  } else if (url.startsWith("/delay/")) {
    const delayInSeconds = parseInt(url.split("/")[2]);
    setTimeout(() => {
      res.writeHead(200, { "Content-Type": "text/plain" });
      res.end(`Response after ${delayInSeconds} seconds`);
    }, delayInSeconds * 1000);
    
  } else {
    res.writeHead(404, { "Content-Type": "text/plain" });
    res.end("Not Found");
  }
});

const PORT = 3000;
server.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
