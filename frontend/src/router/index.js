import { createRouter, createWebHistory } from "vue-router";
import LoginView from "@/views/LoginView.vue";
import RegisterView from "@/views/RegisterView.vue";
import AdminHomeView from "@/views/AdminHomeView.vue";
import AdminCreateView from "@/views/AdminCreateView.vue";
import AdminDeleteView from "@/views/AdminDeleteView.vue";
import AdminUpdateView from "@/views/AdminUpdateView.vue";
import HomeView from "@/views/HomeView.vue";
import SimulatorView from "@/views/SimulatorView.vue";
import ErrorView from "@/views/ErrorView.vue";
import SimulationView from "@/views/SimulationView.vue";
import ProfileView from "@/views/ProfileView.vue";

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
  },
  {
    path: "/register",
    name: "register",
    component: RegisterView,
  },
  {
    path: "/admin",
    name: "admin",
    component: AdminHomeView,
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
  },
  {
    path: "/simulator",
    name: "simulator",
    component: SimulatorView,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "errorPage",
    component: ErrorView,
  },
  {
    path: "/simulation",
    name: "simulation",
    component: SimulationView,
    props: true,
  },
  {
    path: "/profile",
    name: "profile",
    component: ProfileView,
  },
  {
    path: "/admin/create",
    name: "adminCreate",
    component: AdminCreateView,
  },
  {
    path: "/admin/delete",
    name: "adminDelete",
    component: AdminDeleteView,
  },
  {
    path: "/admin/update",
    name: "adminUpdate",
    component: AdminUpdateView,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
