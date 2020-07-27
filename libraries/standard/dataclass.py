from dataclasses import dataclass
from datetime import date


@dataclass
class User:
    id: int
    name: str
    birthdate: date
    admin: bool = False

    @property
    def get_name(self):
        return self.name


user1 = User(id=1, name="Steve Jobs", birthdate=date(1955, 2, 24))
user1.name = "Ben"
print(user1)
print(user1.get_name)
