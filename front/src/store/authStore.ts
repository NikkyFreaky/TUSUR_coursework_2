import { createEvent, createStore, combine } from 'effector';

// Создаем события для обновления полей
export const updateName = createEvent<string>();
export const updateSurname = createEvent<string>();
export const updateLogin = createEvent<string>();
export const updateEmail = createEvent<string>();

// Создаем события для аутентификации
export const loginEvent = createEvent();
export const logoutEvent = createEvent();

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

// Создаем стор для isAuth
export const isAuthenticatedStore = createStore<boolean>(false)
  .on(loginEvent, () => true)
  .reset(logoutEvent);

// Комбинируем все сторы в один объект
export const userStore = combine({
  name: nameStore,
  surname: surnameStore,
  login: loginStore,
  email: emailStore,
  isAuth: isAuthenticatedStore,
});

// использование
// updateName('John');
// updateSurname('Doe');
// updateLogin('john_doe');
// updateEmail('john@example.com');
