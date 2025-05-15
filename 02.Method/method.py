class Myclass():
    def method(self):
        return 'instance method called', self
    
    @classmethod
    def classmethod(cls):
        return 'class method called', cls
    
    @staticmethod
    def staticmethod():
        return 'static method called'

# ref : https://realpython.com/instance-class-and-static-methods-demystified/

# Dynamacally adding method and attribute to class


def __init__(self, name, color):
    self.name = name
    self.color = color

Myclass.__init__ = __init__

print(Myclass.__dict__)