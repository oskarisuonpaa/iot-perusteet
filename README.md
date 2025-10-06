# IoT Perusteet

This repository contains my work for LAB's *IoT Perusteet* course.

> [!IMPORTANT]
> Majority of API keys and other sensitive data has been redacted. You need to provide your own API keys to run code that requires third-party APIs.

## Week 1 - Basics of embedded programming

Contains the following programs:
* `counter.py` -> Counts from 0 to 9.
* `name_checker.py` -> Prints different messages based on the user's input. Try your own name, then 'Clark Kent'.
* `blink_onboard_led.py` -> Blinks the onboard led, duh.
* `blink_onboard_led_optimized.py` -> Same functionality as above but better.
* `blink_external_led.py` -> Blinks an external led, duh.
* `blink_external_led_with_button.py` -> Control external led with button.
* `traffic_lights.py` -> Loops led lights. When button is pressed a buzzer makes a sound, and waits a second before continuing the loop.
* `interrup.py` -> Reaction game that times how long it takes for user to push a button after a led turns off.
* `burglary_alarm.py` -> Prints a message when a sensor detects movement.
* `weather_station.py` -> Prints weather sensor data.
* `weather_station_thing_speak.py` -> Sends weather sensor data to ThingSpeak. *Requires API key: `THINGSPEAK_WRITE_KEY`*.

## Week 2 - Basics of backend programming

Contains a simple Node Express server. Run the following commands `npm i && npm run start` then i.e. `curl localhost:3000/api/sensor` to get hardcoded data.

## Week 3 - Basics of API's and databases

Contains a simple Node Express server with SQLite3 database. Run the following commands `npm i && npm run start`.

Routes:
* GET /api/sensor
* GET /api/users
* POST /api/users
  * Body: {name: "test", email: "test@test.com"}  

## Week 4 - Basics of frontend programming

### Webhook

Contains a simple Node Express server with route to send messages to Discord webhook (*URL must be provided by you*). Create a `.env` file and add your Discord webhook url (DISCORD_WEBHOOK_URL). Run the following commands `npm i && npm run start`.

Routes:
* POST /notify
  * Body: {message: "Hello, World!"}  

### Web Socket

A fullstack app with simple frontend and websocket backend. Run the following commands `npm i && npm run start`. Then open `client.html` in browser. You can then send messages to the server.

### Fetch

A simple app that fetches sensor data from ThingSpeak and draws a chart based on it. Open the `fetch_temperature.html` in your browser.
