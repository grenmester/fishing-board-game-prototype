import { WebSocketServer } from "ws";

const PORT = 3000;

const getFish = (location) => {
  return {
    name: "Fish",
    habitat: location,
    money: 1,
    reputation: 1,
    rarity: "common",
    size: 1,
    color: "silver",
    description: "Roll a 2 and a 4",
  };
};

const broadcast = (message) => {
  wss.clients.forEach((client) => {
    if (client.readyState === WebSocket.OPEN) {
      client.send(JSON.stringify(message));
    }
  });
};

const sendError = (socket, error) => {
  console.error(error);
  socket.send(JSON.stringify({ type: "error", error }));
};

const wss = new WebSocketServer({ port: PORT });
let gameInProgress = false;
let gameState = {
  players: [],
  numDice: 1,
  diceRolls: [0],
  board: {},
};

wss.on("connection", (ws) => {
  console.info("Client connected");
  broadcast({ type: "gameInProgress", gameInProgress });
  broadcast({ type: "gameState", gameState });

  ws.on("message", (message) => {
    const data = JSON.parse(message.toString());
    console.debug(`message: ${JSON.stringify(data, null, 2)}`);

    switch (data.type) {
      case "joinGame":
        if (gameInProgress) {
          sendError(ws, "Game is already in progress");
          return;
        }

        ws.playerId = gameState.players.length;
        gameState.players.push({
          hand: [],
          reputation: 0,
          money: 0,
        });
        ws.send(JSON.stringify({ type: "playerId", playerId: ws.playerId }));
        break;
      case "startGame":
        if (gameInProgress) {
          sendError(ws, "Game is already in progress");
          return;
        }

        const numPlayers = gameState.players.length;
        if (numPlayers < 2 || numPlayers > 8) {
          sendError(ws, "Number of players must be between 2 and 8");
          return;
        }

        gameInProgress = true;
        gameState.board = {
          pier: Array(5)
            .fill()
            .map(() => getFish("pier")),
          lake: Array(5)
            .fill()
            .map(() => getFish("lake")),
          sea: Array(5)
            .fill()
            .map(() => getFish("sea")),
        };
        broadcast({ type: "gameInProgress", gameInProgress });
        break;
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
      case "addCard":
        if (!gameInProgress) {
          sendError(ws, "Game is not in progress");
          return;
        }

        if (!("playerId" in ws)) {
          sendError(ws, "Spectators can't add cards");
          return;
        }

        const newFish = getFish(data.location);
        gameState.board[data.location].push(newFish);
        break;
      case "drawCard":
        if (!gameInProgress) {
          sendError(ws, "Game is not in progress");
          return;
        }

        if (!("playerId" in ws)) {
          sendError(ws, "Spectators can't draw cards");
          return;
        }

        const [drawnFish] = gameState.board[data.location].splice(data.idx, 1);
        gameState.players[ws.playerId].hand.push(drawnFish);
        gameState.players[ws.playerId].reputation += drawnFish.reputation;
        break;
      case "discardCard":
        if (!gameInProgress) {
          sendError(ws, "Game is not in progress");
          return;
        }

        if (!("playerId" in ws)) {
          sendError(ws, "Spectators can't discard cards");
          return;
        }

        gameState.players[ws.playerId].hand.splice(data.idx, 1);
        break;
    }
    broadcast({ type: "gameState", gameState });
  });

  ws.on("close", () => {
    console.info("Client disconnected");

    if (!("playerId" in ws)) {
      return;
    }

    console.info("Game reset");
    gameInProgress = false;
    gameState.players = [];
    broadcast({ type: "gameInProgress", gameInProgress });
    broadcast({ type: "playerId", playerId: -1 });
  });
});

console.info(`The WebSocket server is running on port ${PORT}`);
