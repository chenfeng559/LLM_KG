import requests
import json

# API的URL
url = 'http://127.0.0.1:11434/api/chat'
input_text = "我今年18岁，我的舅舅今年38岁，我的爷爷今年72岁，我和舅舅一共多少岁了？"

# 要发送的数据
data = {
    "model": "llama3",
    "messages": [
        {"role": "system", "content": "你是一个数学家，你可以计算任何算式。"},
        {"role": "user", "content": " "}
    ],
    "stream": False
}

# 找到role为user的message
for message in data["messages"]:
    if message["role"] == "user":
        # 将输入文本添加到content的开头
        message["content"] = input_text

# 将字典转换为JSON格式的字符串
json_data = json.dumps(data)

# 发送POST请求
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

# 打印响应内容
print(response.text)
