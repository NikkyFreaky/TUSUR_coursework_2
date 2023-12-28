import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import { logInAccount, getAccountData } from '../../API';
import Notification from '../Notification';
import './../Modal/modal.css';
import './authModal.css';

// импорты для стора
import {
  updateName,
  updateSurname,
  updateLogin,
  updateEmail,
  updateIsAuth,
} from './../../store/authStore';

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
    logInAccount(login, password)
      .then((responce) => {
        // успешный вход
        if (responce.data.status === 'success') {
          // вроде как при входе на сервер отправляется запрос на получение данных о юзере
          // закидываем эти данные в стор
          localStorage.setItem('isAuth', JSON.stringify(true));
          getAccountData()
            .then((res) => {
              localStorage.setItem('name', res.data.name);
              localStorage.setItem('surname', res.data.surname);
              localStorage.setItem('login', res.data.login);
              localStorage.setItem('email', res.data.email);
            })
            .catch((e) => console.log('AuthModal getAccountData error: ', e));

          setShowNotification(true);
          setNotificationText('Успешный вход');
          setTimeout(() => {
            setShowNotification(false);
            onClose(); // Закрытие модального окна после уведомления
          }, 3000);
        }
        // Пустое поле/поля
        else if (responce.data.message === 'This field is required.') {
          setShowNotification(true);
          setNotificationText('Все поля обязательны к заполнению');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // Юзер в бане
        else if (responce.data.message === 'User is banned') {
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
          setShowNotification(true);
          setNotificationText('Введен неверный логин или пароль');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // обработка на всякий случай. Не знаю, как на неё выйти
        else {
          setShowNotification(true);
          setNotificationText('Некорректные данные регистрации');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
      })
      .catch((error) => {
        console.log('AUTH MODAL CAUGHT ERROR', error);
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
