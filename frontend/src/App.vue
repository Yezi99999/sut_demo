<template>
  <div id="app">
    <router-view />
  </div>
</template>

<script setup>
// 空脚本，所有逻辑在组件中处理
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  background-color: #f5f7fa;
  color: #333;
  line-height: 1.6;
}

#app {
  min-height: 100vh;
}
</style>