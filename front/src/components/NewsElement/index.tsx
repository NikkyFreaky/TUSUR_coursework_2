import './news-element.css';
import { IHeaderDropdownItem, INewsElement } from '../../models';
import placeholder from '../../assets/placeholder.jpg';
import { NewsElementDropdown } from '../UI/NewsElementDropdown';
import { useLocation } from 'react-router-dom';
import { useState, useEffect } from 'react';
import { deleteArticleFromUserCategory } from '../../API';

interface props {
  article: INewsElement;
}

export const NewsElement: React.FC<props> = ({ article }) => {
  const [buttonVisible, setButtonVisible] = useState<boolean>(false);
  const [categoryName, setCategoryName] = useState<string>('');

  const location = useLocation();
  const urlParams = location.pathname.split('/');

  useEffect(() => {
    if (urlParams[1] === 'news_user_category') {
      setButtonVisible(true);
      setCategoryName(urlParams[2]);
    } else {
      setButtonVisible(false);
      setCategoryName('');
    }
  }, [urlParams]);

  const openInNewTab = (url: string) => {
    window.open(url, '_blank', 'noopener,noreferrer');
  };

  const deleteButtonHandler = (articleTitle: string) => {
    //функция, удаляющая новость
    deleteArticleFromUserCategory(categoryName, articleTitle);
    window.location.reload();
  };

  return (
    <div className="article-card">
      <div className="article-card__picture">
        {article.assets.images !== null &&
        article.assets.images !== undefined ? (
          <img src={article.assets.images} alt="Картинка" />
        ) : (
          <img src={placeholder} alt="Картинка" />
        )}
      </div>
      <div className="article-card__main-info">
        <div
          className="main-info_title"
          onClick={() => openInNewTab(article.source.link)}
        >
          {article.title}
        </div>
        <div className="main-info__desc">{article.description}</div>
        <div>{article.event_date}</div>
      </div>
      <NewsElementDropdown articleTitle={article.title} />
      {buttonVisible ? (
        <button onClick={() => deleteButtonHandler(article.title)}>-</button>
      ) : (
        <div></div>
      )}
    </div>
  );
};
