import React, { useState } from 'react';
import './header.css';
import { Link, Outlet } from 'react-router-dom';

import avatar from '../../assets/avatar.jpg';
import { ReactComponent as Logo } from '../../assets/search_icon.svg';
import { HeaderButton } from '../../components/UI/HeaderButton';
import { HeaderDropdown } from '../../components/UI/HeaderDropdown';
import {
  dropdownItemsCountry,
  dropdownItemsTime,
  dropdownItemsCategory,
} from './dropdownContent';

export const Root = () => {
  const [newsParameter, setNewsParameter] = useState<string>('us');
  return (
    <div className="mainPage">
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
              <HeaderDropdown
                value="По стране"
                items={dropdownItemsCountry}
                setNewsParameter={setNewsParameter}
              />
              <HeaderDropdown
                value="По категориям"
                items={dropdownItemsCategory}
                setNewsParameter={setNewsParameter}
              />
              <HeaderDropdown
                value="По дате"
                items={dropdownItemsTime}
                setNewsParameter={setNewsParameter}
              />
              <HeaderButton value="Текст" />
            </div>
          </div>
        </div>
      </div>
      <div id="detail">
        <Outlet />
      </div>
    </div>
  );
};
