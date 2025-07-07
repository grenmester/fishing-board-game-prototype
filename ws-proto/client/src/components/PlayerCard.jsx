import { useEffect, useRef, useState } from "react";
import { FaCircleUser, FaFish, FaMoneyBill, FaStar } from "react-icons/fa6";

import FishCard from "./FishCard";

const PlayerCard = ({ idx, player, playerId }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);

  const modalRef = useRef(null);

  useEffect(() => {
    const handleOutsideClick = (e) => {
      if (!modalRef.current?.contains(e.target)) {
        closeModal();
      }
    };

    if (isModalOpen) {
      document.addEventListener("mousedown", handleOutsideClick);
    }

    return () => {
      document.removeEventListener("mousedown", handleOutsideClick);
    };
  }, [isModalOpen]);

  const closeModal = () => {
    setIsModalOpen(false);
  };

  const openModal = () => {
    setIsModalOpen(true);
  };

  return (
    <div className="relative">
      <div
        className={`flex flex-col gap-y-2 items-center p-4 w-48 bg-purple-300 rounded-lg hover:bg-purple-400 ${playerId == idx && "ring-2 ring-purple-700"}`}
        onClick={openModal}
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
            <span>{player.hand.fish.length}</span>
          </div>
        </div>
        <FaCircleUser size={48} />
        <p className="font-bold">Player {idx}</p>
      </div>
      {isModalOpen && (
        <div className="absolute top-40 left-1/2 z-10 p-4 bg-blue-100 rounded-lg ring-2 ring-blue-700 -translate-x-1/2 w-3xl">
          <h2 className="mb-4 text-xl font-bold text-center">Hand</h2>
          <div className="grid grid-cols-4 gap-4 justify-center mx-auto w-fit">
            {player.hand.fish.map((fish, idx) => (
              <FishCard fish={fish} key={`${fish.name}${idx}`} />
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default PlayerCard;
