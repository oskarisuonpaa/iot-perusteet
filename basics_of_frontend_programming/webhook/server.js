const express = require("express");
const dotenv = require("dotenv");

dotenv.config();

const app = express();
const PORT = 3000;
const DISCORD_WEBHOOK_URL = process.env.DISCORD_WEBHOOK_URL || "";

app.use(express.json());

app.post("/notify", async (request, response) => {
  const { message } = request.body;

  if (!message) {
    return response.status(400).json({ error: "Message is required" });
  }

  try {
    const discordResponse = await fetch(DISCORD_WEBHOOK_URL, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ content: message }),
    });

    if (!discordResponse.ok) {
      throw new Error("Failed to send message to Discord");
    }

    response.status(200).json({ success: true });
  } catch (error) {
    response.status(500).json({ error: error.message });
  }
});

app.listen(PORT, () => {
  console.log(`Server is running on 127.0.0.1:${PORT}`);
});
