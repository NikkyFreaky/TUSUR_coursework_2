СТРУКТУРА ПРИЛОЖЕНИЯ ПО ПАПКАМ:

-- node_modules не трогать, все сломаешь, плакать будешь
-- public я не уверена, что там за файлы, ну и не трогаю, всякие иам веб-иконки
-- src тут весь код
---- API в этой папке весь код про то, как клиент присасывается к серверу
---- assets тут всякие картинки, иконки, шрифты
---- components это папка с react-компонентами
------ AuthModal содержимое модалки со входом в акаунт, верстка и логика
------ Modal верстка и логика модалки
------ NewsElement это компонента с карточкой одноЙ новости
------ NewsList это компонента, которая выводит список NewsElement
------ Pagination это пагинация
------ RegisterModal содержимое модалки с регистрацией, верстка и логика
------ UI тут компоненты типа инпутов, кнопок, выпадающих списков, которые реюзаются в проекте постоянно
---- models в этой папке модели, т.е. интерфейсы, объекты, которые в виде пропсов на вход получают разные реакт-компоненты
---- routes в этой папке лежат страницы приложения
------ Account страница аккаунта юзера
------ ErrorPage страница с ошибкой, если по странному пути зайти
------ News элемент со списком новостей
------ Root корневая страница, хэдер
---- utils сейчас тут файл consts, в котором удобно лежат пути для обращения к бэку

КАК СДЕЛАТЬ, ЧТОБ РАБОТАЛО:

0. Я работаю в VSCode. ВОЗМОЖНО вам потребуется установить node.js (у меня версия v18.15.0)
1. Проект с гита подгружаем
2. Открываем в консоли папку, в которой лежит фронт, скорее всего cd front
3. Устанавливаем node_modules консольной командой npm install
4. После установки модулей(может занять время) пишем в консоль npm start
5. Приложение открывается в браузере. Вы восхитительны