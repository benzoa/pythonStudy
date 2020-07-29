from dataclasses import dataclass
from datetime import date

@dataclass
class User:
    id: int
    name: str
    birthdate: date
    admin: bool = False
    __age: int = 0

    @property
    def get_name(self):
        return self.name

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, val):
        self.__age = val


user1 = User(id=1, name="Steve Jobs", birthdate=date(1955, 2, 24))
print(user1)
user1.name = "Ben"
print(user1.get_name)

user1.age = 21
print(user1.age)
