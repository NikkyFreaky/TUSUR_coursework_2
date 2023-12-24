import axios from 'axios';
import { API_KEY, API_URL } from '../utils/consts';

export const getNews = async (region: string, pageNumber: number) => {
  return await axios.get(
    //`${API_URL}/top-headlines?country=${region}&pageSize=10&page=${pageNumber}${API_KEY}`,
    'http://127.0.0.1:8000/api/news/',
    //'http://localhost:5000/news',
  );
};
