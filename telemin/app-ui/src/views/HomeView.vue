<template>
  <div class="wrapper">
    <header class="header">
      <Header />
    </header>
    <main class="main"></main>
    <footer class="footer"></footer>
  </div>
</template>

<script>
// @ is an alias to /src
// import HelloWorld from '@/components/HelloWorld.vue'
import Header from "@/components/Header.vue";

export default {
  name: "HomeView",
  components: {
    // HelloWorld,
    Header,
  },
};
</script>

<style>
@import "../assets/css/base.scss";
</style>