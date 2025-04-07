import requests

# Ollama 的 API 地址（默认端口为 11434）
ollama_url = "http://localhost:11434/api/generate"

# 发送一个简单的 POST 请求（测试是否可连接）
try:
    response = requests.post(
        ollama_url,
        json={
            "model": "qwen2.5:7b",  # 替换为你的模型名称
            "prompt": "你是谁"
        },
        timeout=10  # 设置超时时间
    )
    print("连接成功！状态码:", response.status_code)
    print("响应内容:", response.text)
except requests.exceptions.ConnectionError:
    print("连接失败！请检查：")
    print("1. Ollama 服务是否运行？")
    print("2. 端口号是否正确？")
except Exception as e:
    print("请求出错:", str(e))