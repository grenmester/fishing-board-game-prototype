import { useEffect, useRef, useState } from "react";
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
  const [gameState, setGameState] = useState({
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
        case "update":
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
      <h1 className="flex justify-center m-10 text-4xl font-bold text-center">
        Fishing Board Game Prototype
      </h1>
      <div className="p-4 w-full max-w-md bg-gray-100 rounded-xl">
        <h2 className="mb-4 font-bold text-center">Dice</h2>
        <div className="flex flex-col gap-y-2 items-center">
          <div className="flex gap-x-2">
            {gameState.diceRolls.map((roll, idx) => {
              const Icon = diceIcons[roll] || GiSquare;
              return <Icon key={idx} size={32} />;
            })}
          </div>
          <div className="flex gap-x-2">
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "addDie" })}
            >
              <IoMdAdd className="text-white" />
            </button>
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "removeDie" })}
            >
              <IoMdRemove className="text-white" />
            </button>
            <button
              className="p-2 bg-gray-500 rounded-full"
              onClick={() => sendMessage({ type: "rollDice" })}
            >
              <IoMdSync className="text-white" />
            </button>
          </div>
        </div>
      </div>
      <div className="p-4 w-full max-w-4xl bg-yellow-100 rounded-xl">
        <h2 className="mb-4 font-bold text-center">Game State</h2>
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
