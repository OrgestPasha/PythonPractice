print(3 > 2 > 1)
print(3 > 2 == 1)

lst = [1] * 3
lst.append(1)

print(lst)
b = 256
a = b
print(a is b)

c = [1, 2]
d = [1, 2]
print(c is d)

print(True + True * False)

print(0 or [] or "hello" or 5)

lst = [1, 2, 3, 4]
for i in lst:
    if i % 2 == 0:
        lst.remove(i)

print(lst)
print(1, 3)


def f():
    try:
        return 1
    finally:
        return 2


print(f())

x = [1, 2, 3]
y = x

x += [4, 5]
y = y + [6, 7]

print(x)
print(y)

print(0 == False)
print([] is False)

a = 1000
b = 1000

print(a is b)
print(a == b)

print("hello"[::-1])
print("hello"[::-2])

x = [0, 1, 2, 3, 4]
for i in x:
    print("Element deleted is " + str(i))
    x.remove(i)
    print(x)
print(x)
