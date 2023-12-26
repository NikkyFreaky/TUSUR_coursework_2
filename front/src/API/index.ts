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

// Вспомогательная функция проверки паметра
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
