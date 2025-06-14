import { useEffect, useRef, useState } from "react";
import { FaCircleUser, FaFish, FaMoneyBill, FaStar } from "react-icons/fa6";
import {
  GiInvertedDice1,
  GiInvertedDice2,
  GiInvertedDice3,
  GiInvertedDice4,
  GiInvertedDice5,
  GiInvertedDice6,
  GiSquare,
} from "react-icons/gi";
import { IoMdAdd, IoMdClose, IoMdRemove, IoMdSync } from "react-icons/io";

import DebugConsole from "./components/DebugConsole";

const diceIcons = [
  GiSquare,
  GiInvertedDice1,
  GiInvertedDice2,
  GiInvertedDice3,
  GiInvertedDice4,
  GiInvertedDice5,
  GiInvertedDice6,
];

const App = () => {
  const [gameInProgress, setGameInProgress] = useState(false);
  const [playerId, setPlayerId] = useState(-1);
  const [gameState, setGameState] = useState({
    players: [],
    numDice: 1,
    diceRolls: [0],
  });
  const [error, setError] = useState("");

  const wsRef = useRef();

  useEffect(() => {
    const ws = new WebSocket("ws://localhost:3000");
    wsRef.current = ws;

    ws.onmessage = (e) => {
      const data = JSON.parse(e.data);

      switch (data.type) {
        case "gameInProgress":
          setGameInProgress(data.gameInProgress);
          break;
        case "playerId":
          setPlayerId(data.playerId);
          break;
        case "gameState":
          setGameState(data.gameState);
          break;
        case "error":
          setError(data.error);
          break;
      }
    };

    return () => {
      ws.close();
    };
  }, []);

  const sendMessage = (message) => {
    wsRef.current?.send(JSON.stringify(message));
  };

  return (
    <div className="flex flex-col gap-y-4 items-center p-4 sm:p-10">
      <h1 className="flex justify-center m-10 text-6xl font-bold text-center">
        Fishing Board Game Prototype
      </h1>
      <p>{gameInProgress ? "Game in Progress" : "Waiting for Game to Start"}</p>
      {!gameInProgress && (
        <div className="flex gap-x-4">
          {playerId == -1 && (
            <button
              className="py-2 px-4 bg-purple-300 rounded-full"
              onClick={() => sendMessage({ type: "joinGame" })}
            >
              Join Game
            </button>
          )}
          <button
            className="py-2 px-4 bg-purple-300 rounded-full"
            onClick={() => sendMessage({ type: "startGame" })}
          >
            Start Game
          </button>
        </div>
      )}
      <div className="p-4 w-full max-w-4xl bg-purple-100 rounded-xl">
        <h2 className="mb-4 text-4xl font-bold text-center">Players</h2>
        <div className="flex flex-wrap gap-4 justify-center">
          {gameState.players.map((player, idx) => (
            <div
              className={`flex flex-col gap-y-2 items-center p-4 bg-purple-300 rounded-lg ${playerId == idx && "border-2 border-purple-700"}`}
              key={idx}
            >
              <div className="flex gap-4">
                <div className="flex gap-1 items-center">
                  <FaStar className="text-yellow-500" />
                  <span>{player.reputation}</span>
                </div>
                <div className="flex gap-1 items-center">
                  <FaMoneyBill className="text-green-500" />
                  <span>{player.money}</span>
                </div>
                <div className="flex gap-1 items-center">
                  <FaFish className="text-blue-500" />
                  <span>{player.hand.length}</span>
                </div>
              </div>
              <FaCircleUser size={48} />
              <p className="font-bold">Player {idx}</p>
            </div>
          ))}
        </div>
      </div>
      <div className="p-4 w-full max-w-2xl bg-gray-100 rounded-xl">
        <h2 className="mb-4 text-4xl font-bold text-center">Dice</h2>
        <div className="flex flex-col gap-y-2 items-center">
          <div className="flex gap-x-2">
            {gameState.diceRolls.map((roll, idx) => {
              const Icon = diceIcons[roll] || GiSquare;
              return <Icon key={idx} size={48} />;
            })}
          </div>
          <div className="flex gap-x-2 text-white">
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "addDie" })}
            >
              <IoMdAdd size={24} />
            </button>
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "removeDie" })}
            >
              <IoMdRemove size={24} />
            </button>
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "rollDice" })}
            >
              <IoMdSync size={24} />
            </button>
          </div>
        </div>
      </div>
      <div className="p-4 w-full max-w-4xl bg-yellow-100 rounded-xl">
        <h2 className="mb-4 text-4xl font-bold text-center">Game State</h2>
        <pre>{JSON.stringify(gameState, null, 2)}</pre>
      </div>
      {error && (
        <div className="fixed top-4 right-4">
          <div className="flex gap-4 justify-between items-center py-2 px-4 text-red-500 bg-red-100 rounded-xl border-2 border-red-500">
            <p className="max-w-md">Error: {error}</p>
            <IoMdClose onClick={() => setError("")} />
          </div>
        </div>
      )}
      <DebugConsole sendMessage={sendMessage} />
    </div>
  );
};

export default App;
