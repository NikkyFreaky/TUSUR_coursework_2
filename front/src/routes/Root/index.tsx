import React, { useState, KeyboardEvent } from 'react';
import './header.css';
import { Outlet, useNavigate } from 'react-router-dom';

import avatar from '../../assets/avatar.jpg';
import { ReactComponent as Logo } from '../../assets/search_icon.svg';
import { HeaderButton } from '../../components/UI/HeaderButton';
import { HeaderDropdown } from '../../components/UI/HeaderDropdown';
import {
  dropdownItemsCountry,
  dropdownItemsTime,
  dropdownItemsCategory,
} from './dropdownContent';

// импорты модалок
import Modal from '../../components/Modal';
import AuthModal from '../../components/AuthModal';
import RegisterModal from '../../components/RegisterModal';
import { UserCategories } from '../../components/UI/UserCategories';

export const Root = () => {
  const navigate = useNavigate();

  // функции работы с модалкой входа
  const [isLoginModalOpen, setLoginModalOpen] = useState(false);
  const openLoginModal = () => {
    setLoginModalOpen(true);
  };
  const closeLoginModal = () => {
    setLoginModalOpen(false);
  };

  // функции работы с модалкой реги
  const [isRegisterModalOpen, setRegisterModalOpen] = useState(false);
  const openRegisterModal = () => {
    setRegisterModalOpen(true);
  };
  const closeRegisterModal = () => {
    setRegisterModalOpen(false);
  };

  // для отправки инпута по энтеру
  const [searchValue, setSearchValue] = useState('');
  const handleKeyDown = (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      console.log('ROOT handleKeyDown Enter pressed');
      // Вызовите вашу функцию по нажатию Enter
      handleSearch();
    }
  };
  const handleSearch = () => {
    // Ваша функция по обработке поиска
    console.log('ROOT handleSearch searchValue: ', searchValue);
    navigate('/news/search/?q=' + searchValue);
    localStorage.setItem('keyword', searchValue);
    window.location.reload();
  };

  //стор
  const storedIsAuth = localStorage.getItem('isAuth');
  const initialIsAuth = storedIsAuth ? JSON.parse(storedIsAuth) : false;

  return (
    <div className="mainPage">
      <div className="navbar">
        <div className="navbar-content">
          <div className="contentTop">
            <a href="/news/" className="contentTop__title">
              NewsBazar
            </a>
            <div className="contentTop__search">
              <Logo />
              <input
                className="search__input"
                type="text"
                placeholder="Ключевые слова..."
                value={searchValue}
                onChange={(e) => setSearchValue(e.target.value)}
                onKeyDown={handleKeyDown}
              />
            </div>
            {initialIsAuth !== true ? (
              <button onClick={openLoginModal}>Вход</button>
            ) : (
              <img
                className="avatar__img"
                src={avatar}
                alt="avatar"
                onClick={(e) => navigate('/account/')}
              />
            )}
          </div>
          <div className="contentBottom">
            <HeaderButton value="Аккаунт" link="/account/" />
            {initialIsAuth === true ? <UserCategories /> : <div></div>}
            <HeaderDropdown value="По стране" items={dropdownItemsCountry} />
            <HeaderDropdown
              value="По категориям"
              items={dropdownItemsCategory}
            />
            <HeaderDropdown value="По дате" items={dropdownItemsTime} />
          </div>
        </div>
      </div>
      {/* модальное окно входа в аккаунт */}
      <Modal isOpen={isLoginModalOpen} onClose={closeLoginModal}>
        <AuthModal
          isOpen={isLoginModalOpen}
          onClose={closeLoginModal}
          switchToRegister={openRegisterModal}
        />
      </Modal>
      {/* модальное окно регистрации */}
      <Modal isOpen={isRegisterModalOpen} onClose={closeRegisterModal}>
        <RegisterModal
          isOpen={isRegisterModalOpen}
          onClose={closeRegisterModal}
          // loginEvent={loginEvent}
        />
      </Modal>

      <div id="detail">
        <Outlet />
      </div>
    </div>
  );
};
