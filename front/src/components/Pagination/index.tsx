import React, { useEffect } from 'react';
import './pagination.css';

interface IPagination {
  pages: number[];
  changePage: React.Dispatch<React.SetStateAction<number>>;
  //setPages
}

export const Pagination: React.FC<IPagination> = ({ pages, changePage }) => {
  return (
    <div className="pagination">
      {pages.map((page) => (
        <span className="pagination-onePage" onClick={() => changePage(page)}>
          <div className="onePage-pageNumber">{page}</div>
        </span>
      ))}
    </div>
  );
};
