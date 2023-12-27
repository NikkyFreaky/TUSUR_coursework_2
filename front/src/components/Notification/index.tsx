import React, { FC, useEffect } from 'react';
import './notification.css';

interface NotificationProps {
  text: string;
  onClose: () => void;
}

const Notification: FC<NotificationProps> = ({ text, onClose }) => {
  useEffect(() => {
    const timeoutId = setTimeout(() => {
      onClose();
    }, 5000);

    return () => {
      clearTimeout(timeoutId);
    };
  }, [onClose]);

  return (
    <div className="notification">
      <p>{text}</p>
    </div>
  );
};

export default Notification;
