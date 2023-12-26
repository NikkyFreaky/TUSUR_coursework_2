import React from 'react';
import './pagination.css';

interface IPagination {
  pages: number[];
  changePage: React.Dispatch<React.SetStateAction<number>>;
  currentPage: number;
}

export const Pagination: React.FC<IPagination> = ({
  pages,
  changePage,
  currentPage,
}) => {
  const MAX_VISIBLE_PAGES = 5; // Максимальное количество видимых страниц
  const getPageList = () => {
    if (pages.length <= MAX_VISIBLE_PAGES) {
      return pages;
    } else {
      const firstVisiblePages = pages.slice(0, MAX_VISIBLE_PAGES - 1);
      const lastPage = pages[pages.length - 1];
      return [...firstVisiblePages, 'ellipsis', lastPage];
    }
  };

  const handlePageClick = (page: number | string) => {
    if (typeof page === 'number') {
      changePage(page);
    }
  };

  return (
    <div className="pagination">
      {getPageList().map((page, index) => (
        <span
          key={index}
          className={`pagination-onePage ${
            currentPage === page ? 'active' : ''
          }`}
          onClick={() => handlePageClick(page)}
        >
          {page === 'ellipsis' ? '...' : page}
        </span>
      ))}
    </div>
  );
};
