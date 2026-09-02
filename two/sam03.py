dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}

print(dic)
a = {1: 'hi'}

a = {'a': [1, 2, 3]}

a = {1: 'a'}
a[2] = 'b'
print(a)

a['name'] = 'pey'
print(a)
a[3] = [1, 2, 3]
print(a)
del a[1]
print(a)

sports = {"김연아": "피겨스케이팅", "류현진": "야구", "손흥민": "축구", "귀도": "파이썬"}
print(sports)

grade = {'pey': 10, 'julliet': 99}
print(grade['pey'])
print(grade['julliet'])
a = {1: 'a', 2: 'b'}
print(a[1])
print(a[2])

a = {'a': 1, 'b': 2}
print(a['a'])
print(a['b'])
dic = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(dic['name'])
print(dic['phone'])
print(dic['birth'])

a = {1: 'a', 1: 'b'}
print(a)
'''
a = {[1, 2] : 'hi'}
'''

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.keys())
for k in a.keys():
    print(k)

print(list(a.keys()))

print(a.values())
print(a.items())

a.clear()
print(a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('name'))
print(a.get('phone'))

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
print(a.get('nokey'))

'''
print(a['nokey'])  # 에러 발생: KeyError: 'nokey'
'''

print(a.get('nokey', '정보없음'))

print('name' in a)
print('email' in a)

a = {'name': 'pey', 'phone': '010-9999-1234', 'birth': '1118'}
phone = a.pop('phone')
print(phone)
print(a)

email = a.pop('email', '정보없음')
print(email)