a = True
b = False

print(type(a))
print(type(b))

print(1 == 1)
print(2 > 1)
print(2 < 1)

a = [1, 2, 3, 4]
while a:
    print(a.pop())

if []:
    print("참")
else:
    print("거짓")

if [1, 2, 3]:
    print("참")
else:
    print("거짓")


print(bool('python'))
print(bool(''))
print(bool([1, 2, 3]))
print(bool([]))
print(bool(0))
print(bool(3))

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print(not True)
print(not False)
print(not 1)
print(not 0)

x = 5
y = 10
print(x > 0 and y > 0)
print(x > 10 or y > 5)
print(not (x > y))