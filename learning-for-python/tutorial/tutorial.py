class MyClass:
    def __init__(self, name, car=None):
        self.name = name
        self.car = car # 인스턴스 변수
    
    def say_hello(self):
        print(f"Hello, {self.name}!")

    def get_name(self):
        return self.name

# 인스턴스 생성
my_instance = MyClass("John")

# 메서드 호출
my_instance.say_hello()  # 출력: Hello, John!

my_instance.get_name()  # 출력: 'John'