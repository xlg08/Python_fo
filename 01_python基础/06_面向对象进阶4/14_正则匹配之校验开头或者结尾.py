import re

"""`

    ^  : 匹配字符串开头
    $  : 匹配字符串结尾

    正则校验：
        | 代表 或的意思
        ()  代表分组 ，从左向右数， 第几个小括号吧( , 就表示第几组
        \num 代表引用的第几组的内容
        
        拓展：
            (?P<分组名>)     设置分组
            (?P=分组名)      使用分组
"""


# result = re.match("")


# 校验手机号
#   规则1：长度必须是11位
#   规则2：第一位必须是1
#   规则3：必须都是纯数字
#   规则4：第二位数字  3-9

# result = re.match("^1[3-9]\d{9}$", "13216541558")
#
# result = re.match("^\d+.", "qabc123xyz")        # 失败
# result = re.match("\d+.", "123xyz")

# ^ 用来限定一个字符串的开头是什么，与后面临近的内容构成一个整体
#   因此 ^\d+ 是一个整体，用来限定开头至少有一个数字
# result = re.match("^\\d+.*[a-zA-Z]{3}", "abc123xyz123")
# result = re.match("^\\d+.", "123xyz")

# result = re.match("^\\d+.*[a-zA-Z]{3}", "abc123zyz12")
# result = re.match("^\\d+.*[a-zA-Z]{3}", "123你好abc12a")

# $ 用来限定一个字符串的结尾是什么，与前面临近的内容构成一个整体
#   因此 [a-zA-Z]{3}$ 是一个整体，用来限定结尾至少有三个大写或者小写字母
# result = re.match("^\\d+.*[a-zA-Z]{3}$", "123你好abc12")
result = re.match("^\\d+.*[a-zA-Z]{3}$", "123你好abc12abc")

if result:
    print(result.group())
else:
    print("匹配失败")