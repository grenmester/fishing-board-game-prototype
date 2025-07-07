import { FaQuestion, FaCircleXmark } from "react-icons/fa6";

const QuestCard = ({ clickHandler, discardHandler, quest }) => (
  <div
    className="flex relative flex-col items-center p-4 w-36 h-52 text-sm text-center rounded-lg bg-neutral-300 group hover:bg-neutral-400"
    onClick={clickHandler}
  >
    <button
      className="absolute -top-3 -right-3 invisible rounded-full group-hover:visible text-neutral-300 bg-neutral-900 hover:text-neutral-400"
      onClick={(e) => {
        discardHandler();
        e.stopPropagation();
      }}
    >
      <FaCircleXmark size={32} />
    </button>
    <p className="h-10 font-bold text-md/5">{quest.name}</p>
    <FaQuestion className="my-2" size={40} />
    <p className="italic">{quest.description}</p>
  </div>
);

export default QuestCard;
