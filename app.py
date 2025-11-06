#!/usr/bin/env python3
"""
一个包含已知漏洞依赖的示例应用
用于演示Dependabot安全扫描
"""

import requests
import flask
from urllib3.exceptions import InsecureRequestWarning

# 禁用安全警告（实际项目中不应这样做）
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def make_http_request():
    """模拟一个HTTP请求函数"""
    try:
        # 使用不安全的请求方式（用于演示）
        response = requests.get('https://httpbin.org/get', verify=False)
        print(f"请求成功: 状态码 {response.status_code}")
        return response.json()
    except Exception as e:
        print(f"请求失败: {e}")
        return None

def create_flask_app():
    """创建一个简单的Flask应用"""
    app = flask.Flask(__name__)
    
    @app.route('/')
    def hello():
        return "Hello from Vulnerable App!"
    
    @app.route('/fetch')
    def fetch_data():
        data = make_http_request()
        return flask.jsonify(data) if data else "Error fetching data"
    
    return app

if __name__ == '__main__':
    app = create_flask_app()
    print("启动应用...")
    print("已知漏洞:")
    print("- requests 2.19.0: CVE-2018-18074, CVE-2018-20206")
    print("- flask 0.12.0: 多个安全漏洞")
    print("- urllib3 1.21.1: 安全漏洞")
    app.run(debug=True, host='0.0.0.0', port=5000)