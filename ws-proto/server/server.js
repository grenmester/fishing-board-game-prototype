import fs from "fs/promises";
import { WebSocketServer } from "ws";
import YAML from "yaml";

const PORT = 3000;

const fileContents = await fs.readFile("./data.yaml", "utf8");
const gameData = YAML.parse(fileContents);

let fishDeck = {};
gameData.fish.forEach((fish) => {
  if (!(fish.habitat in fishDeck)) {
    fishDeck[fish.habitat] = [];
  }
  fishDeck[fish.habitat].push(fish);
});

const getFish = (location) => {
  if (fishDeck[location].length === 0) {
    console.log(`The ${location} deck is empty, refilling cards`);
    fishDeck[location] = gameData.fish.filter(
      (fish) => fish.habitat === location,
    );
  }
  const randomIdx = Math.floor(Math.random() * fishDeck[location].length);
  const [drawnFish] = fishDeck[location].splice(randomIdx, 1);
  return drawnFish;
};

let questDeck = structuredClone(gameData.quests);
let gearDeck = structuredClone(gameData.gear);

const getQuest = () => {
  if (questDeck.length === 0) {
    console.log("The quest deck is empty, refilling cards");
    questDeck = structuredClone(gameData.quests);
  }
  const randomIdx = Math.floor(Math.random() * questDeck.length);
  const [drawnQuest] = questDeck.splice(randomIdx, 1);
  return drawnQuest;
};

const getGear = () => {
  if (gearDeck.length === 0) {
    console.log("The gear deck is empty, refilling cards");
    gearDeck = structuredClone(gameData.gear);
  }
  const randomIdx = Math.floor(Math.random() * gearDeck.length);
  const [drawnGear] = gearDeck.splice(randomIdx, 1);
  return drawnGear;
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
  board: {
    fish: {},
    quests: [],
  },
};

wss.on("connection", (ws) => {
  console.info("Client connected");
  broadcast({ type: "gameInProgress", gameInProgress });
  broadcast({ type: "gameState", gameState });

  ws.on("message", (message) => {
    const data = JSON.parse(message.toString());
    console.debug(`message: ${JSON.stringify(data, null, 2)}`);

    const { type, ...payload } = data;

    if (
      ![
        "joinGame",
        "startGame",
        "addDie",
        "removeDie",
        "rollDice",
        "clearDice",
      ].includes(type)
    ) {
      if (!gameInProgress) {
        sendError(ws, "Game is not in progress");
        return;
      }

      if (!("playerId" in ws)) {
        sendError(ws, "Spectators can't perform this action");
        return;
      }
    }

    switch (type) {
      case "joinGame":
        if (gameInProgress) {
          sendError(ws, "Game is already in progress");
          return;
        }

        ws.playerId = gameState.players.length;
        gameState.players.push({
          hand: {
            fish: [],
            quests: [],
            gear: [],
          },
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

        console.info("Loaded decks:");
        Object.keys(fishDeck).forEach((location) => {
          console.info(location, ": ", fishDeck[location].length, "cards");
          gameState.board.fish[location] = Array(5)
            .fill()
            .map(() => getFish(location));
        });
        gameInProgress = true;
        gameState.board.quests = Array(5)
          .fill()
          .map(() => getQuest());
        gameState.board.gear = [];
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
      case "clearDice":
        gameState.diceRolls = Array(gameState.numDice).fill(0);
        break;
      case "addFish":
        const newFish = getFish(payload.location);
        gameState.board.fish[payload.location].push(newFish);
        break;
      case "drawFish":
        const [drawnFish] = gameState.board.fish[payload.location].splice(
          payload.idx,
          1,
        );
        gameState.players[ws.playerId].hand.fish.push(drawnFish);
        gameState.players[ws.playerId].reputation += drawnFish.reputation;
        break;
      case "removeFish":
        gameState.board.fish[payload.location].splice(payload.idx, 1);
        break;
      case "sellFish":
        const [soldFish] = gameState.players[ws.playerId].hand.fish.splice(
          payload.idx,
          1,
        );
        gameState.players[ws.playerId].money += soldFish.money;
        break;
      case "discardFish":
        gameState.players[ws.playerId].hand.fish.splice(payload.idx, 1);
        break;
      case "addQuest":
        const newQuest = getQuest();
        gameState.board.quests.push(newQuest);
        break;
      case "drawQuest":
        const [drawnQuest] = gameState.board.quests.splice(payload.idx, 1);
        gameState.players[ws.playerId].hand.quests.push(drawnQuest);
        break;
      case "removeQuest":
        gameState.board.quests.splice(payload.idx, 1);
        break;
      case "sellQuest":
        gameState.players[ws.playerId].hand.quests.splice(payload.idx, 1);
        break;
      case "discardQuest":
        gameState.players[ws.playerId].hand.quests.splice(payload.idx, 1);
        break;
      case "addGear":
        const newGear = getGear();
        gameState.board.gear.push(newGear);
        break;
      case "drawGear":
        const [drawnGear] = gameState.board.gear.splice(payload.idx, 1);
        gameState.players[ws.playerId].hand.gear.push(drawnGear);
        break;
      case "removeGear":
        gameState.board.gear.splice(payload.idx, 1);
        break;
      case "sellGear":
        gameState.players[ws.playerId].hand.gear.splice(payload.idx, 1);
        break;
      case "discardGear":
        gameState.players[ws.playerId].hand.gear.splice(payload.idx, 1);
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
