<template>
  <HomeView/>
  <!-- <nav>
    <router-link to="/login">Login</router-link>
    <router-link to="/register">Register</router-link>
  </nav> -->
  <router-view />
</template>

<style>
@import './assets/css/zero.css';
@import './assets/css/style.css';
@import url('https://fonts.googleapis.com/css2?family=Source+Sans+Pro:wght@300;400;600;700;900&display=swap');

#app {
  font-family: 'Source Sans Pro', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #fff;
}
</style>
