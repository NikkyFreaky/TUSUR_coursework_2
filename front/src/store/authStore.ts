import { createEvent, createStore } from 'effector';

export const loginEvent = createEvent();
export const logoutEvent = createEvent();

export const isAuthenticatedStore = createStore(false)
  .on(loginEvent, () => true)
  .reset(logoutEvent);
