<template>
  <div
    id="app"
    :style="{'background-image': 'url(' + require('../assets/NUS_Background_3.png') + ')', 'height': '1500px'}"
  >
    <header>
      <h1>{{job}}</h1>
      <div v-if="job === 'Business Analyst'">
        <img src="../assets/Business_Analyst.png" width="500">
      </div>
      <div v-else-if="job === 'Data Analyst'">
        <img src="../assets/Data_Analyst.png" width="500">
      </div>
      <div v-else-if="job === 'IT Consultant'">
        <img src="../assets/IT_Consultant.png" width="500">
      </div>
      <div v-else-if="job === 'Software Engineer'">
        <img src="../assets/Software_Engineer.png" width="500">
      </div>
      <div v-else-if="job === 'Information Security Officer'">
        <img src="../assets/Information_Security_Officer.png" width="500">
      </div>
      <h3>
        Job Description: </h3>
        {{GetJobDescription(jobDescription,job)}}
        <br>
        <h3>How much seniors earn: </h3>{{GetSalaryByJob(salary,major,industry,job)}}
        <br>
        <h3>Where seniors work: </h3>{{GetCompaniesByJob(companies,major,industry,job)}}
        <br>
        <h3>How many interviews seniors go for on average: </h3>{{GetNumInterview(numInterviews,major,industry,job)}}
        <br>
        <h3>When seniors are getting the job: </h3>
        Early: {{GetofferDate90ByJob(offerDate90,major,industry,job)}}
        <br>
        Average: {{GetofferDate50ByJob(offerDate50,major,industry,job)}}
        <br>
        Late: {{GetofferDate10ByJob(offerDate10,major,industry,job)}}
        <br>
        <h3>Who are the seniors that you are competing with: </h3>
        <pie-chart :data="GetCompetitionForJob(competitors, industry, job)"></pie-chart>
        <br>
        <a
          href="https://vafs.nus.edu.sg/adfs/ls/?SAMLRequest=jZJPb4IwHIa%2FCukdihWdNELC9DATtxFhO%2ByylFKlSWkZv%2BLmtx%2FI%2FriL2blP3%2Fftky6B1aqhSWcrvRNvnQDrfNRKAz0fRKhrNTUMJFDNagHUcpol91tKPJ82rbGGG4WcBEC0Vhq9Mhq6WrSZaI%2BSi6fdNkKVtQ1QjKGSRWGUsJWrO3A51B6c6kZJLu3J46bG2Q%2FhARg8FBGcPmY5ctb9MqnZ0PGbeGR78PosT5SdBwfMyj1gBRg5m3WEXud%2BOQ%2FK2Wwa7kMyJTdFuOAFZ0KUvCAlC3oMoBMbDZZpGyHiT0LXD9zJNPcJJQtKghfkpF%2BvvJW6lPpwXUkxQkDv8jx1x%2BnPooXz7B5A8XIQS8%2FF7YXq67Hs2y%2BK%2F29zULjEF3Vjd0Mf%2BvzNOjU9e3ISpcz7qhXMighNEI7HK3%2F%2FRPwJ&RelayState=cookie%3A1555122504_2c16"
        >Explore Jobs</a>
      </h3>
    </header>
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
import bg from "../assets/NUS_Background_4.png";
import ba from "../assets/Business_Analyst.png";

import router from "../router";

export default {
  name: "app",
  data() {
    return {
      wordcloud: null
    };
  },
  firebase: {
    // we should use async await here
    salary: {
      source: db.ref("ave_salary"),
      asObject: true
    },
    companies: {
      source: db.ref("companie"),
      asObject: true
    },
    offerDate10: {
      source: db.ref("offer_date_10"),
      asObject: true
    },
    offerDate50: {
      source: db.ref("offer_date_50"),
      asObject: true
    },
    offerDate90: {
      source: db.ref("offer_date_90"),
      asObject: true
    },
    numInterviews: {
      source: db.ref("num_interviews"),
      asObject: true
    },
    jobDescription: {
      source: db.ref("job_description"),
      asObject: true
    },
    competitors: {
      source: db.ref("competition"),
      asObject: true
    }
  },
  created() {
    this.route = this.$route.params;
    this.job = this.$route.params.id;
    this.major = this.$route.params.id3;
    this.industry = this.$route.params.id2;
  },
  methods: {
    GetSalaryByJob: function(salary, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(salary);

      if (salary[major] === undefined) {
        console.log("Error");
      } else {
        console.log("NAM");
        return salary[major][industry][job];
      }
    },
    GetCompaniesByJob: function(companies, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(companies);
      if (companies[major] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return companies[major][industry][job];
      }
    },
    GetofferDate10ByJob: function(offerDate10, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(offerDate10);
      if (offerDate10[major] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return offerDate10[major][industry][job];
      }
    },
    GetofferDate50ByJob: function(offerDate50, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(offerDate50);
      if (offerDate50[major] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return offerDate50[major][industry][job];
      }
    },
    GetofferDate90ByJob: function(offerDate90, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(offerDate90);
      if (offerDate90[major] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return offerDate90[major][industry][job];
      }
    },
    GetNumInterview: function(numInterviews, major, industry, job) {
      console.log("GETTING");
      console.log(major);
      console.log(numInterviews);
      if (numInterviews[major] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return numInterviews[major][industry][job];
      }
    },
    GetCompetitionForJob: function(competitors, industry, job) {
      console.log("GETTING");
      console.log(industry);
      console.log(competitors);
      if (competitors[industry] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return competitors[industry][job];
      }
    },
    GetJobDescription: function(jobDescription, job) {
      console.log("GETTING");
      console.log(job);
      console.log(jobDescription);
      if (jobDescription[job] === undefined) {
        console.log("Error");
      } else {
        console.log("Felicia");
        return jobDescription[job];
      }
    },
    GetImage: function() {
      if (job === "Business Analytics") {
        this.wordcloud = ba;
      }
    }
  }
};
</script>script>