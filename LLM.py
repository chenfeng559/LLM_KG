import requests
import json
import yaml
import os
"""
军事问答llm

"""

def config_loader(config_path = 'prompt.yaml'):
    """
    加载系统prompt

    Args:
        config_path (str): 配置文件路径。

    Returns:
        system。
    """
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_path)
    with open(abs_path, 'r') as file:
        config = yaml.safe_load(file)

    system_prompt =config['prompt']['system_prompt']
    return system_prompt






# API的URL
url = 'http://127.0.0.1:11434/api/chat'

# 要发送的数据

sys_prompt = config_loader('prompt.yaml')
data = {
    "model": "glm4_9b",
    "messages": [
        {"role": "system", "content": sys_prompt },
        {"role": "user", "content": " "}
    ],
    "stream": False
}

input_text = "请问P-9B风神反潜机黄海侦察事件和F35战机干扰事件和敌方那个军种有关?"
# 找到role为user的message
for message in data["messages"]:
    if message["role"] == "user":
        # 将输入文本添加到content的开头
        message["content"] = input_text

json_data = json.dumps(data)

# 发送POST请求
response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})
response = response.json()


# 打印响应内容
print(response['message']['content'])
