import local_LLM
import os
from datetime import datetime

def read_questions_from_txt(file_path):
    """从txt文件读取问题列表"""
    with open(file_path, 'r', encoding='utf-8') as f:
        questions = [line.strip() for line in f.readlines() if line.strip()]
    return questions

def save_responses_to_txt(questions_and_responses, output_file):
    """将问题和响应保存到txt文件"""
    with open(output_file, 'w', encoding='utf-8') as f:
        for i, (question, response) in enumerate(questions_and_responses, 1):
            f.write(f"问题 {i}:\n{question}\n\n")
            f.write(f"响应 {i}:\n{response}\n")
            f.write("\n" + "="*50 + "\n\n")  # 分隔符


def process_questions(input_file, output_dir='outputs'):
    """处理问题并保存响应"""
    # 创建输出目录（如果不存在）
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 生成输出文件名（包含时间戳）
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_file = os.path.join(output_dir, f'responses_{timestamp}.txt')

    # 读取问题
    questions = read_questions_from_txt(input_file)

    # 存储问题和响应
    questions_and_responses = []

    # 处理每个问题
    for i, question in enumerate(questions, 1):
        print(f"处理问题 {i}/{len(questions)}: {question}")
        try:
            # 调用LLM获取响应
            response = local_LLM.query_military_llm(question)
            questions_and_responses.append((question, response))
            print(f"已获得响应 {i}")
        except Exception as e:
            error_message = f"处理失败: {str(e)}"
            questions_and_responses.append((question, error_message))
            print(f"问题 {i} 处理失败: {str(e)}")

    # 保存结果
    save_responses_to_txt(questions_and_responses, output_file)
    print(f"\n处理完成！响应已保存到: {output_file}")

    return output_file


if __name__ == "__main__":

    input_file = "question.txt"  # 你的问题文件路径

    # 处理问题并获取输出文件路径
    output_file = process_questions(input_file)



