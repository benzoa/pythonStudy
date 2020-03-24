class Person:
    # initializer 
    # type1
    '''
    def __init__(self, name, money):
        self.name = name

        # private attribute
        self.__wallet = money
    ''' 
    '''
    # type2
    def __init__(self, *args):
        self.name = args[0]
        self.__wallet = args[1]
    
    '''
    # type3
    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.__wallet = kwargs['money']

    def add_attr(self):
        self.new = "added"
    
    # private(special/magic) method
    def __add_money(self, money):
        self.__wallet += money
        print("total money: {}".format(self.__wallet))
    
    def disp_stat(self):
        print("name: {}, money: {}".format(self.name, self.__wallet))
    
    def spend_money(self, what, amount):
        if self.__wallet < amount:
            print("not enough money!")
            return
        
        self.__wallet -= amount
        print("spend: {}({}), now: {}".format(what, amount, self.__wallet))
    
    def save_money(self, amount):
        self.__wallet += amount
        print("save: {}, now: {}".format(amount, self.__wallet))
    
    def __del__(self):
        print("Done!")
    
    # __slot__ = ['weight', 'height', 'addr']

# p = Person("Ben", 100)  # type1
# p = Person(*['Ben', 100])  # type2
p = Person(**{'name': 'Ben', 'money': 100})  # type3
p.disp_stat()
p.save_money(2200)
p.spend_money("Shopping", 1800)

# add attributes to instance at runtime
p.addr = "76 W 35th St, New York"
p.weight = 70

p.__class__.name = "Kevin"
print("isinstance(p, Person): {}".format(isinstance(p, Person)))
print("=" * 40)
print(p.__dict__)
print("=" * 40)
print(Person.__dict__)
print("=" * 40)
