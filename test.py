'''Lambda'''
add10 = lambda x: x + 10
print(add10(3))


a = [1, 4, 5, 10]
b = map(lambda x: x * 2, a)
print(list(b))

'''Added multiply to  Lambda'''

mult = lambda x, y: x * y
print(mult(4, 5))

'''Added filter to  Lambda'''

y = filter(lambda x: x % 2 == 0, a)
print(list(y))