import axios from 'axios';
import { API_URL } from '../utils/consts';

// Запрос новостей по параметру категории/дате/стране
export const getNews = async (parameter: string) => {
  const checkForSearch = parameter.split('/')[1];
  console.log('API getNews parse parameter: ', parameter);
  console.log('API getNews checkForSearch: ', checkForSearch);
  // поиск новости по ключевому слову
  if (parameter === 'search/') {
    // http://127.0.0.1:8000/api/news/search/
    const searchValue = localStorage.getItem('keyword');
    const response = await axios.post(`${API_URL}/news/search/`, {
      searchValue,
    });
    return response;
  }
  // достаем новости с юзер категории
  else if (checkForSearch === 'news_user_category') {
    const sessionid = localStorage.getItem('cookie');
    const userCategoryName = parameter.split('/')[2];
    //console.log('param', userCategoryName);
    const response = await axios.post(`${API_URL}/news_user_category/`, {
      sessionid,
      userCategoryName,
    });
    console.log('getUserCategoryNews', response);
    return response;
  }
  // печать новости по региону и парсинг
  else {
    axios.get(`${API_URL}/parse/${parametercheck(parameter)}`);
    const response = await axios.get(`${API_URL}/news/${parameter}`);
    return response;
  }
};

// Запрос всех новостей с АПИ
export const getAllNews = async () => {
  axios.get(`${API_URL}/parse/us`);
  const responce = await axios.get(`${API_URL}/news`);
  return responce;
};

// Запрос входа в аккаунт
export const logInAccount = async (username: string, password: string) => {
  const response = await axios.post(`${API_URL}/login/`, {
    username: username,
    password: password,
  });
  //Set-Cookie
  console.log('API logInAccount sessionid: ', response.data.sessionid);
  localStorage.setItem('cookie', response.data.sessionid);

  return response;
};

// запрос регистрации
export const registerInAccount = async (
  username: string,
  email: string,
  first_name: string,
  last_name: string,
  password1: string,
  password2: string,
) => {
  const response = await axios.post(`${API_URL}/register/`, {
    username: username,
    email: email,
    first_name: first_name,
    last_name: last_name,
    password1: password1,
    password2: password2,
  });

  localStorage.setItem('cookie', response.data.sessionid);

  return response;
};

// запрос на выход
export const logOutAccount = async () => {
  // Получаем куки из localStorage
  const response = await axios.post(`${API_URL}/logout/`, {
    sessionid: localStorage.getItem('cookie'),
  });
  console.log('API logOutAccount responce: ', response);
  return response;
};

// запрос данных о пользователе
export const getAccountData = async () => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/get_user_data/`, { sessionid });
  return response;
};

// запрос на получение списка пользовательских категорий
export const getUserCategories = async () => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/get_user_category/`, {
    sessionid,
  });

  return response;
};

// запрос на создание пользовательской категории
export const createUserCategory = async (category_name: string) => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/create_user_category/`, {
    sessionid,
    category_name,
  });
  console.log('createUserCategory ', response);
  return response;
};

// запрос на удаление пользовательского списка
export const deleteUserCategory = async (categoryName: string) => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/delete_category/`, {
    sessionid,
    categoryName,
  });
  console.log('createUserCategory ', response);
  return response;
};

// добавление новости в пользовательскую категорию
export const addArticleToCategory = async (
  category_name: string,
  news_title: string,
) => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/add_news_to_category/`, {
    sessionid,
    category_name,
    news_title,
  });
  console.log('addArticleToCategory ', response);
  return response;
};

// запрос на удаление новости из пользовательского списка
export const deleteArticleFromUserCategory = async (categoryName: string, title: string) => {
  const sessionid = localStorage.getItem('cookie');
  const response = await axios.post(`${API_URL}/delete_news/`, {
    sessionid,
    categoryName,
    title
  });
  console.log('deleteArticleFromUserCategory ', response);
  return response;
};

// Вспомогательная функция проверки параметра при запросе новостей
const parametercheck = (parameter: string) => {
  const countryList = [
    'ae',
    'ar',
    'at',
    'au',
    'be',
    'bg',
    'br',
    'ca',
    'ch',
    'cn',
    'co',
    'cu',
    'cz',
    'de',
    'eg',
    'fr',
    'gb',
    'gr',
    'hk',
    'hu',
    'id',
    'ie',
    'il',
    'in',
    'it',
    'jp',
    'kr',
    'lt',
    'lv',
    'ma',
    'mx',
    'my',
    'ng',
    'nl',
    'no',
    'nz',
    'ph',
    'pl',
    'pt',
    'ro',
    'rs',
    'ru',
    'sa',
    'se',
    'sg',
    'si',
    'sk',
    'th',
    'tr',
    'tw',
    'ua',
    'us',
    've',
    'za',
  ];

  return countryList.includes(parameter) ? parameter : 'us';
};
