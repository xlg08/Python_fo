from builtins import open   # 通过 builtins.open 确保直接引用 Python 内置函数，避免环境干扰。
FILE_SUFFIX = "_chat.log"
history = []
def historyToFile(name, dialogue_history):
    fileName = None
    try:
        fileName = open(name + FILE_SUFFIX, "w", encoding="utf-8")
        for i in range(len(dialogue_history)):
            fileName.write(dialogue_history[i])
    except FileNotFoundError as fe:
        print("资源未找到：", fe)
    except Exception as e:
        print("出现的异常是：", e)
    finally:
        if fileName != None:
            fileName.close()

def getHistoryFromFile(name):
    fileName = None
    try:
        fileName = open(name + FILE_SUFFIX, "r", encoding="utf-8")
        while True:
            c = fileName.readline()
            # print(c)
            # c = c.replace("\n", "")
            # print("信息为：", c)
            if c == "":
                break
            # history.append(eval(c))
            history.append(c)
    except FileNotFoundError as fe:
        print("资源未找到：", fe)
    except Exception as e:
        print("出现的异常是：", e)
    finally:
        if fileName != None:
            fileName.close()
    return history


if __name__ == "__main__":
    # historyToFile("小艾",["张三","王五"])
    his = getHistoryFromFile("小冰")
    for i in his:
        print(i)
    # print(his)