class Robot:
    ''' Robot Class '''     # Robot.__doc__

    # class attribute
    population = 0
    __total_price = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Robot.population += 1
        Robot.__total_price += price
        print("name: {}, price: {}".format(name, price))
    
    def say_hi(self):
        ''' say hi method '''   # Robot.say_hi.__doc__ or instance.say_hi.__doc__
        print("Hi! I'm {}".format(self.name))
    
    def die(self):
        Robot.population -= 1
        Robot.__total_price -= self.price

        if Robot.population == 0:
            print("{} was the last one.".format(self.name))

    @staticmethod
    def mul(x, y):
        return x * y

    @classmethod
    def now_stat(cls):
        print("robot: {}".format(cls.population))
        print("total_price: {}".format(cls.__total_price))


ben = Robot("Ben", 100)
ben.say_hi()
Robot.now_stat()
print("staticmethod: {}".format(Robot.mul(11, 22)))
print("=" * 40)

kevin = Robot("Kevin", 150)
kevin.say_hi()
Robot.now_stat()
print("=" * 40)

ben.die()
kevin.die()
Robot.now_stat()
