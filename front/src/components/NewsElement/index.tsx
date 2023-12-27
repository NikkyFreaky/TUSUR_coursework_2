import React from 'react';
import './news-element.css';
import { INewsElement } from '../../models';
import placeholder from '../../assets/placeholder.jpg';

interface props {
  article: INewsElement;
}

export const NewsElement: React.FC<props> = ({ article }) => {
  const openInNewTab = (url: string) => {
    window.open(url, '_blank', 'noopener,noreferrer');
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
      </div>
    </div>
  );
};
