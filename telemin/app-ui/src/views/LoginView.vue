<template>
  <div class="wrapper">
    <div class="login__block">
      <img src="../assets/img/yandex_logo.svg" alt="Логотип" />
      <!-- <h1>Авторизация</h1> -->
      <div class="login-form">
        <form action="" method="post">
          <input type="text" name="" id="login" placeholder="Имя пользователя"/>
          <input type="password" name="" id="password" placeholder="Пароль" />
          <input type="submit" value="Войти" id="entry">
        </form>
        <div class="support__block">
          <p>Войти с помощью</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "LoginView",
  components: {
    // HelloWorld,
    // Header,
  },
};
</script>

<style lang="scss" scoped>
img {
    width: 130px;
    margin-bottom: 25px;
}
.wrapper {
  height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.login__block {
  width: max-content;
  background-color: fff;
  padding: 32px 20px;
  border-radius: 18px;
  text-align: center;
  box-shadow: 0px 4px 36px 1px rgba(34, 60, 80, 0.11);
  border: 1px solid rgba(0, 0, 0, 0.05);

  h1 {
    font-size: 28px;
    font-weight: bold;
    text-align: center;
    margin-bottom: 15px;
  }

  form {
    width: 100%;
    input {
      display: block;
      margin-bottom: 10px;
      border-radius: 8px;
      padding: 12px 30px 12px 15px;
      border: none;
      background-color: #fff;
      font-size: 15px;
      font-weight: normal;
      border: 1px solid rgba(0, 0, 0, 0.09);
    }
  }
}

#entry {
    display: flex;
    width: 100%;
    background-color: rgba(34, 60, 80, 0.11);
    justify-content: center;
}
</style>