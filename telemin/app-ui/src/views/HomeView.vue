<template>
  <div class="wrapper">
    <header class="header">
      <div class="header__container">
        <a href="/" class="header__logo">
          <img src="../assets/img/yandex_logo.svg" alt="Логотип" />
        </a>
        <nav class="header__menu menu">
          <ul class="menu__list">
            <li class="menu__item">
              <router-link to="/register" class="router__link"
                >Пост</router-link
              >
            </li>
            <li class="menu__item">
              <router-link to="/register" class="router__link"
                >Мой профиль</router-link
              >
            </li>
            <li class="menu__item">
              <router-link to="/register" class="router__link"
                >Как это работает</router-link
              >
            </li>
            <li class="menu__item">
              <router-link to="/register" class="router__link"
                >Комьюнити</router-link
              >
            </li>
          </ul>
        </nav>
        <div class="header__button">
          <router-link to="/register" class="button button_dark"
                >Для разработчиков</router-link
              >
        </div>
        <a href=""><img src="img/avatar.png" alt="" class="avatar" /></a>
      </div>
    </header>
  </div>
  <router-view />
</template>

<style>
.router__link {
  font-size: 16px;
  color: rgba(255, 255, 255, 0.7);
  transition-property: background-color, color, border-color;
  transition-duration: 0.25s, 0.2s, 0.2s;
  transition-timing-function: ease, ease, ease;
}

.router__link:hover {
  color: rgba(255, 255, 255, 0.9);
}
</style>
