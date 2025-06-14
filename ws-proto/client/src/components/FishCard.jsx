import { FaFish, FaMoneyBill, FaStar } from "react-icons/fa6";

const capitalize = (str) =>
  str
    .toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + str.slice(1))
    .join(" ");

const FishCard = ({ clickHandler, fish }) => (
  <div
    className="flex flex-col items-center p-4 w-40 h-56 bg-cyan-300 rounded-lg hover:bg-cyan-400"
    onClick={clickHandler}
  >
    <div className="flex gap-x-4 items-center">
      <div className="flex gap-x-1 items-center">
        <FaStar />
        <span>{fish.reputation}</span>
      </div>
      <p className="text-sm font-italic">{capitalize(fish.habitat)}</p>
      <div className="flex gap-x-1 items-center">
        <FaMoneyBill />
        <span>{fish.money}</span>
      </div>
    </div>
    <p className="text-xl font-bold">{fish.name}</p>
    <p className="text-sm">
      {fish.rarity}, {fish.size} cm
    </p>
    <FaFish className="my-4" size={40} />
    <p>{fish.description}</p>
  </div>
);

export default FishCard;
