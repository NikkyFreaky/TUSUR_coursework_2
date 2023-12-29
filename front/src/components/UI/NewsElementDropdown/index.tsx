import React, { useState, useEffect } from 'react';
import { IHeaderDropdownItem } from '../../../models';
import './headerDropdown.css';
import { addArticleToCategory, getUserCategories } from '../../../API';

export interface INewsElementDropdown {
  articleTitle: string;
}

export const NewsElementDropdown: React.FC<INewsElementDropdown> = ({
  articleTitle,
}) => {
  // Создаем состояние для отслеживания открытости/закрытости выпадающего списка
  const [isDropdownOpen, setDropdownOpen] = useState(false);
  const [items, setItems] = useState<string[]>([]);

  // Обработчик клика по кнопке
  const handleButtonClick = () => {
    // Закрываем все выпадающие списки перед открытием текущего
    // список пользовательских категорий

    getUserCategories().then((res) => {
      const categories = res.data.name;
      // const dropdownItems: string[] = categories.map((category: string) => ({
      //   text: category,
      // }));
      //setItems(dropdownItems);
      setItems(categories);
    });
    console.log(items);
    setDropdownOpen(true);
  };

  // Обработчик клика по элементу выпадающего списка
  const handleDropdownItemClick = (itemTitle: string) => {
    // ДОБАВЛЯЕМ НОВОСТЬ ПО ТАЙТЛУ В СПИСОК
    // Закрываем выпадающий список
    addArticleToCategory(itemTitle, articleTitle);
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
        +
      </button>

      {isDropdownOpen && (
        <div className="dropdownContent">
          <div className="dropdownItemsWrapper">
            {items.map((item, index) => (
              <a key={index} onClick={(e) => handleDropdownItemClick(item)}>
                {item}
              </a>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};
