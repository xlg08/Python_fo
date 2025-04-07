class Animal:
    def speak(self):        # 抽象的方法
        pass

class Dog(Animal):
    def speak(self):
        print("狗叫")

class Cat(Animal):
    def speak(self):
        print("猫叫")

# 因为python是弱类型的语言
#       所以  :Animal 只是指示形参an需要传入Animal类型的对象，所以python是伪多态
def make_noise(an:Animal):
    an.speak()


d = Dog()
# d.speak()
c = Cat()
# c.speak()

make_noise(d)

# 父类引用指向子类对象
# 创建一个父类类型的变量，实际存储的是子类对象
# 但是python是弱类型，因此python是伪多态
an: Animal = Dog()
print(type(an))
an.speak()


