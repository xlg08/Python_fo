"""
pip install ollama
pip install langchain
需求：通过python调用API实现基于qwen2在0.5b数据集下实现对文本的续写，
     用户输入一个简短的故事开头，系统能够生成一段连贯、有趣的续写内容。
①：导模块
②：调用模块中的方法 ，对数据进行处理
③：对处理后的数据进行输出
"""
# ①：导模块
import ollama

# ②：调用模块中的方法 ，对数据进行处理
#  调用ollama 聊天对话接口
# model='qwen2:1.5b' 指定处理模型
# messages 格式apifox里面拿的请求结构
#role ： system 系统的
        # user 用户的
        # assistant  小助手
s = ollama.chat(model='qwen2.5:1.5b', messages=[{"role": "user", "content": "从前有座山，山里有一个庙 续写一下这个小故事"}])
# print(s) 我们直接打印 ，发现里面返回的好多数据 ，但是我们只需要 Message.content
# print(s['message'])  打印了，但是发现里面带来一些我们不需要的内容role='assistant'  images=None tool_calls=None
#                      经过分析只需要content
#写法一
# print(s['message']['content'])
#写法二
print(s.message.content)
