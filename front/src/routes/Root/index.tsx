import React, { useState } from 'react';
import './header.css';
import { Outlet } from 'react-router-dom';

import avatar from '../../assets/avatar.jpg';
import { ReactComponent as Logo } from '../../assets/search_icon.svg';
import { HeaderButton } from '../../components/UI/HeaderButton';
import { HeaderDropdown } from '../../components/UI/HeaderDropdown';
import {
  dropdownItemsCountry,
  dropdownItemsTime,
  dropdownItemsCategory,
} from './dropdownContent';
import Modal from '../../components/Modal';

export const Root = () => {
  // функции работы с модальным окном
  const [isModalOpen, setModalOpen] = useState(false);
  const openModal = () => {
    setModalOpen(true);
  };
  const closeModal = () => {
    setModalOpen(false);
  };

  return (
    <div className="mainPage">
      <div className="navbar">
        <div className="navbar-content">
          <div className="contentTop">
            <div className="contentTop__title">NewsBazar</div>
            <div className="contentTop__search">
              <Logo />
              <input
                className="search__input"
                type="text"
                placeholder="Ключевые слова..."
              />
            </div>
            <button onClick={openModal}>Вход</button>
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
      <div id="detail">
        <Outlet />
      </div>
      <Modal isOpen={isModalOpen} onClose={closeModal}>
        {/* ... Ваш контент модального окна ... */}
      </Modal>
    </div>
  );
};
