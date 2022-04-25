<template>
  <div class="header__container">
    <a href="." class="header__logo">
      <img src="../assets/img/yandex_logo.svg" alt="Логотип" />
    </a>
    <nav class="header__menu menu">
      <ul class="menu__list">
        <li class="menu__item"><a href="" class="menu__link">Пост</a></li>
        <li class="menu__item">
          <a href="" class="menu__link">Мой профиль</a>
        </li>
        <li class="menu__item">
          <a href="" class="menu__link">Как это работает</a>
        </li>
        <li class="menu__item"><a href="" class="menu__link">Комьюнити</a></li>
      </ul>
    </nav>
    <div class="header__button">
      <a href="" class="button button_dark">Для разработчиков</a>
    </div>
    <img src="../assets/img/avatar.png" alt="" class="avatar" />
    <Dropdown title="Services" :items="services"/>
  </div>
</template>

<script>
import Dropdown from "./Dropdown.vue";

export default {
  name: "Header",
  components: {
    Dropdown,
  },
  data () {
    return {
      services:[
        {
          title: 'Web',
          link: '#'
        },
        {
          title: 'Design',
          link: '#'
        }
      ]
    }
  }
}
</script>

<style scoped lang="scss">

</style>