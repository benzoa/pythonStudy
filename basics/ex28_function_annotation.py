def func(arg1:str, arg2: 1+2, arg3: 'this is annottion') -> bool:
    print(f'arg1 = {arg1}')
    print(f'arg2 = {arg2}')
    print(f'arg3 = {arg3}')
    return True

ret = func('test1', 3, 'this is test')
print(f'result = {ret}')
