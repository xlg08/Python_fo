import re

list1 = ["apple", "banana", "orange", "pear"]
list2 = []
for value in list1:
    result = re.match("apple|pear", value)
    if result:
        list2.append(result.group())
    else:
        pass

print(list2)