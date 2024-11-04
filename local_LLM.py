import requests
import json
import yaml
import os


def config_loader(config_path='prompt.yaml'):
    """
    加载系统prompt

    Args:
        config_path (str): 配置文件路径。

    Returns:
        system_prompt (str): 系统prompt内容。
    """
    abs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), config_path)
    with open(abs_path, 'r') as file:
        config = yaml.safe_load(file)

    system_prompt = config['prompt']['ccf_system_prompt']
    return system_prompt


def query_military_llm(input_text, url='http://127.0.0.1:11434/api/chat', config_path='prompt.yaml'):
    """
    调用军事问答LLM接口

    Args:
        input_text (str): 用户输入的问题文本
        url (str): API接口地址
        config_path (str): 配置文件路径

    Returns:
        str: LLM的响应内容
    """
    try:
        # 加载系统prompt
        sys_prompt = config_loader(config_path)

        # 构造请求数据
        data = {
            "model": "glm4_9b",
            "messages": [
                {"role": "system", "content": sys_prompt},
                {"role": "user", "content": input_text}
            ],
            "stream": False
        }

        # 转换为JSON格式
        json_data = json.dumps(data)

        # 发送POST请求
        response = requests.post(
            url,
            data=json_data,
            headers={'Content-Type': 'application/json'}
        )

        # 解析响应
        response_data = response.json()
        return response_data['message']['content']

    except Exception as e:
        print(f"Error occurred: {str(e)}")
        return None


# 使用示例
if __name__ == "__main__":
    question = "请问P-9B风神反潜机黄海侦察事件和F35战机干扰事件和敌方那个军种有关?"
    result = query_military_llm(question)
    print(result)