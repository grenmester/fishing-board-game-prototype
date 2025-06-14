import { useEffect, useRef, useState } from "react";
import { VscDebug } from "react-icons/vsc";

const DebugConsole = ({ sendMessage }) => {
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [debugString, setDebugString] = useState("");

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

  const debugStringHandler = (e) => {
    setDebugString(e.target.value);
  };

  const sendMessageHandler = () => {
    sendMessage(debugString);
  };

  return (
    <div>
      <button
        className="fixed right-4 bottom-4 p-2 text-white bg-red-500 rounded-full shadow hover:bg-red-600"
        onClick={openModal}
      >
        <VscDebug />
      </button>
      {isModalOpen && (
        <div
          className="fixed right-4 bottom-4 z-10 py-4 px-6 w-96 bg-red-100 rounded-lg border-2 border-red-500"
          ref={modalRef}
        >
          <h2 className="mb-2 font-bold">WebSocket Debug Console</h2>
          <textarea
            className="py-1 px-2 w-full h-24 bg-white rounded border-2 border-red-500"
            onChange={debugStringHandler}
            placeholder="WebSocket message"
          />
          <div className="flex justify-end">
            <button
              className="py-2 px-4 text-sm text-white bg-red-500 rounded-full hover:bg-red-600"
              onClick={sendMessageHandler}
            >
              Send Message
            </button>
          </div>
        </div>
      )}
    </div>
  );
};

export default DebugConsole;
