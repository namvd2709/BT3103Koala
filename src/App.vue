<!--https://bt3103-3c2fe.firebaseio.com-->
<template>
  <div id="app">
    <!-- the router outlet, where all matched components would ber viewed  -->
    <router-link v-bind:to="'/profile'">Set up your profile here!</router-link>
    <!-- src\components\App.vue
    <router-link v-bind:to="'/profile'">Update Profile Link</router-link>
    <!--    <router-link v-bind:to="'/paramdetails'">Industry</router-link>
    
    <router-link v-bind:to="'/brenda'">Brenda</router-link>
    -->
    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: "app"
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
