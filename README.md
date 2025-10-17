# 用户管理中心 (SUT) - 软件测试学习项目

## 项目简介

这是一个基于 Django 和 Vue.js 的前后端分离用户管理系统，专为软件测试学习设计。项目包含了完整的用户认证、权限管理和前后端交互功能，适合用于学习 API 测试、前端测试、集成测试等软件测试技术。

## 技术栈

### 后端技术
- **框架**: Django 4.2.7 + Django REST Framework
- **数据库**: SQLite (开发环境)
- **认证**: Token 认证
- **API 文档**: Django REST Framework 自动生成

### 前端技术
- **框架**: Vue 3 + Composition API
- **路由**: Vue Router 4
- **状态管理**: Pinia
- **HTTP 客户端**: Axios
- **构建工具**: Vue CLI

## 功能特性

### 用户管理功能
- ✅ 用户注册 (用户名、邮箱、密码、手机号)
- ✅ 用户登录 (Token 认证)
- ✅ 用户退出登录
- ✅ 个人资料查看和编辑
- ✅ 权限控制和路由守卫

### 测试友好特性
- ✅ 完整的 RESTful API 设计
- ✅ 清晰的错误处理和状态码
- ✅ 前后端分离架构
- ✅ 详细的测试文档
- ✅ 预置的 API 测试脚本

## 项目结构

```
sut_demo/
├── backend/                    # Django 后端
│   ├── user_management/       # Django 项目配置
│   ├── users/                 # 用户管理应用
│   │   ├── models.py         # 用户数据模型
│   │   ├── views.py          # API 视图
│   │   ├── serializers.py    # 序列化器
│   │   └── urls.py           # API 路由
│   ├── manage.py             # Django 管理脚本
│   └── requirements.txt      # Python 依赖
├── frontend/                  # Vue 前端
│   ├── src/
│   │   ├── views/            # 页面组件
│   │   ├── router/           # 路由配置
│   │   ├── store/            # 状态管理
│   │   └── services/         # API 服务
│   └── package.json          # Node.js 依赖
├── docs/                      # 项目文档
└── tests/                     # 测试相关文件
```

## 快速开始

### 环境要求
- Python 3.8+
- Node.js 14+
- npm 或 yarn

### 后端启动步骤

```bash
# 1. 进入项目目录
cd sut_demo

# 2. 创建并激活虚拟环境 (Windows)
python -m venv venv
venv\Scripts\activate

# 3. 安装 Python 依赖
pip install -r requirements.txt

# 4. 数据库迁移
python manage.py migrate

# 5. 创建超级用户 (可选，用于管理员界面)
python manage.py createsuperuser

# 6. 启动开发服务器
python manage.py runserver
```

后端服务将在 http://127.0.0.1:8000 启动

### 前端启动步骤

```bash
# 1. 进入前端目录
cd frontend

# 2. 安装依赖
npm install

# 3. 启动开发服务器
npm run serve
```

前端服务将在 http://localhost:8080 启动

## API 接口文档

### 认证接口

| 方法 | 端点 | 描述 | 请求体 |
|------|------|------|--------|
| POST | `/api/register/` | 用户注册 | `username, email, password, password_confirm, phone` |
| POST | `/api/login/` | 用户登录 | `username, password` |
| POST | `/api/logout/` | 用户退出 | 需要 Token 认证 |
| GET | `/api/profile/` | 获取资料 | 需要 Token 认证 |
| PUT | `/api/profile/` | 更新资料 | 需要 Token 认证 |

### 测试数据示例

**用户注册:**
```json
{
  "username": "testuser",
  "email": "test@example.com",
  "password": "testpass123",
  "password_confirm": "testpass123",
  "phone": "13800138000"
}
```

**用户登录:**
```json
{
  "username": "testuser",
  "password": "testpass123"
}
```

## 测试学习指南

### 1. API 测试学习

项目提供了完整的 API 测试脚本：

```bash
# 运行基础 API 测试
python test_api.py

# 运行完整功能测试
python test_api_complete.py
```

### 2. 手动测试场景

#### 功能测试
- 用户注册流程测试
- 用户登录流程测试
- 个人资料管理测试
- 权限控制测试
- 错误处理测试

#### 接口测试
- HTTP 状态码验证
- 响应数据格式验证
- 错误消息验证
- Token 认证测试
- 请求参数验证

#### 集成测试
- 前后端数据交互测试
- 跨域请求测试
- 本地存储测试
- 路由跳转测试

### 3. 测试工具推荐

- **API 测试**: Postman, Insomnia, curl
- **前端测试**: Vue DevTools, 浏览器开发者工具
- **自动化测试**: pytest, Jest, Cypress
- **性能测试**: Apache Bench, JMeter

## 学习目标

通过本项目，您可以学习：

### 后端测试技能
- Django 单元测试编写
- DRF API 测试
- 数据库操作测试
- 认证和权限测试
- 错误处理和异常测试

### 前端测试技能
- Vue 组件测试
- 用户交互测试
- 路由导航测试
- 状态管理测试
- API 调用测试

### 集成测试技能
- 前后端联调测试
- 跨浏览器兼容性测试
- 移动端适配测试
- 性能和安全测试

## 常见测试用例

### 成功场景
1. 新用户注册并自动登录
2. 已注册用户成功登录
3. 用户查看和更新个人资料
4. 用户安全退出系统

### 异常场景
1. 注册时密码不匹配
2. 登录时凭证错误
3. 未认证访问受保护接口
4. 提交无效的表单数据

### 边界场景
1. 用户名长度边界测试
2. 密码复杂度测试
3. 邮箱格式验证测试
4. 手机号格式验证测试

## 扩展学习建议

1. **添加更多测试类型**: 性能测试、安全测试、兼容性测试
2. **实现自动化测试**: 使用 CI/CD 工具自动化测试流程
3. **扩展功能模块**: 添加更多业务功能进行复杂场景测试
4. **学习测试框架**: 深入掌握 pytest, Jest, Cypress 等测试工具

## 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个测试学习项目！

## 许可证

本项目采用 MIT 许可证，适合学习和教学使用。

---

**开始您的软件测试学习之旅吧！** 🚀

如果有任何问题，请查看项目文档或提交 Issue。
