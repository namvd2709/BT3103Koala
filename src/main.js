// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
//import the vue instance
import Vue from "vue";

//import firebase
import VueFire from "vuefire";
import firebase from "firebase/app";

Vue.use(VueFire);
// if (!firebase.apps.length) {
//   firebase.initializeApp({
//     projectId: "bt3103",
//     databaseURL: "https://bt3103-3c2fe.firebaseio.com"
//   });
// }

//import the App component
import App from "./App";
//import the vue router
import VueRouter from "vue-router";
//tell vue to use the router
Vue.use(VueRouter);

import { routes } from "./router";

// Create the router instance and pass the `routes` option
// You can pass in additional options here, but let's
// keep it simple for now.
const router = new VueRouter({
  routes, // short for routes: routes
  mode: "history"
});
//instatinat the vue instance
new Vue({
  //define the selector for the root component
  el: "#app",
  //pass the template to the root component
  template: "<App/>",
  //declare components that the root component can access
  components: { App },
  //pass in the router to the Vue instance
  router
}).$mount("#app"); //mount the router on the app
