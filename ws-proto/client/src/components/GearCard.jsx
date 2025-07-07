import { FaCircleXmark, FaGear, FaMoneyBill } from "react-icons/fa6";

const capitalize = (str) =>
  str
    .toLowerCase()
    .split(" ")
    .map((word) => word.charAt(0).toUpperCase() + str.slice(1))
    .join(" ");

const GearCard = ({ clickHandler, discardHandler, gear }) => (
  <div
    className="flex relative flex-col items-center p-4 w-36 h-52 text-sm text-center rounded-lg bg-slate-300 group hover:bg-slate-400"
    onClick={clickHandler}
  >
    <button
      className="absolute -top-3 -right-3 invisible rounded-full group-hover:visible text-slate-300 bg-slate-900 hover:text-slate-400"
      onClick={(e) => {
        discardHandler();
        e.stopPropagation();
      }}
    >
      <FaCircleXmark size={32} />
    </button>
    <div className="flex justify-between items-center w-28">
      <p className="text-xs font-bold">{capitalize(gear.type)}</p>
      <div className="flex gap-x-1 items-center">
        <FaMoneyBill />
        <span>{gear.cost}</span>
      </div>
    </div>
    <p className="h-10 font-bold text-md/5">{gear.name}</p>
    <FaGear className="my-2" size={40} />
    <p className="italic">{gear.description}</p>
  </div>
);

export default GearCard;
