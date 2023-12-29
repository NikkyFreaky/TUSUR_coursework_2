import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import { registerInAccount, getAccountData } from '../../API';
import Notification from '../Notification';
import './../Modal/modal.css';
import './registerModal.css';

// импорты для стора
import {
  updateName,
  updateSurname,
  updateLogin,
  updateEmail,
} from './../../store/authStore';

interface IRegisterModalProps {
  isOpen: boolean;
  onClose: () => void;
}

const RegisterModal: FC<IRegisterModalProps> = ({ isOpen, onClose }) => {
  const [login, setLogin] = useState('');
  const [email, setEmail] = useState('');
  const [first_name, setName] = useState('');
  const [last_name, setSurname] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');

  const handleLogin = () => {
    registerInAccount(login, email, first_name, last_name, password1, password2)
      .then((responce) => {
        // успешная регистрация
        if (responce.data.status === 'success') {
          getAccountData()
            .then((res) => {
              localStorage.setItem('name', res.data.name);
              localStorage.setItem('surname', res.data.surname);
              localStorage.setItem('login', res.data.login);
              localStorage.setItem('email', res.data.email);
            })
            .catch((e) => console.log('AuthModal getAccountData error: ', e));
          localStorage.setItem('isAuth', JSON.stringify(true));

          setShowNotification(true);
          setNotificationText('Успешная регистрация');
          setTimeout(() => {
            setShowNotification(false);
            onClose(); // Закрытие модального окна после уведомления
          }, 3000);
        }
        // хоть одно из полей пустое
        else if (responce.data.message === 'This field is required.') {
          setShowNotification(true);
          setNotificationText('Все поля обязательны к заполнению');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // регистрация с распространенным паролем
        else if (responce.data.message === 'This password is too common.') {
          setShowNotification(true);
          setNotificationText(
            'Данный пароль является слишком распространенным',
          );
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // повторяющийся логин
        else if (
          responce.data.message === 'A user with that username already exists.'
        ) {
          setShowNotification(true);
          setNotificationText('Данный логин уже используется');
          setTimeout(() => {
            setShowNotification(false);
          }, 3000);
        }
        // Несовпадение пароля и проверки пароля
        else if (
          responce.data.message === 'The two password fields didn’t match.'
        ) {
          setShowNotification(true);
          setNotificationText('Пароль и проверка пароля не совпадают');
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
        setShowNotification(true);
        setNotificationText('Неверные данные регистрации');
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
          <label htmlFor="email">E-mail:</label>
          <input
            type="text"
            id="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>
        <div className="labelInputPair">
          <label htmlFor="name">Имя:</label>
          <input
            type="text"
            id="name"
            value={first_name}
            onChange={(e) => setName(e.target.value)}
          />
        </div>
        <div className="labelInputPair">
          <label htmlFor="surname">Фамилия:</label>
          <input
            type="text"
            id="surname"
            value={last_name}
            onChange={(e) => setSurname(e.target.value)}
          />
        </div>
        <div className="labelInputPair">
          <label htmlFor="password">Пароль:</label>
          <input
            type="password"
            id="password"
            value={password1}
            onChange={(e) => setPassword1(e.target.value)}
          />
        </div>
        <div className="labelInputPair">
          <label htmlFor="password2">Подтвердите пароль:</label>
          <input
            type="password"
            id="password2"
            value={password2}
            onChange={(e) => setPassword2(e.target.value)}
          />
        </div>
        <div className="registerButton">
          <button onClick={handleLogin}>Регистрация</button>
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

export default RegisterModal;
