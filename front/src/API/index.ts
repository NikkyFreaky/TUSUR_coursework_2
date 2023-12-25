import axios from 'axios';
import { API_URL } from '../utils/consts';

export const getNews = async (region: string) => {
  axios.get(`${API_URL}/parse/${region}`);
  const responce = await axios.get(`${API_URL}/news/country/${region}`);
  return responce;
};
