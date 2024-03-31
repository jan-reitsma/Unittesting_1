'''
some methods and classes for testing
'''

def fun1():
    instance = B()
    return instance.method()

def fun2():
    return 10


class B:
    def method(self):
        self.something(1,2,3)

    def something(self, a,b,c):
        pass



class MyClass():
    def __init__(self):
        self.a:int = 1
        self.b:int = 2

    def get_values(self):
        print("haha")
        return [self.a , self.b]


class AnotherClass():
    def fun1(self, n:int):
        self.fun2(n*2)

    def fun2(self, n:int):
        if n == 10:
            print("i am doing something complicated and slow")
        else:
            return


if __name__ == "__main__":

    c = MyClass()
    print(c.get_values())