import React, { useEffect, useState } from 'react';
import { NewsList } from '../../components/NewsList';
import { INewsList } from '../../models';
import { getAllNews, getNews } from '../../API';
import { Pagination } from '../../components/Pagination';
import './news.css';

import { useParams } from 'react-router-dom';
import { useLocation } from 'react-router-dom';

export const News = () => {
  const [news, setNews] = useState<INewsList>();
  const [pages, setPages] = useState<number[]>([]);
  const [currentPage, setCurrentPage] = useState<number>(1);

  const location = useLocation();
  const urlParams = location.pathname.replace('/news/', ''); // Получаем все параметры после '/news/'

  useEffect(() => {
    if (
      urlParams === '' ||
      urlParams === undefined ||
      urlParams === null ||
      urlParams.length === 0
    ) {
      getAllNews().then((res) => {
        setNews(res.data);
        // getPageCount(res.data.length);
      });
    } else {
      getNews(urlParams).then((res) => {
        setNews(res.data);
        // getPageCount(res.data.length);
      });
    }
  }, [currentPage]);

  // const getPageCount = (count: number) => {
  //   const pageCount = Math.ceil(count / 10);
  //   const pagesArray = [];
  //   for (let i = 1; i <= pageCount; i++) pagesArray.push(i);
  //   setPages(pagesArray);
  // };

  return (
    <div className="news">
      {news !== undefined && (
        <div>
          <NewsList
            message={news.message}
            news={news.news}
            success={news.success}
          />
        </div>
      )}
      {/* <Pagination pages={pages} changePage={setCurrentPage} /> */}
    </div>
  );
};
