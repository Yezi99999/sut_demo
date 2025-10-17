<template>
  <div class="not-found-container">
    <div class="not-found-content">
      <h1>404</h1>
      <h2>页面未找到</h2>
      <p>抱歉，您访问的页面不存在。</p>
      <router-link to="/" class="home-link">返回首页</router-link>
    </div>
  </div>
</template>

<script setup>
// 设置页面标题
document.title = '页面未找到 - 用户管理中心 (SUT)';
</script>

<style scoped>
.not-found-container {
  min-height: 100vh;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  padding: 20px;
}

.not-found-content {
  background: white;
  padding: 60px 40px;
  border-radius: 12px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
  text-align: center;
  max-width: 500px;
  width: 100%;
}

.not-found-content h1 {
  font-size: 120px;
  color: #667eea;
  margin: 0;
  line-height: 1;
}

.not-found-content h2 {
  font-size: 24px;
  color: #333;
  margin: 20px 0 10px;
}

.not-found-content p {
  color: #666;
  margin-bottom: 30px;
  font-size: 16px;
}

.home-link {
  display: inline-block;
  padding: 12px 30px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  color: white;
  text-decoration: none;
  border-radius: 6px;
  font-weight: 600;
  transition: opacity 0.3s;
}

.home-link:hover {
  opacity: 0.9;
}
</style>