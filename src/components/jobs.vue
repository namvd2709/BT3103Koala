<template>
<div :style="{'background-image': 'url(' + require('../assets/NUS_Background_3.png') + ')', 'height': '1000px'}">
  <header>
    <h1>Recommended Jobs</h1>
  </header>
  <body id="app">
    <div>
      <!-- .Technology is currently hardcoded.-->
      <pie-chart :data="GetByMajor(roles, major, industry)"></pie-chart>

      <br>Explore jobs:
      <br>
      <br>
      <form>
        <select name="job" v-model="job">
          <option v-for="job1 in GetJobList(roles, major, industry)" selected :value="job1" v-bind:key="job1">{{job1}}</option>
          <!--         <option value="Data Analyst">Data Analyst</option>
          <option value="Software Engineer">Software Engineer</option>
          <option value="IT Consultant">IT Consultant</option>
          <option value="Information Security Officer">Information Security Officer</option>
          -->
        </select>
        <br>
        <input type="button" value="Let's GO" @click="GoToRoute();">
      </form>
    </div>
  </body>
</div>
</template>

<script>
import Vue from "vue";
import Vuex from "vuex";
import Vuexfire from "vuexfire";
import Chartkick from "chartkick";
import VueChartkick from "vue-chartkick";
import firebase from "firebase";
import VueChartjs from "vue-chartjs";
import Chart from "chart.js";
import { db } from "../config";
import bg from "../assets/NUS_Background_3.png";
import router from "../router";

Vue.use(VueChartkick, { adapter: Chart });

export default {
  name: "app",
  data() {
    return {
      job: ""
    };
  },

  firebase: {
    // we should use async await here
    roles: {
      source: db.ref("jobs"),
      asObject: true
    }
  },
  created() {
    this.route = this.$route.params;
    this.major = this.$route.params.id;
    this.industry = this.$route.params.id2;
  },
  methods: {
    GetByMajor: function(roles, major, industry) {
      console.log("GETTING");
      if (roles[major] === undefined) {
        console.log(roles);
      } else if (roles[major][industry] === undefined) {
        console.log(roles[major]);
      } else {
        return roles[major][industry];
      }
    },
    GoToRoute: function() {
      this.$router.push({
        name: "IndvJobs",
        params: { id: this.job, id2: this.industry, id3: this.major }
      });
    },
    GetJobList: function(roles, major, industry) {
      if (roles[major] === undefined) {
        console.log("WAITING");
      } else if (roles[major][industry] === undefined) {
        console.log("WAITING");
      } else {
        let result = Object.keys(roles[major][industry]);
        return result;
      }
    }
  }
};
</script>





