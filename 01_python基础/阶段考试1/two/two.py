"""
    1、手动在当前项目根目录下创建singer.txt文件，
        内容如下：
            沉默是金，张国荣
            少女的祈祷，杨千嬅
            暗里着迷，刘德华
            难念的经，周华健（内容见附件）
    2、定义一个singer类(歌手类)，包含初始化init方法：
        成员属性: 歌曲名 歌手名字
        成员方法：fans()：打印“XXX歌手的YYY歌曲持续打榜，粉丝为喜欢的歌手打call” XXX为对象的歌手名字，YYY为对象的歌曲名。

    3、在歌手类外面完成以下功能：
        1）通过程序逐行读取singer.txt文件内容，
            根据每行数据创建对应歌手对象并赋值，依次将歌手对象存入列表。
        2）遍历列表，获取元素并调用对象的fans方法
"""
class Singer:
    def __init__(self,gequ_name = "",singer_name = ""):
        self.gequ_name = gequ_name
        self.singer_name = singer_name

    def fans(self):
        print(f"{self.singer_name}歌手的{self.gequ_name}歌曲持续打榜，粉丝为喜欢的歌手打call")

def read_file():
    singers = []
    with open("./singer.txt", "r", encoding="utf-8") as src_f:

        # for i in range(4):
        #     data = src_f.readline()
        #     gequ_name, singer_name = data.split("，")
        #
        #     singer = Singer()
        #     singer.gequ_name = gequ_name
        #     singer.singer_name = singer_name.strip()
        #
        #     singers.append(singer)

        while True:
            data = src_f.readline()
            # if data == "":
            if len(data) == 0:
                break
            gequ_name, singer_name = data.split("，")

            singer = Singer()
            singer.gequ_name = gequ_name
            singer.singer_name = singer_name.strip()

            singers.append(singer)

    return singers
def bianli(singers):
    for singer in singers:
        singer.fans()



if __name__ == '__main__':
    singers = read_file()
    bianli(singers)


