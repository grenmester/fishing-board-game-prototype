import { WebSocketServer } from "ws";

const PORT = 3000;

const genInitialGameState = () => {
  return {
    numDice: 1,
    diceRolls: [0],
  };
};

const broadcastGameState = () => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify({ type: "update", gameState }));
    }
  });
};

const sendError = (socket, error) => {
  console.error(error);
  socket.send(JSON.stringify({ type: "error", error }));
};

const wss = new WebSocketServer({ port: PORT });
let gameState = genInitialGameState();

wss.on("connection", (ws) => {
  console.info("Client connected");

  ws.on("message", (message) => {
    const data = JSON.parse(message.toString());
    console.debug(`message: ${JSON.stringify(data, null, 2)}`);
    switch (data.type) {
      case "addDie":
        if (gameState.numDice == 10) {
          sendError(ws, "Max number of dice is 10");
          return;
        }
        gameState.numDice++;
        gameState.diceRolls.push(0);
        break;
      case "removeDie":
        if (gameState.numDice == 1) {
          sendError(ws, "Min number of dice is 1");
          return;
        }
        gameState.numDice--;
        gameState.diceRolls.pop();
        break;
      case "rollDice":
        gameState.diceRolls = Array(gameState.numDice)
          .fill()
          .map(() => Math.floor(Math.random() * 6) + 1);
        break;
    }
    broadcastGameState();
  });

  ws.on("close", () => {
    console.info("Client disconnected, game reset");
    gameState = genInitialGameState();
  });
});

console.info(`The WebSocket server is running on port ${PORT}`);
