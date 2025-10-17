import requests
import json


def test_api():
    base_url = "http://127.0.0.1:8000/api"

    print("=== 测试用户注册 ===")
    register_data = {
        "username": "testuser",
        "email": "test@example.com",
        "password": "testpass123",
        "password_confirm": "testpass123",
        "phone": "13800138000"
    }

    try:
        response = requests.post(f"{base_url}/register/", json=register_data)
        print(f"状态码: {response.status_code}")
        if response.status_code == 201:
            print("✅ 注册成功!")
            result = response.json()
            print(f"用户: {result['user']['username']}")
            print(f"Token: {result['token']}")
            return result['token']
        else:
            print(f"❌ 注册失败: {response.text}")
            return None
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None


def test_login():
    print("\n=== 测试用户登录 ===")
    login_data = {
        "username": "testuser",
        "password": "testpass123"
    }

    try:
        response = requests.post("http://127.0.0.1:8000/api/login/", json=login_data)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print("✅ 登录成功!")
            result = response.json()
            print(f"用户: {result['user']['username']}")
            print(f"Token: {result['token']}")
            return result['token']
        else:
            print(f"❌ 登录失败: {response.text}")
            return None
    except Exception as e:
        print(f"❌ 请求异常: {e}")
        return None


def test_profile(token):
    print("\n=== 测试获取用户资料 ===")
    headers = {
        "Authorization": f"Token {token}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get("http://127.0.0.1:8000/api/profile/", headers=headers)
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print("✅ 获取资料成功!")
            profile = response.json()
            print(f"用户名: {profile['username']}")
            print(f"邮箱: {profile['email']}")
            print(f"手机: {profile['phone']}")
            print(f"角色: {profile['role']}")
        else:
            print(f"❌ 获取资料失败: {response.text}")
    except Exception as e:
        print(f"❌ 请求异常: {e}")


if __name__ == "__main__":
    # 先测试注册
    token = test_api()

    # 如果注册成功，测试登录和资料
    if token:
        test_profile(token)
    else:
        # 如果用户已存在，测试登录
        token = test_login()
        if token:
            test_profile(token)