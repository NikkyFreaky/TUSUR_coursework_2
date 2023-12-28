import './account.css';
import avatar from './../../assets/avatar.jpg';
import CustomTextInput from '../../components/UI/Input';
import { HeaderButton } from '../../components/UI/HeaderButton';

export const Account = () => {
  return (
    <div className="account">
      <div className="container">
        <div className="avatarInfo">
          <img className="avatarInfo__avatar" src={avatar} alt="avatar" />
          <div className="avatarInfo__username">Имя Фамилия</div>
        </div>
        <div className="accountInfo">
          <div className="accountInfo__container">
            <div className="accountInfo__labelInputPair">
              <label>E-mail</label>
            </div>
            <div className="accountInfo__labelInputPair">
              <label>Логин</label>
            </div>
            <HeaderButton value="Выйти" link="" />
          </div>
        </div>
      </div>
    </div>
  );
};
