import React, { useState } from 'react';
import { IHeaderDropdown } from '../../../models';
import './headerDropdown.css';

export const HeaderDropdown: React.FC<IHeaderDropdown> = ({ value, items, setNewsParameter }) => {
  // Создаем состояние для отслеживания открытости/закрытости выпадающего списка
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  // Обработчик клика по кнопке
  const handleButtonClick = () => {
    setDropdownOpen(!isDropdownOpen);
  };

  // Обработчик клика по элементу выпадающего списка
  const handleDropdownItemClick = (itemHref: string) => {
    // Закрываем выпадающий список
    setNewsParameter(itemHref);
    setDropdownOpen(false);
  };

  return (
    <div className={`headerButtonContainer ${isDropdownOpen ? 'open' : ''}`}>
      <button className="headerButton" onClick={handleButtonClick}>
        {value}
      </button>

      {isDropdownOpen && (
        <div className="dropdownContent">
          {/* Добавляем стили для прокрутки и отображения только 8 элементов */}
          <div className="dropdownItemsWrapper">
            {items.map((item, index) => (
              <a key={index} href={item.href} onClick={(e) => handleDropdownItemClick(item.href)}>
                {item.text}
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
