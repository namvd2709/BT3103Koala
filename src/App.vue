<!--https://bt3103-3c2fe.firebaseio.com-->
<template>
  <div id="app">
    <router-link v-bind:to="'/profile'">Set up your profile here!</router-link>
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app",
  computed: {
    currentRoute () {
      return this.$route.name
    }
  }
};
</script>
<!-- styling for the component -->
<style>
#app {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
