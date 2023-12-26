import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import { registerInAccount } from '../../API';
import './../Modal/modal.css';
import './registerModal.css';

interface IRegisterModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const RegisterModal: FC<IRegisterModalProps> = ({ isOpen, onClose }) => {
  const [login, setLogin] = useState('');
  const [password, setPassword] = useState('');
  const [passwordVerify, setPasswordVerify] = useState('');

  const handleLogin = () => {
    // Реализуйте вашу логику регистрации с использованием login и password
    console.log('Попытка регистрации:', login, password, passwordVerify);
  };

  return (
    <Modal isOpen={isOpen} onClose={onClose}>
      <div className="register-modal">
        <div className="newsBazar">NewsBazar</div>
        <div className="modalTitle">Регистрация</div>
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
        <div className="labelInputPair">
          <label htmlFor="passwordVerify">Подтвердите пароль:</label>
          <input
            type="password"
            id="passwordVerify"
            value={passwordVerify}
            onChange={(e) => setPasswordVerify(e.target.value)}
          />
        </div>
        <div className="registerButton">
          <button onClick={handleLogin}>Регистрация</button>
        </div>
      </div>
    </Modal>
  );
};

export default RegisterModal;
