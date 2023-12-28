import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import { logInAccount } from '../../API';
import Notification from '../Notification';
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

  const [auth, setAuth] = useState<boolean>(false);

  const handleLogin = () => {
    logInAccount(login, password)
      .then((responce) => {
        console.log(responce.data);
        // успешный вход
        if (responce.data.status === 'success') {
          setAuth(true);
          console.log(
            'Login successfull with message: ',
            responce.data.message,
          );
          setShowNotification(true);
          setNotificationText('Успешный вход');
          setTimeout(() => {
            setShowNotification(false);
            onClose(); // Закрытие модального окна после уведомления
          }, 3000);
        }
        // Пустое поле/поля
        else if (responce.data.message === 'This field is required.') {
          console.log('Login failed with message: ', responce.data.message);
          setShowNotification(true);
          setNotificationText('Все поля обязательны к заполнению');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // Юзер в бане
        else if (responce.data.message === 'User is banned') {
          console.log('Login failed with message: ', responce.data.message);
          setShowNotification(true);
          setNotificationText('Пользователь в черном списке');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // Неверный логин/пароль
        else if (
          responce.data.message ===
          'Please enter a correct username and password'
        ) {
          console.log('Login failed with message: ', responce.data.message);
          setShowNotification(true);
          setNotificationText('Введен неверный логин или пароль');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // обработка на всякий случай. Не знаю, как на неё выйти
        else {
          console.log('Login failed, i dont know what happened');
          setShowNotification(true);
          setNotificationText('Некорректные данные регистрации');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
      })
      .catch((error) => {
        console.log('Login failed with error: ', error);
        setShowNotification(true);
        setNotificationText('Неверные данные входа');
        setTimeout(() => {
          setShowNotification(false);
        }, 3000);
      });
  };

  // всплывающее уведомление
  const [showNotification, setShowNotification] = useState(false);
  const [notificationText, setNotificationText] = useState('');

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
      {showNotification && (
        <Notification
          text={notificationText}
          onClose={() => setShowNotification(false)}
        />
      )}
    </Modal>
  );
};

export default AuthModal;
