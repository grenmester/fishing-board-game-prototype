import { FaCircleXmark, FaFish, FaMoneyBill, FaStar } from "react-icons/fa6";

const capitalize = (str) =>
  str
    .toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + str.slice(1))
    .join(" ");

const FishCard = ({ clickHandler, discardHandler, fish }) => (
  <div
    className="flex relative flex-col items-center p-4 w-36 h-52 text-sm text-center bg-gray-300 rounded-lg hover:bg-gray-400 group"
    onClick={clickHandler}
  >
    <button
      className="absolute -top-3 -right-3 invisible text-gray-300 bg-gray-900 rounded-full group-hover:visible hover:text-gray-400"
      onClick={(e) => {
        discardHandler();
        e.stopPropagation();
      }}
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
    <p className="h-10 font-bold text-md/5">{fish.name}</p>
    <FaFish className="my-2" size={40} />
    <p className="italic">{fish.description}</p>
  </div>
);

export default FishCard;
