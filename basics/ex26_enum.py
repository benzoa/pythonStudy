from enum import Enum, auto

class Skill(Enum):
    HTML = 1
    CSS = 2
    JS = 3
    Python = auto()

print(Skill.HTML.value, Skill.HTML.name)
print(Skill.Python.value, Skill.Python.name)

Skill = Enum("Skill", "HTML CSS JS")
print(list(Skill))

class StrEnum(str, Enum):
    def _generate_next_value_(name, start, count, last_values):
        return name

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class MySkill(StrEnum):
    HTML = auto()
    CSS = auto()
    JS = auto()

print(MySkill.HTML == "HTML")
print(isinstance(MySkill.HTML, str))
