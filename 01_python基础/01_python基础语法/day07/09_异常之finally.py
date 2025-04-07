"""
    try:
        可能出现异常代码
    except:
        如果出现异常，要执行代码
    else:
        如果没有出现异常，要执行代码
    finally:
        无论异常与否，要执行代码

"""
f = None
try:
    f = open("data.txt", "r")
except Exception as e:
    print("出异常了！")
    print(e)
else:
    print("2没有异常，程序打印")
    c = f.read()
    f.close()
finally:
    print("3终会打印")
    if f != None:
        f.close()


"""    要保证程序的健壮性和鲁棒性     """
