'''Lambda'''
add10 = lambda x: x + 10
print(add10(3))


a = [1, 4, 5, 10]
b = map(lambda x: x * 2, a)
print(list(b))

'''Added another Lambda'''

mult = lambda x, y: x * y
print(mult(4, 5))