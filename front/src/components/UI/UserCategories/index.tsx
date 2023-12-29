import React, { useState, useEffect } from 'react';
import { IHeaderDropdownItem } from '../../../models';
import './userCategories.css';
import {
  createUserCategory,
  deleteUserCategory,
  getUserCategories,
} from '../../../API';
import CategoryModal from '../../CategoryModal';

export interface IUserCategories {}

export const UserCategories: React.FC<IUserCategories> = ({}) => {
  // Создаем состояние для отслеживания открытости/закрытости выпадающего списка
  const [isDropdownOpen, setDropdownOpen] = useState(false);
  const [items, setItems] = useState<IHeaderDropdownItem[]>([]);

  // Обработчик клика по кнопке
  const handleButtonClick = () => {
    getUserCategories()
      .then((res) => {
        console.log('USERCATEGORIES getUserCategories res.data: ', res.data);
        const categories = res.data.name;
        const dropdownItems: IHeaderDropdownItem[] = categories.map(
          (category: string) => ({
            href: `/news_user_category/${category}`, // замените на реальный путь
            text: category,
          }),
        );
        setItems(dropdownItems);
        console.log(items);
      })
      .catch((e) => console.log('USERCATEGORIES getUserCategories error: ', e));
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

  //добавление пользовательской категории
  //   const addUserCategory = () => {
  //     openModal();
  //     const newCategoryName = 'Bunnies';
  //     createUserCategory(newCategoryName);
  //     window.location.reload();
  //   };

  // удаление пользовательской категории
  const handleCategoryDelete = (categoryName: string) => {
    // Ваша логика удаления категории
    console.log('Deleting category:', categoryName);
    deleteUserCategory(categoryName);
    window.location.reload();
  };

  //модалка
  const [isModalOpen, setModalOpen] = useState(false);
  //const [selectedCategory, setSelectedCategory] = useState('');

  const openModal = () => {
    setModalOpen(true);
  };
  const handleAddCategory = (newCategoryName: string) => {
    createUserCategory(newCategoryName);
    window.location.reload();
  };

  return (
    <div className={`headerButtonContainer ${isDropdownOpen ? 'open' : ''}`}>
      <button className="headerButton" onClick={handleButtonClick}>
        Пользовательские
      </button>

      {isDropdownOpen && (
        <div className="dropdownContent">
          <div className="dropdownItemsWrapper">
            <a
              href="#"
              onClick={() => {
                setDropdownOpen(false);
                openModal();
              }}
            >
              Новая
            </a>
            {items.map((item, index) => (
              <div key={index} className="categoryItem">
                <a
                  href={item.href}
                  onClick={() => handleDropdownItemClick(item.href)}
                >
                  {item.text}
                </a>
                <button onClick={() => handleCategoryDelete(item.text)}>
                  Удалить
                </button>
              </div>
            ))}
          </div>
        </div>
      )}
      <CategoryModal
        isOpen={isModalOpen}
        onClose={() => setModalOpen(false)}
        onSubmit={handleAddCategory}
      />
    </div>
  );
};
