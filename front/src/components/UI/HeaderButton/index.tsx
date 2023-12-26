import React from 'react';
import { IHeaderButton } from '../../../models';
import './headerButton.css';
import { useNavigate } from 'react-router-dom';

export const HeaderButton: React.FC<IHeaderButton> = ({ value, link }) => {
  const navigate = useNavigate();

  return (
    <button className="headerButton" onClick={() => navigate(link)}>
      {value}
    </button>
  );
};
