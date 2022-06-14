import { createRouter, createWebHistory } from 'vue-router'
import LoginView from '../views/LoginView.vue'
import RegisterView from '../views/RegisterView.vue'
import AdminView from '../views/AdminView.vue'
import HomeView from '../views/HomeView.vue'
import SimulatorView from '../views/SimulatorView.vue'
import ErrorView from '../views/ErrorView.vue'
import SimulationView from '../views/SimulationView.vue'
import ProfileView from '../views/ProfileView.vue'

const routes = [
  {
    path: '/login',
    name: 'login',
    component: LoginView
  },
  {
    path: '/register',
    name: 'register',
    component: RegisterView
  },
  {
    path: '/admin',
    name: 'admin',
    component: AdminView
  },
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/simulator',
    name: 'simulator',
    component: SimulatorView
  },
  {
    path: '/:pathMatch(.*)*',
    name: 'errorPage',
    component: ErrorView
  },
  {
    path: '/simulation/:id',
    name: 'simulation',
    component: SimulationView,
    props: route => ({ id: parseInt(route.params.id) })
  },
  {
    path: '/profile',
    name: 'profile',
    component: ProfileView
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
