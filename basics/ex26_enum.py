from enum import Enum, auto

class Skill(Enum):
    HTML = 1
    CSS = 2
    JS = 3
    Python = auto()

print(Skill.HTML.value, Skill.HTML.name)
print(Skill.Python.value, Skill.Python.name)
