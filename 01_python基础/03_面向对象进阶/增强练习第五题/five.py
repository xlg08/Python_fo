import fileUtils

"""
    1. 创建`ChatBot`类，属性：`name`（名字）、`dialogue_history`（对话历史列表）、mood
    2. 方法：
        - `reply(message)`：根据用户输入生成回复，若消息含"开心"或"难过"关键词
            - 开心：我也为您感到高兴！
            - 难过：希望我能帮到您...
            - 如果以上词都不包含：收到您的消息，正在处理中~
        - `show_history()`：显示最近3条对话记录。
        - `__str__`：返回机器人活跃状态，如「AI客服小冰 | 已处理对话：5条」。
    3. 使用`__del__`销毁对象时自动保存对话记录到文件.当销毁对象打印：
        对话记录已加密保存到【小冰_chat.log】

例如：
    测试一：
        请输入您的状态：我今天很难过
        😔 希望我能帮到您...
    测试二：
        请输入您的状态：我饿了。想吃饭
        🤖 收到您的消息，正在处理中~
    测试三：调用show_history显示最近3条对话	
        最近对话记录：
            小冰：😔 希望我能帮到您...
            用户：系统出问题了
            小冰：🤖 收到您的消息，正在处理中~

    测试四：删除对象提示：
        对话记录已加密保存到【小冰_chat.log】

    实现以上对话要求

"""
class ChatBot:
    def __init__(self, name):
        self.name = name
        self.dialogue_history = []      # 对话历史列表
        self.mood = "难过", "开心"       # 心情

    def reply(self, message):       # 消息回复
        if message == (None or "" or " "):
            print("请输入内容！！")
        elif self.mood[1] in message and self.mood[0] in message:
            self.addHistory("用户", message)
            print("希望我为您感到高兴的同时能帮到您...")
            self.addHistory(self.name, "希望我为您感到高兴的同时能帮到您...")
        elif self.mood[1] in message:
            self.addHistory("用户", message)
            print("我也为您感到高兴！")
            self.addHistory(self.name, " 我也为您感到高兴！")
        elif self.mood[0] in message:
            self.addHistory("用户", message)
            print("😔 希望我能帮到您...")
            self.addHistory(self.name, " 😔 希望我能帮到您...")
        elif message == "展示对话内容":
            his = self.show_history()
            for i in range(len(his)):
                print(his[i], end="")
        elif message == "展示小助手":
            print(self)
        # elif message == "退出系统":
        #     self.__del__()
        #     os._exit(0)
        else:
            self.addHistory("用户", message)
            print("🤖 收到您的消息，正在处理中~")
            self.addHistory(self.name, " 🤖 收到您的消息，正在处理中~")

    def addHistory(self, name, message):
        self.dialogue_history.append(f"{name}:{message}\n")

    def show_history(self):
        return self.dialogue_history[-1:-4:-1]

    def __str__(self):
        return f"「AI客服{self.name} | 已处理对话：{len(self.dialogue_history)}条」"

    def __del__(self):

        # fileName = open(self.name + "_chat.log", "w", encoding="utf-8")
        # for i in range(len(self.dialogue_history)):
        #     fileName.write(self.dialogue_history[i])

        fileUtils.historyToFile(self.name, self.dialogue_history)
        print(f"对话记录已加密保存到【{self.name}_chat.log】")

name = "小冰"
chatBox = ChatBot(name)

print("""你可以输入您的状态
也可以通过输入：
    1.展示对话内容
    2.展示小助手
    3.退出 
    等等来操作本系统""")
while True:

    message = input("请输入您的状态：\n")
    if message == "退出":
        del chatBox
        break
    else:
        chatBox.reply(message)