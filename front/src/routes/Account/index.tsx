import './account.css';
import avatar from './../../assets/avatar.jpg';
import { HeaderButton } from '../../components/UI/HeaderButton';

import { useNavigate } from 'react-router-dom';
import { logOutAccount } from '../../API';

// импорты для стора
import { useStoreMap } from 'effector-react';
import { userStore, logoutEvent } from './../../store/authStore';

export const Account = () => {
  const navigate = useNavigate();

  const name = useStoreMap({
    store: userStore,
    keys: ['name'],
    fn: (state) => state.name,
  });

  const surname = useStoreMap({
    store: userStore,
    keys: ['surname'],
    fn: (state) => state.surname,
  });

  const email = useStoreMap({
    store: userStore,
    keys: ['email'],
    fn: (state) => state.email,
  });

  const login = useStoreMap({
    store: userStore,
    keys: ['login'],
    fn: (state) => state.login,
  });

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
                logoutEvent();
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
