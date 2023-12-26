import React, { useState, useEffect } from 'react';
import { IHeaderDropdown } from '../../../models';
import './headerDropdown.css';

export const HeaderDropdown: React.FC<IHeaderDropdown> = ({ value, items }) => {
  // Создаем состояние для отслеживания открытости/закрытости выпадающего списка
  const [isDropdownOpen, setDropdownOpen] = useState(false);

  // Обработчик клика по кнопке
  const handleButtonClick = () => {
    // Закрываем все выпадающие списки перед открытием текущего
    setDropdownOpen(true);
  };

  // Обработчик клика по элементу выпадающего списка
  const handleDropdownItemClick = (itemHref: string) => {
    // Закрываем выпадающий список
    setDropdownOpen(false);
  };

  const handleDocumentClick = (event: MouseEvent) => {
    const dropdownContainers = document.querySelectorAll(
      '.headerButtonContainer',
    );
    let isInsideAnyDropdown = false;

    dropdownContainers.forEach((dropdownContainer) => {
      if (dropdownContainer.contains(event.target as Node)) {
        isInsideAnyDropdown = true;
      }
    });

    // Закрываем все выпадающие списки, если клик был вне любого из них
    if (!isInsideAnyDropdown) {
      setDropdownOpen(false);
    }
  };

  useEffect(() => {
    document.addEventListener('click', handleDocumentClick);

    // Отписываемся от обработчика при размонтировании компонента
    return () => {
      document.removeEventListener('click', handleDocumentClick);
    };
  }, []);

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
              <a
                key={index}
                href={item.href}
                onClick={(e) => handleDropdownItemClick}
              >
                {item.text}
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
