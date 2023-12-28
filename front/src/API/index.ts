import axios from 'axios';
import { API_URL } from '../utils/consts';
import { updateCookie } from '../store/authStore';

// Запрос новостей по параметру категории/дате/стране
export const getNews = async (parameter: string) => {
  const checkForSearch = parameter.split('/')[0];
  console.log('API getNews parse parameter: ', parameter);
  if (checkForSearch === 'search') {
    // http://127.0.0.1:8000/api/news/search/
    //const keyword = parameter.split('/')[1];
    // console.log('API getNews keyword: ', keyword);

    //const headers = { q: keyword };
    // const responce = await axios.get(`${API_URL}/news/${parameter}`);
    //const responce = await axios.get(`${API_URL}/news/search/`, { headers });

    const searchValue = localStorage.getItem('keyword');
    const response = await axios.post(`${API_URL}/news/search/`, { searchValue });

    return response;
  } else {
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

  const cookie = response.headers['set-cookie'];
  if (cookie) {
    console.log('API register request', cookie);
    localStorage.setItem('cookie', JSON.stringify(cookie));
  }

  return response;
};

// // запрос на выход
// export const logOutAccount = async () => {
//   const response = await axios.post(`${API_URL}/logout/`);

//   return response;
// };

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

// поиск по ключевым словам
// http://127.0.0.1:8000/api/news/search/
export const getSearchResult = async (keyword: string) => {
  const headers = { q: keyword };
  const response = await axios.get(`${API_URL}/news/search/?q=` + keyword);
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
