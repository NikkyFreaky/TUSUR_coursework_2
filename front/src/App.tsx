import './App.css';
import { Root } from './routes/Root';
import { News } from './routes/News';
import { ErrorPage } from './routes/ErrorPage';
import { createBrowserRouter, RouterProvider } from 'react-router-dom';
import { Account } from './routes/Account';

const router = createBrowserRouter([
  {
    path: '/',
    element: <Root />,
    errorElement: <ErrorPage />,
    children: [
      {
        path: '/news/:parameters/:parameters',
        element: <News />,
      },
      {
        path: '/account/',
        element: <Account />,
      },
    ],
  },
]);

function App() {
  return <RouterProvider router={router} />;
}

export default App;
