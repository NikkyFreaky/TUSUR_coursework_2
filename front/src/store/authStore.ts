import { createEvent, createStore, combine } from 'effector';

// Создаем события для обновления полей
export const updateName = createEvent<string>();
export const updateSurname = createEvent<string>();
export const updateLogin = createEvent<string>();
export const updateEmail = createEvent<string>();
export const updateIsAuth = createEvent<boolean>();
export const updateCookie = createEvent<string[]>();

// Создаем сторы для каждого поля
export const nameStore = createStore<string>('').on(
  updateName,
  (_, value) => value,
);

export const surnameStore = createStore<string>('').on(
  updateSurname,
  (_, value) => value,
);

export const loginStore = createStore<string>('').on(
  updateLogin,
  (_, value) => value,
);

export const emailStore = createStore<string>('').on(
  updateEmail,
  (_, value) => value,
);

export const isAuthenticatedStore = createStore<boolean>(false).on(
  updateIsAuth,
  (_, value) => value,
);

export const cookieStore = createStore<string[]>([]).on(
  updateCookie,
  (_, value) => value,
);

// Комбинируем все сторы в один объект
export const userStore = combine({
  name: nameStore,
  surname: surnameStore,
  login: loginStore,
  email: emailStore,
  isAuth: isAuthenticatedStore,
  cookie: cookieStore,
  // keyword: keywordStore,
});

// Подписываемся на обновления и сохраняем в Local Storage
userStore.watch((state) => {
  localStorage.setItem('userData', JSON.stringify(state));
});

// Загружаем данные из Local Storage при инициализации
const storedData = localStorage.getItem('userData');
if (storedData) {
  const parsedData = JSON.parse(storedData);
  updateName(parsedData.name);
  updateSurname(parsedData.surname);
  updateLogin(parsedData.login);
  updateEmail(parsedData.email);
  updateIsAuth(parsedData.isAuth);
  updateCookie(parsedData.cookie);
}
