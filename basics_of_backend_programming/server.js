const express = require("express");
const app = express();
const PORT = 3000;

app.get("/api/sensor", (request, response) => {
  response.json({
    temperature: 22.5,
    humidity: 55,
    status: "OK",
  });
});

app.listen(PORT, () => {
  console.log(`Server listening on 127.0.0.1:${PORT}`);
});
