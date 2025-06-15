# SOLID Principles
# S - Single Responsibility Principle
# O - Open/Closed Principle
# L - Liskov Substitution Principle
# I - Interface Segregation Principle
# D - Dependency Inversion Principle

# Single Responsibility Principle
""" A class should have one and only one reason to change, meaning that a class should have only one job or responsibility. """

# O - Open/Closed Principle
""" Software entities (classes, modules, functions, etc.) should be open for extension but closed for modification. """

# L - Liskov Substitution Principle
""" If you have a functions that works with a base class, it should also work with any derived class without knowing the difference. """

# I - Interface Segregation Principle
""" A client should not be forced to depend on methods it does not use. """

# Example of Interface Segregation Principle:

class lightbulb:
    def turn_on(self):
        print("Lightbulb is turned on")
    def turn_off(self):
        print("Lightbulb is turned off")

class switch:
    def __init__(self, bulb: lightbulb):
        self.bulb = bulb

    def operate(self, action: str):
        if action == "on":
            self.bulb.turn_on()
        elif action == "off":
            self.bulb.turn_off()
        else:
            raise ValueError("Invalid action. Use 'on' or 'off'.")

bulb = lightbulb()
switch = switch(bulb)
switch.operate("off")

""" Here switch is directly depend on lightbulb class,
  so if I want to use a different device I need to change switch class,
 so it's tighty coupled.
  which is vilation of Dependency Inversion Principle. """

# With DIP:

from abc import ABC, abstractmethod

class switchableDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    def turn_off(self):
        pass

class lightbulb(switchableDevice):
    def turn_on(self):
        print("Lightbulb is turned on in DIP")
    def turn_off(self):
        print("Lightbulb is turned off in DIP")


class switch:
    def __init__(self, device: switchableDevice):
        self.device = device

    def operate(self, action: str):
        if action == "on":
            self.device.turn_on()
        elif action == "off":
            self.device.turn_off()
        else:
            raise ValueError("Invalid action. Use 'on' or 'off'.")
        

bulb = lightbulb()
siwtch = switch(bulb)
siwtch.operate("off")

""" Now switch class is not directly depend on lightbulb class,
  so if I want to use a different device I don't need to change switch class,
  which is fullfill the Dependency Inversion Principle. """


# Design Patterns:
# Singleton Pattern
""" implentation of Singleton Pattern """
class SingletonMeta(type):
    _instance = {}

    def __call__(cls, *args, **kwds):
        if cls not in cls._instance:
            instance = super().__call__(*args, **kwds)
            cls._instance[cls] = instance
        return cls._instance[cls]

class Singleton(metaclass=SingletonMeta):
    def __init__(self, value):
        self.value = value

# Usgae
instance1 = Singleton(10)
instance2 = Singleton(20)

print(instance1==instance2)  # True, both are the same instance

# Thread-Safe Singleton Pattern
from threading import Lock, Thread
class ThreadSafeSingletonMeta(type):
    __instance = {}
    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        
        with cls._lock:
            if cls not in cls.__instance:
                instance = super().__call__(*args, **kwargs)
                cls.__instance[cls] = instance
        return cls.__instance[cls]
    
class singleton_typesafe(metaclass=ThreadSafeSingletonMeta):
    value: str = None

    def __init__(self, value):
        self.value = value

def test_singleton_typesafe(value: str) -> None:
    singleton_typesafe_ = singleton_typesafe(value)
    print(singleton_typesafe_.value)

# if __name__ == "__main__":
#     process1 = Thread(target=test_singleton_typesafe, args=("Sumanta",))
#     process2 = Thread(target=test_singleton_typesafe, args=("Raj",))
#     process1.start()
#     process2.start()

# Factory Pattern:
""" Simple Notiification service created using Factory Method Design Pattern: """

from abc import ABC, abstractmethod

# step:1 Create the Product Interface
class Notification(ABC):

    @abstractmethod
    def send(self, msg, recipient):
        pass

# step:2 Create the Concrete Product

class EmailNotification(Notification):
    "Concreate implementation of email notification"

    def send(self, msg: str, recipient: str) -> None:
        print(f"Sending Email:  {msg} for {recipient}")

class SmsNotification(Notification):
    "Concrete implementation of email SMS"
    def send(self, msg: str, recipient: str) -> None:
        print(f"Sending Email:  {msg} for {recipient}")


# step:3 Create the abstruct Creator:
class NotificationService(ABC):

    @abstractmethod
    def create_notification(self):
        pass

    def send_notification(self, msg, recipient):
        notification = self.create_notification()
        return notification.send(msg, recipient)

# step:4 Concreate Creator    
class EmailNotificationService(NotificationService):

    def create_notification(self):
        return EmailNotification()
    
class SmsNotificationService(NotificationService):

    def create_notification(self):
        return SmsNotification()
    
if __name__ == "__main__":
    print("Sending Email Notification to google@gmail.com")
    email = EmailNotificationService()
    email.send_notification('All Okay!!', 'google@gmail.com')