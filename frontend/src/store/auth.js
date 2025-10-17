import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { authAPI } from '../services/api';

export const useAuthStore = defineStore('auth', () => {
  const user = ref(JSON.parse(localStorage.getItem('user') || 'null'));
  const token = ref(localStorage.getItem('token') || '');
  const isAuthenticated = computed(() => !!token.value);

  const setAuth = (userData, authToken) => {
    user.value = userData;
    token.value = authToken;
    localStorage.setItem('user', JSON.stringify(userData));
    localStorage.setItem('token', authToken);
  };

  const clearAuth = () => {
    user.value = null;
    token.value = '';
    localStorage.removeItem('user');
    localStorage.removeItem('token');
  };

  const login = async (credentials) => {
    try {
      const response = await authAPI.login(credentials);
      setAuth(response.data.user, response.data.token);
      return response.data;
    } catch (error) {
      throw error.response?.data || error;
    }
  };

  const register = async (userData) => {
    try {
      const response = await authAPI.register(userData);
      setAuth(response.data.user, response.data.token);
      return response.data;
    } catch (error) {
      throw error.response?.data || error;
    }
  };

const logout = async () => {
  try {
    await authAPI.logout();
  } catch (error) {
    console.error('Logout API error:', error);
  } finally {
    clearAuth();
  }
};

  const updateProfile = async (userData) => {
    try {
      const response = await authAPI.updateProfile(userData);
      user.value = response.data.user;
      localStorage.setItem('user', JSON.stringify(user.value));
      return response.data;
    } catch (error) {
      throw error.response?.data || error;
    }
  };

  return {
    user,
    token,
    isAuthenticated,
    login,
    register,
    logout,
    updateProfile,
    clearAuth,
  };
});