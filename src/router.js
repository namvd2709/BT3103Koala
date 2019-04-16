import Vue from "vue";
// import VueFire from "vuefire";
import Router from "vue-router";

import Profile from '@/components/profile'
import Jobs from '@/components/jobs'
import IndvJobs from "./components/IndvJobs.vue";

Vue.use(Router);

const routes = [
  { path: '/', name: "profile", component: Profile },
  { path: "/profile", component: Profile, name: "profile" },
  { path: "/jobs", component: Jobs, name: "jobs" },
  { path: "/jobs/:id", component: Jobs, name: "jobs1" },
  { path: "/jobs/:id2", component: Jobs, name: "jobs2" },
  { path: "/IndvJobs", component: IndvJobs, name: "IndvJobs"},
  { path: "/IndvJobs/:id", component: IndvJobs, name: "IndvJobs1" },
  { path: "/IndvJobs/:id2", component: IndvJobs, name: "IndvJobs2" },
  { path: "/IndvJobs/:id3", component: IndvJobs, name: "IndvJobs3" }
];

export default routes;