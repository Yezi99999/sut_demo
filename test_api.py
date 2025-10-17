import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"


def test_registration():
    """测试用户注册"""
    print("测试用户注册...")
    data = {
        "username": "testuser2",
        "email": "test2@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123",
        "phone": "13800138001"
    }

    response = requests.post(f"{BASE_URL}/register/", json=data)
    print(f"注册响应: {response.status_code}")
    if response.status_code == 201:
        print("注册成功!")
        return response.json()
    else:
        print(f"注册失败: {response.text}")
        return None


def test_login():
    """测试用户登录"""
    print("\n测试用户登录...")
    data = {
        "username": "testuser2",
        "password": "testpass123"
    }

    response = requests.post(f"{BASE_URL}/login/", json=data)
    print(f"登录响应: {response.status_code}")
    if response.status_code == 200:
        print("登录成功!")
        return response.json()
    else:
        print(f"登录失败: {response.text}")
        return None


def test_profile(token):
    """测试获取用户资料"""
    print("\n测试获取用户资料...")
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    response = requests.get(f"{BASE_URL}/profile/", headers=headers)
    print(f"资料响应: {response.status_code}")
    if response.status_code == 200:
        print("获取资料成功!")
        print(f"用户信息: {response.json()}")
    else:
        print(f"获取资料失败: {response.text}")


if __name__ == "__main__":
    # 测试流程
    reg_result = test_registration()
    if reg_result:
        login_result = test_login()
        if login_result:
            token = login_result.get('token')
            test_profile(token)