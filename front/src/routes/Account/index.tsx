import './account.css';
import avatar from './../../assets/avatar.jpg';
import { HeaderButton } from '../../components/UI/HeaderButton';

import { useNavigate } from 'react-router-dom';
import { logOutAccount } from '../../API';

// импорты для стора
import { useStoreMap } from 'effector-react';
import { userStore } from './../../store/authStore';

export const Account = () => {
  const navigate = useNavigate();


const name = localStorage.getItem('name');
const surname = localStorage.getItem('surname');
const login = localStorage.getItem('login');
const email = localStorage.getItem('email');

  return (
    <div className="account">
      <div className="container">
        <div className="avatarInfo">
          <img className="avatarInfo__avatar" src={avatar} alt="avatar" />
          <div className="avatarInfo__username">
            {name} {surname}
          </div>
        </div>
        <div className="accountInfo">
          <div className="accountInfo__container">
            <div className="accountInfo__labelInputPair">
              <label>{email}</label>
            </div>
            <div className="accountInfo__labelInputPair">
              <label>{login}</label>
            </div>
            <button
              onClick={() => {
                localStorage.setItem('isAuth', JSON.stringify(false));
                logOutAccount();
                navigate('/news/');
              }}
            >
              Выйти
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};
