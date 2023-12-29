import React, { useState } from 'react';
import './news-list.css';
import { INewsList } from '../../models';
import { NewsElement } from '../NewsElement';
import { Pagination } from '../Pagination'; // Подключаем компонент Pagination
import { getUserCategories } from '../../API';

interface INewsListWithPagination extends INewsList {
  currentPage: number;
  setCurrentPage: React.Dispatch<React.SetStateAction<number>>;
}

export const NewsList: React.FC<INewsListWithPagination> = ({
  message,
  news,
  success,
  currentPage,
  setCurrentPage,
}) => {
  const itemsPerPage = 10; // Количество новостей на странице

  // Вычисляем начальный и конечный индексы для текущей страницы
  const startIndex = (currentPage - 1) * itemsPerPage;
  const endIndex = startIndex + itemsPerPage;

  // Получаем новости для текущей страницы
  const currentNews = news.slice(startIndex, endIndex);

  return (
    <div className="newsList-container">
      {success ? (
        <div>
          {currentNews.map((article) => (
            <NewsElement article={article}  />
          ))}
          <Pagination
            pages={Array.from(
              { length: Math.ceil(news.length / itemsPerPage) },
              (_, i) => i + 1,
            )}
            currentPage={currentPage}
            changePage={setCurrentPage}
          />
        </div>
      ) : (
        <div>При получении новостей произошла ошибка.</div>
      )}
    </div>
  );
};
