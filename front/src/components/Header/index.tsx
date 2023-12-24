import React from 'react';
import './header.css';
import { Link } from 'react-router-dom';

import { IHeader } from '../../models';
import avatar from '../../assets/avatar.jpg';
import { ReactComponent as Logo } from '../../assets/search_icon.svg';
import { HeaderButton } from '../UI/HeaderButton';
import { HeaderDropdown } from '../UI/HeaderDropdown';
import {
  dropdownItemsCountry,
  dropdownItemsTime,
  dropdownItemsCategory,
} from './dropdownContent';

export const Header: React.FC<IHeader> = ({}) => {
  function refreshPage() {
    window.location.reload();
  }

  return (
    <div className="navbar">
      <div className="navbar-content">
        <div className="contentTop">
          <Link to="/news/us" className="contentTop__title">
            NewsBazar
          </Link>
          <div className="contentTop__search">
            <Logo />
            <input
              className="search__input"
              type="text"
              placeholder="Ключевые слова..."
            />
          </div>
          <img className="avatar__img" src={avatar} alt="avatar" />
        </div>
        <div className="contentBottom">
          <div className="contentBottom__left">
            <HeaderButton value="Главная" />
            <HeaderButton value="Аккаунт" />
            <HeaderButton value="Текст" />
          </div>
          <div className="contentBottom__right">
            <HeaderDropdown value="По стране" items={dropdownItemsCountry} />
            <HeaderDropdown
              value="По категориям"
              items={dropdownItemsCategory}
            />
            <HeaderDropdown value="По дате" items={dropdownItemsTime} />
            <HeaderButton value="Текст" />
          </div>
        </div>
      </div>
    </div>
  );
};

{
  /* <div className="v31_7" onClick={refreshPage}>
  <div className="v30_17"></div>
  <span className="v30_19">Главная</span>
</div>; */
}
