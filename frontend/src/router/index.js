import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '../store/auth';

const routes = [
  {
    path: '/',
    redirect: '/profile'
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Login.vue'),
    meta: {
      requiresGuest: true,
      title: '用户登录 - 用户管理中心 (SUT)'  // 添加页面标题
    }
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/Register.vue'),
    meta: {
      requiresGuest: true,
      title: '用户注册 - 用户管理中心 (SUT)'  // 添加页面标题
    }
  },
  {
    path: '/profile',
    name: 'Profile',
    component: () => import('../views/Profile.vue'),
    meta: {
      requiresAuth: true,
      title: '个人资料 - 用户管理中心 (SUT)'  // 添加页面标题
    }
  },
    {
  path: '/:pathMatch(.*)*',
  name: 'NotFound',
  component: () => import('../views/NotFound.vue'),
  meta: {
    title: '页面未找到 - 用户管理中心 (SUT)'
  }
}
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

// 路由守卫，设置页面标题
router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();

  // 设置页面标题
  if (to.meta.title) {
    document.title = to.meta.title;
  } else {
    document.title = '用户管理中心 (SUT)'; // 默认标题
  }

  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next('/login');
  } else if (to.meta.requiresGuest && authStore.isAuthenticated) {
    next('/profile');
  } else {
    next();
  }
});

export default router;