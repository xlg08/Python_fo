"""
    链表介绍：
        概述：
            是数据结构的线性结构的一种，每一阶段只有一个前驱和一个后继
        作用：
            优化顺序表的弊端（如果没有足够的内存空间，会导致扩容失败）
            链表的扩容，有地就行。连不连续无所谓
        组成：
            链表 有 节点 ， 节点由  元素域 和链接域 组成
        分类：


    自定义代码模拟链表：
        1.自定义SingleNode类，  表示节点类
            属性：
                item   数值域（元素域）
                next   地址域（链接域）   此处不是本节点的地址，而是他下一个结点的地址
        2.自定义SingleLinkList类   表示：链表
            属性：
                head  表示头节点 ， 指向链表的第一个节点
            行为：
                is_empty(self)  : 链表是否为空
                length(self):判断链表长度
                traverse(self)：遍历整个链表
                add(self,item)：给链表头部添加元素
                append(self,item)：链表尾部添加元素
                insert(self,item)：指定位置添加元素
                remove(self,item)：删除节点
                search(self,item)：查询节点是否存在

"""


# 自定义SingleNode 类，表示节点类
class SingleNode:
    # 初始化属性
    def __init__(self, item):
        self.item = item  # 元素域（数值域）
        self.next = None  # 链接域（地址域）


# 自定义SingleLinklist类，表示链表
class SingleLinklist:
    # 初始化链表
    def __init__(self, node=None):
        self.head = node

    def is_empty(self):  # 链表是否为空
        # 思路：判断头节点是否为Node，如果为None，则列表为空
        # 写法一 if else
        # if self.head is None:
        #     return True
        # else:
        #     return False

        # 写法二
        # return True if self.head is None else False

        # 写法三
        return self.head is None

    """
        设置 cur 表示当前元素，然后定义一个计数器初始化为 0 
        如果 cur 不为 None ， count + 1 ,并让cur = cur.next （把下一个地址给当前） 直到cur 为 None ，结束
        打印计数器的值，即：链表的长度
    """

    def length(self):  # 判断链表长度
        # 默认从头开始
        cur = self.head
        # 初始化计数器
        count = 0
        # 开始遍历，只要当前节点不为空，就一直循环
        while cur is not None:
            count += 1
            cur = cur.next
        return count

    def traverse(self):  # 遍历整个链表
        cur = self.head
        while cur is not None:
            print(f"当前节点元素值为：{cur.item}")
            cur = cur.next

    """
        1. 先初始化一个新节点  （搞一个新节点）
        2. 让一个新节点的next，之前链表的头节点
        3. 然后让头节点指向新节点
    
        提示：执行顺序不能变，如果先让head指向新节点，之前的节点的next地址就丢了，节点就回不去了
    """

    def add(self, item):  # 给链表头部添加元素
        # 1.创建一个新节点
        new_node = SingleNode(item)
        # 2.设置新节点的地址域，指向头节点
        new_node.next = self.head
        # 3.设置头节点指向新节点
        self.head = new_node

    """
        1. 创建一个新节点
        2. 核心点就是 cur.next 的值Node
        3. 让尾节点的next等于新节点
    """

    def append(self, item):  # 链表尾部添加元素
        new_node = SingleNode(item)
        if self.is_empty():
            self.head = new_node
        else:
            # 此处说明链表不为空，需要找到链表的尾节点
            # 默认从头开始
            cur = self.head
            while cur.next is not None:
                # 地址后移
                cur = cur.next
            # 此处说明，cur 就是最后一个节点，所以设置它的地址指向新的节点
            cur.next = new_node

    """
        Insert(pos, item) 在指定位置添加节点 insert(位置, 值)
        如果pos小于0，说明头插， pos大于链表长度，说明尾插
        
        例如：在 pos = 2 处插入元素  如何处理
            即：需要在pos=1 后面插入，这样新元素才会变成了 pos = 2
                1. 需要找到插入位置的前一个元素(pos=1)的位置
                2. 让新的节点的next指向pos2的地址（也就是pos1的next中的值）
            目标：要插入pos=2这个位置，经过分析，找到pos=1这个节点，
                所以 while count < pos - 1 要成立的话，
                    while count <  2  - 1 成立的话，count为0，当count=0的时候，是pos=0的节点
                        所以此时，pos=0 cur，则需要拿到pos = 1 的节点的位置，故cur = cur.next
                        因为 pos = 0 是当前 cur ，所以需要更新 cur.next ,需要更新计数器 count += 1
        
    """
    # pos为插入的位置，也即插入后该元素在列表中的位置
    def insert(self, pos, item):  # 指定位置添加元素
        # 头插
        if pos <= 0:
            self.add(item)
        elif pos >= self.length():
            self.append(item)
        else:  # 此处为插入到任意位置
            # 走到此处，说明pos是合法的，即：中间值，想要找到插入到哪个元素
            cur = self.head
            # 定义当前节点的位置
            count = 0
            while count < pos - 1:      # pos - 1 是要插入位置的前一个结点的位置
                # 走到此处，说明还没有找到插入前的那个节点，就节点后移，计数器+1
                cur = cur.next
                count += 1
            # 走到此处，cur就是插入位置前的那一个节点，封装新节点
            new_node = SingleNode(item)
            # 设置新节点的地址域，指向插入位置前的那个节点的地址域
            new_node.next = cur.next
            # 设置插入位置前的那个节点的地址域指向新节点
            cur.next = new_node

    """
        情况一：想要删除cur，则需要通过cur定位到前一个pre,
            然后直接越过他，指向cur的后面节点
            最后让当前节点next的值给pre的next，即：让pre的next指向当前元素的下一个节点 pre.next = cur.next
        情况二：
            如果当前元素是链表的头节点，直接让head指向cur的下一个元素
        情况三：
            如果当前节点不是要删除的节点，就把cur给pre，然后把cur.next 给cur，
            即：cur = cur.next 当前节点向后走
    """

    def remove(self, item):  # 删除节点
        # 默认从头开始
        cur = self.head
        pre = None
        while cur is not None:          # 判断当前节点是否为空
            # 判断当前节点是否是要删除的节点
            if cur.item == item:
                # 判断要删除的节点是否是头节点
                if cur == self.head:
                    # 直接设置头节点为当前节点的下一个节点
                    self.head == cur.next
                else:
                    # 走到此处，说明要删除的节点不是头节点，直接设置前驱(pre)的地址域指向当前节点的地址域即可
                    pre.next = cur.next
                    cur.next = None
                    # 走到此处，说明删除成功，返回即可
                return
            else:
                # 走到此处，说明当前节点不是要删除的节点，后移，pre也要后移
                pre = cur
                print("cur:", cur.item)
                cur = cur.next

    """
        传入item值，如果cur.item = item 则返回True
            否则 cur.next 给 cur 即：cur = cur.next
    """

    def search(self, item):  # 查询节点是否存在
        # 默认从头节点开始
        cur = self.head
        # 只要当前节点不为空，就一直循环
        while cur is not None:
            if cur.item == item:
                return True
            # 如果当前节点不是要找的节点，后移
            cur = cur.next
        return False


if __name__ == '__main__':
    # 1.1测试节点类
    node1 = SingleNode(10)
    # 1.2打印当前节点的元素域 和 链接域
    print(f"元素域(数值域)：{node1.item}")
    print(f"链接域(地址域)：{node1.next}")
    print(f"node1对象：{node1}")
    print(f"node1类型：{type(node1)}")
    print(f"node1地址：{id(node1)}")

    my_linklist = SingleLinklist(node1)
    print(f"头节点：{my_linklist}")
    print(f"头节点的元素域：{my_linklist.head.item}")
    print(f"头节点的地址域：{my_linklist.head.next}")

    # 3.1 测试链表是否为空
    # my_linklist = SingleLinklist()
    print(f"是否为空链表：{my_linklist.is_empty()}")

    # 测试链表长度
    print(f"当前链表的长度：{my_linklist.length()}")

    # 测试遍历
    my_linklist.traverse()

    # 测试头插
    print("测试头插")
    my_linklist.add(20)
    my_linklist.traverse()

    # 测试尾插
    print("测试尾插")
    my_linklist.append(30)
    my_linklist.traverse()

    # 测试任意位置插入
    print("测试任意位置插入")
    my_linklist.insert(-1, 2)
    my_linklist.insert(8, 55)
    my_linklist.insert(2, 32)
    my_linklist.traverse()

    # 测试删除元素
    print("测试删除元素")
    my_linklist.remove(55)
    my_linklist.traverse()

    # 测试查询元素
    print("测试查询元素")
    print(my_linklist.search(55))
    print(my_linklist.search(32))
