def func(arg1:str, arg2: 1+2, arg3: 'this is annottion') -> bool:
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    return True

ret = func('test1', 3, 'this is test')
print(f'result = {ret}\n')

class AnnotationClassExample:
    first_param: str
    second_param: int

    def set_first_param(self, value: str) -> None:
        self.first_param = value

    def set_second_param(self, value: int) -> bool:
        if type(value) == int:
            self.second_param = value
            return True
        else:
            self.second_param = 0
            return False

def main():
    new_class = AnnotationClassExample()
    print(new_class.__annotations__)
    print(new_class.set_first_param.__annotations__)
    print(new_class.set_second_param.__annotations__)

if __name__ == '__main__':
    main()
