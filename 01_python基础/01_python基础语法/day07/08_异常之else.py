"""
    try:
        可能出现的异常代码
    except:
        异常捕获
    else:
        如果没有捕获到异常，自动执行else中缩进代码

"""

try:
    f = open("data.txt", "r", encoding="utf-8")
except Exception as e:
    print("异常出现")
    print(e)
else:
    print("  else  ")
    context = f.read()
    print(context)

print("顺序执行")


