import React from 'react';
import { IHeaderButton } from '../../../models';
import "./headerButton.css";

export const HeaderButton: React.FC<IHeaderButton> = ({value}) => {
  return <button className='headerButton'>{value}</button>;
};
