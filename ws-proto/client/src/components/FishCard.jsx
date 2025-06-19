import { FaFish, FaMoneyBill, FaStar, FaCircleXmark } from "react-icons/fa6";

const capitalize = (str) =>
  str
    .toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + str.slice(1))
    .join(" ");

const FishCard = ({ clickHandler, discardHandler, fish }) => (
  <div
    className="group relative flex flex-col items-center p-4 w-36 h-52 text-sm text-center bg-gray-300 rounded-lg hover:bg-gray-400"
    onClick={clickHandler}
  >
    <button
      className="invisible group-hover:visible absolute -top-3 -right-3 text-gray-300 bg-gray-900 rounded-full hover:text-gray-400"
      onClick={e => { discardHandler(); e.stopPropagation() }}
    >
      <FaCircleXmark size={32} />
    </button>
    <div className="flex justify-between items-center w-28">
      <div className="flex gap-x-1 items-center">
        <FaStar />
        <span>{fish.reputation}</span>
      </div>
      <p className="text-xs font-bold">{capitalize(fish.habitat)}</p>
      <div className="flex gap-x-1 items-center">
        <FaMoneyBill />
        <span>{fish.money}</span>
      </div>
    </div>
    <p className="mb-1 text-xs text-gray-500">{fish.category}</p>
    <p className="h-10 font-bold text-lg/5">{fish.name}</p>
    <FaFish className="my-2" size={40} />
    <p>{fish.description}</p>
  </div>
);

export default FishCard;
