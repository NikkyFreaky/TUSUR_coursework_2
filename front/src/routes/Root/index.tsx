import { Header } from '../../components/Header';
import { Outlet } from 'react-router-dom';

export const Root = () => {
  return (
    <div className="mainPage">
      <Header />
      <div id="detail">
        <Outlet />
      </div>
    </div>
  );
};
