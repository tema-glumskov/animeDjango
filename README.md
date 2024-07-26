**Проект AnimeDjango**

1. **Общие сведения**

   Проект представляет собой веб-сайт, посвященный аниме и манге. Он содержит функции регистрации, авторизации, просмотра аниме и манги, а также управления избранными аниме пользователя.

3. **Django ORM Модели**
   - `AnimeTitle`: Модель для хранения информации о разных аниме.
   - `AnimeUser`: Модель для хранения информации о пользователях, включая их логин, пароль и список избранных аниме.

4. **Представления**
   - `index`: Главная страница сайта. Пользователь может ввести логин и пароль для авторизации. Если введенные данные совпадают с данными администратора, пользователь автоматически авторизуется и переходит на страницу с аниме. Если введенные данные совпадают с данными пользователя, пользователь также автоматически авторизуется и переходит на страницу с аниме. Если пользователь не авторизован, он может зарегистрироваться на сайте.
   - `anime`: Страница с аниме. Если пользователь авторизован, он может добавлять аниме в избранное.
   - `manga`: Страница с мангой.
   - `register`: Страница регистрации нового пользователя.
   - `account`: Страница профиля пользователя. Он может выйти из аккаунта, удалить аниме из избранного или просмотреть свой список избранных аниме.

5. **Функции**
   - `index`: Функция, которая реализует представление главной страницы и содержит в себе форму для входа на сайт.
   - `anime`: Функция, которая реализует представление страницы с аниме.
   - `register`: Функция, которая проверяет, существует ли пользователь с таким же логином. Если такой пользователь не существует, функция создает нового пользователя.
   - `account`: Функция, которая реализует представление личного кабинета.
     
6. **Сообщения**
   - `messages`: Библиотека, которая позволяет отображать сообщения на странице. Например, после успешной регистрации пользователя отображается сообщение "Регистрация прошла успешно!".

7. **URL-адреса**
   - `/`: Главная страница сайта.
   - `/anime/`: Страница с аниме.
   - `/manga/`: Страница с мангой.
   - `/register/`: Страница регистрации нового пользователя.
   - `/account/`: Страница личного кабинета.

8. **Переменные**
   - `login`: Переменная, которая хранит логин пользователя.
   - `locked`: Переменная, которая хранит информацию о том, авторизован ли пользователь. Если пользователь авторизован, `locked` равно `False`, иначе `True`.

9. **Стили и шаблоны**
   - `index.html`: Главная страница сайта.
   - `anime.html`: Страница с аниме.
   - `register.html`: Страница регистрации нового пользователя.
   - `account.html`: Страница профиля пользователя.
   - `style.css`: Файл со стилями сайта.

10. **Внешние ссылки**
   - `https://youtu.be/dQw4w9WgXcQ?si=N5_ZSmfxseh59c3k`: Ссылка на видео, которая показывается, когда пользователь не авторизован и пытается просмотреть страницу с аниме или зайти в личный кабинет.
