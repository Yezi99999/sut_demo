<template>
  <div class="profile-container" v-if="user">
    <nav class="navbar">
      <div class="nav-brand">
        <h1>用户管理中心 (SUT)</h1>
      </div>
      <div class="nav-menu">
        <span class="user-info">欢迎, {{ user.username }}</span>
        <button @click="handleLogout" class="logout-btn">退出登录</button>
      </div>
    </nav>

    <div class="profile-content">
      <div class="profile-card">
        <div class="avatar-section">
          <div class="avatar">
            {{ userInitials }}
          </div>
          <h3>{{ user.username }}</h3>
          <p class="role">{{ roleText }}</p>
        </div>

        <form @submit.prevent="handleUpdate" class="profile-form">
          <div class="form-row">
            <div class="form-group">
              <label for="email">邮箱</label>
              <input
                type="email"
                id="email"
                v-model="form.email"
                required
              />
            </div>

            <div class="form-group">
              <label for="phone">手机号</label>
              <input
                type="tel"
                id="phone"
                v-model="form.phone"
              />
            </div>
          </div>

          <div class="form-row">
            <div class="form-group">
              <label for="first_name">姓</label>
              <input
                type="text"
                id="first_name"
                v-model="form.first_name"
              />
            </div>

            <div class="form-group">
              <label for="last_name">名</label>
              <input
                type="text"
                id="last_name"
                v-model="form.last_name"
              />
            </div>
          </div>

          <button type="submit" :disabled="loading" class="update-btn">
            {{ loading ? '更新中...' : '更新资料' }}
          </button>

          <div v-if="message" class="success-message">
            {{ message }}
          </div>

          <div v-if="error" class="error-message">
            {{ error }}
          </div>
        </form>

        <div class="profile-info">
          <h4>账户信息</h4>
          <div class="info-item">
            <span class="label">注册时间:</span>
            <span class="value">{{ formatDate(user.date_joined) }}</span>
          </div>
          <div class="info-item">
            <span class="label">最后登录:</span>
            <span class="value">{{ formatDate(user.last_login) }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- 添加加载状态或未登录状态 -->
  <div v-else class="loading-container">
    <div class="loading-message">
      <p>正在退出登录...</p>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useAuthStore } from '../store/auth';

const router = useRouter();
const authStore = useAuthStore();

const user = computed(() => authStore.user);
const form = ref({
  email: '',
  phone: '',
  first_name: '',
  last_name: ''
});

const loading = ref(false);
const error = ref('');
const message = ref('');

const userInitials = computed(() => {
  if (!user.value) return '';
  const first = user.value.first_name?.[0] || '';
  const last = user.value.last_name?.[0] || '';
  return (first + last) || user.value.username[0].toUpperCase();
});

const roleText = computed(() => {
  if (!user.value) return '';
  const roles = {
    admin: '管理员',
    user: '普通用户',
    viewer: '游客'
  };
  return roles[user.value?.role] || '未知';
});

const formatDate = (dateString) => {
  if (!dateString) return '未知';
  return new Date(dateString).toLocaleString('zh-CN');
};

const handleUpdate = async () => {
  loading.value = true;
  error.value = '';
  message.value = '';

  try {
    await authStore.updateProfile(form.value);
    message.value = '资料更新成功';
  } catch (err) {
    if (typeof err === 'object') {
      error.value = Object.values(err).flat().join(', ');
    } else {
      error.value = err || '更新失败，请重试';
    }
  } finally {
    loading.value = false;
  }
};

const handleLogout = async () => {
  try {
    await authStore.logout();
    // 确保重定向到登录页面
    router.push('/login');
  } catch (error) {
    console.error('退出登录错误:', error);
    // 即使 API 调用失败，也清除本地状态并重定向
    authStore.clearAuth();
    router.push('/login');
  }
};

// 监听用户状态变化
watch(user, (newUser) => {
  if (!newUser) {
    // 如果用户状态变为 null，重定向到登录页
    router.push('/login');
  }
});

onMounted(() => {
  if (user.value) {
    form.value = {
      email: user.value.email || '',
      phone: user.value.phone || '',
      first_name: user.value.first_name || '',
      last_name: user.value.last_name || ''
    };
  } else {
    // 如果没有用户信息，重定向到登录页
    router.push('/login');
  }
});
</script>

<style scoped>
.profile-container {
  min-height: 100vh;
  background-color: #f5f7fa;
}

.navbar {
  background: white;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand h1 {
  color: #667eea;
  font-size: 1.5rem;
  margin: 0;
}

.nav-menu {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.user-info {
  color: #666;
  font-weight: 500;
}

.logout-btn {
  padding: 8px 16px;
  background: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background 0.3s;
}

.logout-btn:hover {
  background: #c0392b;
}

.profile-content {
  max-width: 800px;
  margin: 0 auto;
  padding: 30px 20px;
}

.profile-card {
  background: white;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  padding: 30px;
}

.avatar-section {
  text-align: center;
  margin-bottom: 30px;
  padding-bottom: 30px;
  border-bottom: 1px solid #eee;
}

.avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 24px;
  font-weight: bold;
  margin: 0 auto 15px;
}

.avatar-section h3 {
  margin: 0 0 5px;
  color: #333;
}

.role {
  color: #666;
  margin: 0;
  font-size: 14px;
}

.form-row {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 20px;
  margin-bottom: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

label {
  margin-bottom: 8px;
  font-weight: 500;
  color: #555;
}

input {
  padding: 10px;
  border: 2px solid #e1e5e9;
  border-radius: 6px;
  font-size: 16px;
  transition: border-color 0.3s;
}

input:focus {
  outline: none;
  border-color: #667eea;
}

.update-btn {
  padding: 12px 30px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 16px;
  font-weight: 600;
  cursor: pointer;
  transition: opacity 0.3s;
}

.update-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.update-btn:hover:not(:disabled) {
  opacity: 0.9;
}

.success-message {
  margin-top: 15px;
  padding: 10px;
  background: #efe;
  border: 1px solid #cfc;
  border-radius: 4px;
  color: #363;
  text-align: center;
}

.error-message {
  margin-top: 15px;
  padding: 10px;
  background: #fee;
  border: 1px solid #fcc;
  border-radius: 4px;
  color: #c33;
  text-align: center;
}

.profile-info {
  margin-top: 30px;
  padding-top: 20px;
  border-top: 1px solid #eee;
}

.profile-info h4 {
  margin-bottom: 15px;
  color: #333;
}

.info-item {
  display: flex;
  justify-content: space-between;
  padding: 8px 0;
  border-bottom: 1px solid #f5f5f5;
}

.label {
  color: #666;
  font-weight: 500;
}

.value {
  color: #333;
}

.loading-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.loading-message {
  background: white;
  padding: 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  text-align: center;
}

.loading-message p {
  color: #333;
  font-size: 18px;
  margin: 0;
}

@media (max-width: 768px) {
  .form-row {
    grid-template-columns: 1fr;
  }

  .navbar {
    flex-direction: column;
    gap: 15px;
    text-align: center;
  }

  .profile-content {
    padding: 20px 15px;
  }
}
</style>