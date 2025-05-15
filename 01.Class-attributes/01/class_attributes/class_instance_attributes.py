class Myclass():
    counter = 0

    def __init__(self, value):
        self.value = value
        Myclass.counter += 1
    
    def set_value(self, new_value):
        self.value = new_value
    
    def get_value(self):
        return self.value
    
    def get_counter(self):
        return Myclass.counter

class1 = Myclass(10)
# print(class1.get_value())  # 10
# print(class1.get_counter())  # 1
class2 = Myclass(20)
# print(class2.get_value())  # 20
# print(class2.get_counter())  # 2