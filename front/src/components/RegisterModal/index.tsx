import React, { FC, useState } from 'react';
import Modal from './../Modal'; // Подключите ваш компонент Modal
import { registerInAccount } from '../../API';
import Notification from '../Notification';
import './../Modal/modal.css';
import './registerModal.css';

// импорты для стора
import {
  updateName,
  updateSurname,
  updateLogin,
  updateEmail,
  loginEvent,
} from './../../store/authStore';

interface IRegisterModalProps {
  isOpen: boolean;
  onClose: () => void;
  // loginEvent: EventCallable<void>;
}

const RegisterModal: FC<IRegisterModalProps> = ({ isOpen, onClose }) => {
  const [login, setLogin] = useState('');
  const [email, setEmail] = useState('');
  const [first_name, setName] = useState('');
  const [last_name, setSurname] = useState('');
  const [password1, setPassword1] = useState('');
  const [password2, setPassword2] = useState('');

  const [auth, setAuth] = useState<boolean>(false);

  const handleLogin = () => {
    registerInAccount(
      login,
      email,
      first_name,
      last_name,
      password1,
      password2,
    ).then((responce) => console.log(responce.data));
  };

  // updateName(first_name);
  // updateSurname(last_name);
  // updateLogin(login);
  // updateEmail(email);
  // loginEvent();

  // const handleLogin = () => {

  //   registerInAccount(login, email, first_name, last_name, password1, password2)
  //     .then((responce) => {
  //       if (responce.status === 200) {
  //         setAuth(true);
  //         console.log('Auth successfull with status', responce.status);
  //         setShowNotification(true);
  //         setNotificationText('Успешная регистрация');
  //         setTimeout(() => {
  //           setShowNotification(false);
  //           onClose(); // Закрытие модального окна после уведомления
  //         }, 3000);
  //       }
  //     })
  //     .catch((error) => {
  //       console.log('Auth failed with error: ', error);
  //       setShowNotification(true);
  //       setNotificationText('Неверные данные регистрации');
  //       setTimeout(() => {
  //         setShowNotification(false);
  //       }, 3000);
  //     });
  // };

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
