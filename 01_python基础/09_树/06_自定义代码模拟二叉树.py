# 定义Node类，表示二叉树节点
class Node:
    # 初始化属性
    def __init__(self, item):
        self.item = item
        self.lchild = None
        self.rchild = None

# 自定义BinaryTree  ， 表示二叉树
class BinaryTree:
    def __init__(self, node = None):
        self.root = node

    # 定义add函数，表示添加节点
    def add(self, item):
        # 1.item 封装为节点
        new_node = Node(item)
        # 2.判断根节点是否为None,如果为空，设置当前节点为根节点
        if self.root is None:
            self.root = new_node
            return
        # 3.创建一个队列，添加根节点到队伍中
        queue = []
        queue.append(self.root)
        # 4.通过while True 死循环  找到空缺的节点位置
        while True:
            # 5.获取队列的第一个元素，并从队列中取出
            node = queue.pop(0)
            # 6.判断当前节点左子树是否为空
            if node.lchild is None:
                # 6.1把新结点当作当前节点的左子树，并结束
                node.lchild = new_node
                return
            else:
                # 6.2 走到此处，说明左子树不为空，把当前节点的左子树添加到队列中
                queue.append(node.lchild)
            # 7.判断当前节点的右子树是否为空
            if node.rchild is None:
                # 7.1把新节点设置为当前节点的右子树，并结束
                node.rchild = new_node
                return
            else:
                # 走到此处，说明右子树不为空，把当前节点的右子树，添加到队列中
                queue.append(node.rchild)


    # 定义遍历二叉树 -----  广度优先遍历
    #   广度优先遍历：逐层遍历，一层一层的遍历
    #    例如：先根节点，再根节点的左节点，再根节点的右节点
    #                 再根节点的左节点的左节点、再根节点的左节点的右节点
    #                 再根节点的右节点的左节点、再根节点的右节点的右节点
    #                 。。。。。。。。。。。。。
    def breadth(self):
        # 1.判断根节点是否为空
        if self.root is None:
            return

        # 2.创建队列
        queue = []
        queue.append(self.root)

        # 3.循环打印内容
        while len(queue) != 0:
            # 4.获取第一个元素
            node = queue.pop(0)
            # 5.打印该节点的元素域
            print(node.item, end="\t")

            # 6.判断当前节点的左子树是否存在，存在则添加到队列中
            if node.lchild is not None:
                queue.append(node.lchild)

            # 7.判断当前节点的右子树是否存在，存在则添加到队列中
            if node.rchild is not None:
                queue.append(node.rchild)


    # 深度优先之先序遍历（先根、再左、最后右）
    def perorder(self, root):
        # 1.判断根节点是否不为空，不为空才打印
        if root is not None:
            print(root.item, end="\t")
            # 递归遍历左子树
            self.perorder(root.lchild)
            # 递归遍历右子树
            self.perorder(root.rchild)


    # 深度遍历之中序遍历（先左、再根、最后右）
    def inorder(self, root):
        # 1.判断根节点是否不为空，不为空才打印
        if root is not None:
            # 递归遍历左子树
            self.inorder(root.lchild)
            print(root.item, end="\t")
            # 递归遍历右子树
            self.inorder(root.rchild)


    # 深度遍历之中序遍历（先左、再右、最后根）
    def postorder(self, root):
        # 1.判断根节点是否不为空，不为空才打印
        if root is not None:
            # 递归遍历左子树
            self.postorder(root.lchild)
            # 递归遍历右子树
            self.postorder(root.rchild)
            print(root.item, end="\t")


def dm1_1_测试节点和二叉树类():
    # 1 - 创建节点
    node1 = Node("A")

    # 打印节点的元素域   左子树   右子树
    print(node1.item)
    print(node1.lchild)
    print(node1.rchile)

    print("测试空树")
    # 创建了一个空树
    bt = BinaryTree()
    print(bt.root)

    print("测试二叉树类")
    bt = BinaryTree(node1)
    print(bt.root)
    print(bt.root.item)

def dm2_2_测试广度优先遍历():
    bt = BinaryTree()
    bt.add("张三")
    bt.add("李四")
    bt.add("王五")
    bt.add("赵六")
    bt.add("钱七")

    bt.breadth()

def dm4_4_测试深度优先_先序遍历节点():
    bt = BinaryTree()
    bt.add("A")
    bt.add("B")
    bt.add("C")
    bt.add("D")
    bt.add("E")
    bt.add("F")
    bt.add("G")
    bt.add("H")
    bt.add("I")
    bt.add("J")

    bt.perorder(bt.root)

if __name__ == '__main__':

    # dm1_1_测试节点和二叉树类()
    # dm4_4_测试深度优先_先序遍历节点()
    bt = BinaryTree()
    bt.add("A")
    bt.add("B")
    bt.add("C")
    bt.add("D")
    bt.add("E")
    bt.add("F")
    bt.add("G")
    bt.add("H")
    bt.add("I")
    bt.add("J")

    print("中序遍历：根左右")
    bt.perorder(bt.root)
    print()
    print("中序遍历：左根右")
    bt.inorder(bt.root)
    print()
    print("后序遍历：左右根")
    bt.postorder(bt.root)







