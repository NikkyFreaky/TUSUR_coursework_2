import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import './../Modal/modal.css';
import './authModal.css';

interface IAuthModalProps {
  isOpen: boolean;
  onClose: () => void;
  switchToRegister: () => void;
}

const AuthModal: FC<IAuthModalProps> = ({
  isOpen,
  onClose,
  switchToRegister,
}) => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    // Реализуйте вашу логику входа с использованием login и password
    console.log('Попытка входа:', login, password);
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div className="auth-modal">
        <div className="newsBazar">NewsBazar</div>
        <div className="modalTitle">Вход</div>
        <div className="labelInputPair">
          <label htmlFor="login">Логин:</label>
          <input
            type="text"
            id="login"
            value={login}
            onChange={(e) => setLogin(e.target.value)}
          />
        </div>
        <div className="labelInputPair">
          <label htmlFor="password">Пароль:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <div className="loginAndRegister">
          <button onClick={handleLogin}>Войти</button>
          <span
            className="registerAsking"
            onClick={() => {
              onClose();
              switchToRegister();
            }}
          >
            Регистрация
          </span>
        </div>
      </div>
    </Modal>
  );
};

export default AuthModal;
