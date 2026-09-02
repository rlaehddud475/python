a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
a[2:5]
a[3][:2]
a = [1, 2, 3]
b = [4, 5, 6]
a + b
len(a)
a[2] = 4
print(a)
str(a[2]) + "hi"
del a[1]
print(a)
a = [1, 2, 3, 4, 5]
del a[2:]
a = [1, 2, 3]
a.append(4)
a.append([5, 6])
print(a)
a = [1, 4, 3, 2]
a.sort()
print(a)
a = ['a', 'c', 'b']
a.reverse()
print(a)
a = [1, 2, 3]
a.index(3)
a.index(1)
a.index(0)
a.insert(0, 4)
a.insert(3, 5)
a = [1, 2, 3, 1, 2, 3]
a.remove(3)
a.remove(3)
a.pop()
a.pop(1)
a = [1, 2, 3, 1]
a.count(1)
 a = [1, 2, 3]
a.extend([4, 5])
b = [6, 7]
a.extend(b)