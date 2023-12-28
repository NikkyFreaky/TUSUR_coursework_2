import axios from 'axios';
import { API_URL } from '../utils/consts';
import { updateCookie } from '../store/authStore';

// Запрос новостей по параметру категории/дате/стране
export const getNews = async (parameter: string) => {
  axios.get(`${API_URL}/parse/${parametercheck(parameter)}`);
  const responce = await axios.get(`${API_URL}/news/${parameter}`);
  return responce;
};

// Запрос всех новостей с АПИ
export const getAllNews = async () => {
  axios.get(`${API_URL}/parse/us`);
  const responce = await axios.get(`${API_URL}/news`);
  return responce;
};

// Запрос входа в аккаунт
export const logInAccount = async (username: string, password: string) => {
  const response = await axios.post(
    `${API_URL}/login/`,
    {
      username: username,
      password: password,
    },
    {
      headers: {
        'Set-Cookie': '1',
      },
    },
  );
  //Set-Cookie

  const headers = response.headers;
  console.log('API login responce ', headers);
  console.log('API login headers', headers);

  // if (response.headers) {
  //   const sessionid = response.headers;
  //   console.log('API login SESSIONID ', sessionid);
  //   localStorage.setItem('cookie', JSON.stringify(sessionid));
  // }
  // console.log('API login LOCALSTORAGE ', localStorage.getItem('cookie'));

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
  const headers = {
    'Content-Type': 'application/json',
    Cookie: localStorage.getItem('cookie'), // Убедитесь, что у вас есть куки для установки
  };
  console.log(headers);

  const response = await axios.post(
    `${API_URL}/logout/`,
    {},
    { headers, withCredentials: true },
  );

  return response;
};

// запрос данных о пользователе
export const getAccountData = async () => {
  const response = await axios.get(`${API_URL}/get_user_data/`);
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
