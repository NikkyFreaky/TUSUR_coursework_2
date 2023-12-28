import axios from 'axios';
import { API_URL } from '../utils/consts';

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
  const response = await axios.post(`${API_URL}/login/`, {
    username: username,
    password: password,
  });
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
  return response;
};

// запрос на выход
export const logOutAccount = async () => {
  const response = await axios.post(`${API_URL}/logout/`);
  return response;
};

// запрос о войденности юзера в аккаунт на бэке
export const isUserEntered = async () => {
  const response = await axios.get(`${API_URL}/check_online/`);
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
