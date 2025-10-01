const express = require("express");
const sqlite3 = require("sqlite3");
const app = express();
const PORT = 3000;

app.use(express.json());

const database = new sqlite3.Database("./database.db", (error) => {
  if (error) {
    console.error(error.message);
  } else {
    console.log("Connected to SQLite database");
  }
});

database.run(`CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
    )`);

app.get("/api/sensor", (_, response) => {
  response.json({
    temperature: 22.5,
    humidity: 55,
    status: "OK",
  });
});

app.get("/api/users", (_, response) => {
  database.all("SELECT * FROM users", (error, rows) => {
    if (error) {
      return response.status(500).json({ error: error.message });
    }

    response.json(rows);
  });
});

app.post("/api/users", (request, response) => {
  const { name, email } = request.body;

  database.run(
    `INSERT INTO users (name, email) VALUES (?,?)`,
    [name, email],
    (error) => {
      if (error) {
        return response.status(400).json({ error: error.message });
      }

      response.status(201).json({ id: this.lastID, name, email });
    }
  );
});

app.listen(PORT, () => {
  console.log(`Server listening on 127.0.0.1:${PORT}`);
});
