# string
abc = "ABCDEF"
print("[:]: {}, [::]: {}".format(abc[:], abc[::]))
print("abc[1:4]: {}".format(abc[1:4]))
print("abc[:3]: {}".format(abc[:3]))
print("abc[-2:]: {}".format(abc[-2:]))
print("abc[::2]: {}".format(abc[::2]))
print("=" * 40)

# list
shop_list = ['apple', 'mango', 'carrot', 'banana']
print("shop_list[1:3]: {}".format(shop_list[1:3]))
print("shop_list[:2]: {}".format(shop_list[:2]))
print("shop_list[2:]: {}".format(shop_list[2:]))
print("shop_list[:]: {}".format(shop_list[:]))
print("shop_list[1:-1]: {}".format(shop_list[1:-1]))

print("shop_list[::1]: {}".format(shop_list[::1]))
print("shop_list[::2]: {}".format(shop_list[::2]))
print("shop_list[0::2]: {}".format(shop_list[0::2]))
print("shop_list[::-1]: {}".format(shop_list[::-1]))
print("shop_list[::-2]: {}".format(shop_list[::-2]))
print("shop_list[-3:]: {}".format(shop_list[-3:]))

shop_list[len(shop_list):] = ["onion"]
print(shop_list)

add_items = ["pears", "grape"]
shop_list[len(shop_list):] = add_items
print(shop_list)
print("=" * 40)

# tuple
name_list = 'ben', 'kim', 'john', 'chol'
print("name_list[1:3]: {}".format(name_list[1:3]))
print("name_list[::1]: {}".format(name_list[::1]))
print("name_list[0::2]: {}".format(name_list[0::2]))
print("name_list[::-1]: {}".format(name_list[::-1]))
print("name_list[::-2]: {}".format(name_list[::-2]))
print("name_list[-3::2]: {}".format(name_list[-3::2]))

# slice(start, end, step)
s = slice(3)
print(name_list[s])

# and so on.
tmp = [11, 11]
add_items = list(range(8))
tmp[1:1] = add_items
print(tmp)
print("=" * 40)

cpy = tmp[:]
cpy[2:5] = [10, 20]
print(cpy)
cpy[5:7] = ["Ben", "John", "Kevin"]
print(cpy)

cpy[1:len(cpy):3] = ["Orange", "Apple", "Mango"]
print(cpy)

del cpy[1:-3]
print("del: {}".format(cpy))

search_item = "Mango"

if search_item in cpy:
    print("item: {}, idx: {}".format(search_item, cpy.index(search_item)))

