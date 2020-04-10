class SchoolMember:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
        print("SchoolMember, {}, {}".format(self.name, self.__salary))

    def tell(self):
        print("{}: {}".format(self.name, self.__salary))


class Teacher(SchoolMember):
    def __init__(self, name, salary, subject):
        super().__init__(name, salary)
        self.subject = subject
        print(" + Teacher: {}".format(self.subject))

    # method overriding
    def tell(self):
        super().tell()
        print(" + subject: {}".format(self.subject))


class Student(SchoolMember):
    def __init__(self, name, salary, marks):
        SchoolMember.__init__(self, name, salary)
        self.marks = marks
        print(" + Student: {}".format(self.marks))

    def tell(self):
        SchoolMember.tell(self)
        print(" + marks: {:d}".format(self.marks))


John = SchoolMember("John", 100)
Ben, Kevin = Teacher("Ben", 200, "CS"), Student("Kevin", 0, 87)
print("=" * 40)

John.tell()
Ben.tell()
Kevin.tell()
print("=" * 40)

print("Student is subclass of SchoolMember:", issubclass(Student, SchoolMember))
print("BaseClass of the Student:", Student.__base__)
print("John is instance of SchoolMember:", isinstance(John, SchoolMember))
print("Ben is instance of SchoolMember:", isinstance(Ben, SchoolMember))
print("Kevin is instance of SchoolMember:", isinstance(Kevin, SchoolMember))
print("=" * 40)

teachers = []
teachers.append(Teacher("Jessi", 150, "Physics"))
teachers.append(Teacher("Jung", 110, "Chemistry"))
teachers.append(Teacher("Bob", 160, "Biology"))
print("=" * 40)

students = []
students.append(Student("Park", 0, 77))
students.append(Student("Lee", 0, 84))
students.append(Student("Han", 0, 63))

members = teachers + students

for i, member in enumerate(members):
    if i == len(teachers):
        print("-" * 30)

    member.tell()

print("=" * 40)

from abc import ABCMeta, abstractmethod

class Person(metaclass=ABCMeta):
    @abstractmethod
    def update_salary(self, new_salary):
        pass

    @abstractmethod
    def say_hi(self):
        pass


class Police(Person):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def update_salary(self, new_salary):
        self.salary = new_salary
        print("Update Salary: {}".format(self.salary))

    def say_hi(self):
        print("Hi! I'm {}.".format(self.name))


james = Police("James", 100)
james.update_salary(200)
james.say_hi()
