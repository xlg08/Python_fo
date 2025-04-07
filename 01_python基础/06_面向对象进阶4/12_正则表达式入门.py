"""
    使用方法;
        1.导包
            import re
        2.正则匹配
            result = re.match('正则表达式', '要校验的字符串')       从前向后依次匹配。只要能匹配上即可
            result = re.search('正则表达式', '要校验的字符串')      支持分段查找
    细节：
        1.学正则表达式，就是学习正则表达式的规则。
        2.会简单
        3.正则不独属于 python 象 sql、java、php、go 等都支持

"""

import re

# # . 表示匹配任意1个字符
# #   参数一：匹配规则
# #   参数二：要匹配的字符串
# result = re.match(".lt", "ait")     # 匹配成功
# result = re.match(".lt", "你it")     # 匹配成功
# result = re.match(".lt", "你好it")    # 匹配失败
# result = re.match(".lt", "@it")    # 匹配成功
#
#
#
# # [] 匹配[]中列举的字符
# result = re.match("[abc]lt", "ait")     # 匹配成功
# result = re.match("[abc]lt", "hit")     # 匹配失败
# result = re.match("[abc]lt", "a it")     # 匹配失败
#
#
#
# # [^] 取反  匹配[]中列举的字符
# result = re.match('[^abc]it','ait')     # 匹配失败
# result = re.match('[^abc]it','a it')     # 匹配失败
#
#
# # [3-7]  从3开始到7
# # result = re.match('[3-7]it','7it')
# result = re.match('[a-zA-Z0-9]it', '_it')
#
# # \d  匹配数字 0-9
# result = re.match('a\\dit', 'a-8it')        # a8it

# \D 即：匹配的不是数字，
result = re.match("a\\Dit", "a-8it")        # 表示a与it之间不能是数字

# # \s匹配空白  即：空格  tab键
# result = re.match('a\sit','a it')       # 匹配成功
# result = re.match('a\sit','a    it')        # 匹配失败
# result = re.match('a\sit','a\tit')      # 匹配成功
#
# # \S 匹配非空白
# result = re.match('a\Sit','a_it')   # 匹配成功
#
# # \w 匹配非特殊字符    a-z A-Z 0-9 汉字
# result = re.match('a[\w]it','a_it')
#
# # \W 匹配特殊字符  非字母  非数字  非汉字
# result = re.match('a[\W]it','a_it')

# * 匹配前一个字符出现0次或者无限次   即：可有可无
#   因此 * 和前一个字符是一体的
#   .*  表示此处有没有东西都可以
# result = re.match("hm.*", "abchm123")
# result = re.match("hm.*", "hm123")

# + 匹配前一个字符出现1次或者无限次
#    因此 + 和前一个字符是一体的
#    .+  表示此处至少有一个任意字符
# result = re.match(".+hm.*", "abchm")
# result = re.match(".+hm.*", "hm123")
# result = re.match(".+hm.*", "abchm123")

# ? 匹配前一个字符出现1次或者0次
#   因此 ? 和前一个字符是一体的
#   .?  表示此处如果有字符只能有一个，要不就没有
# result = re.match(".?hm.*", "abchm123")
# result = re.match(".?hm.*", "ahm123")


if result:
    print(result.group())
else:
    print("匹配失败")