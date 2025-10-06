const socket = new WebSocket("ws://localhost:8080");

socket.onopen = () => {
  document.getElementById("log").innerText = "Connected to server\n";
};

socket.onmessage = (event) => {
  document.getElementById("log").innerText += `Received: ${event.data}\n`;
};

function sendMessage() {
  const input = document.getElementById("msg");
  const message = input.value;
  socket.send(message);
  input.value = "";
}
