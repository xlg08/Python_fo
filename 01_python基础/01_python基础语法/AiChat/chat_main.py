"""
    该模块用于充当聊天机器人的前端模块
    即：接受用户录入的问题，调用chat_utils模块，get_response函数
    获取模型处理的结果。并且通过streamlit的前端页面进行展示

"""



# 1.导包
import streamlit as st      # streamlit库：python代码实现的前端页面开发并且部署
from chat_utils import get_response     # 自定义模块：封装模型处理函数，获取处理结果
from langchain.memory import ConversationBufferMemory   # 聊天机器人核心模块 ConversationBufferMemory 存储聊天机器人上下文对话


# 2.标题
st.title("智聊机器人")

# 3.判断是否有历史数据记录对象，如果没有就创建，并存储所有记录消息
if "memory" not in st.session_state:    # session_state 存储会话状态的     ，用户存储会话数据
    # 3.1创建一个ConversationBufferMemory对象，并且将数据存储到session_state
    st.session_state.memory = ConversationBufferMemory()
    print("ssm是：",st.session_state.memory)
    # 3.2添加机器人欢迎语句
    st.session_state.message = [{'role':"assistant", 'content':'你好，。。。'}]

# st.session_state.message.append({'role':"user", 'content':'你认识周杰伦吗？'})
# st.session_state.message.append({'role':"assistant", 'content':'不认识'})
# st.session_state.message.append({'role':"user", 'content':'你走'})
# st.session_state.message.append({'role':"assistant", 'content':'我不'})

# 4.遍历session_state.message里面所有记录
for message in st.session_state.message:
    # 4.1通过 聊天消息容器，用于显示达能前角色内容
    with st.chat_message(message['role']):
        # 4.2显示当前角色的内容
        st.markdown(message['content'])

    # st1 = st.chat_message(message['role'])
    # st1.markdown(message['content'])

# 5.接受用户录入的内容
promt = st.chat_input("请输入您要咨询的问题")

# 6.判断用户录入的问题是否为空，不为空，才向下执行
if promt:
    # 7.把用户信息添加到历史记录中
    st.session_state.message.append({'role':'user','content':promt})
    st.chat_message("user").markdown(promt)

    with st.spinner("Ai小助手正在思考中。。。"):
        response = get_response(st.session_state.message)

    response = get_response(st.session_state.message)

    # 8.把模型处理的结果添加到历史消息记录中，并且展示给前端页面
    st.session_state.message.append({'role':'assistant','content':response})
    st.chat_message("assistant").markdown(response)

