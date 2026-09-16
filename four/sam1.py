def add(a,b):
    return a + b
a = 3
b = 4
c = add(a, b)
print(c)

def add(a, b):
    return a + b

print(add(3, 4))

def add(a, b):
    result = a + b
    return result

a = add(3, 4)
print(a)

def say():
    return 'Hi'

print(say())

def add(a, b):
    print(f"{a}, {b}의 합은 {a+b}입니다.")

add(3, 4)

a = add(3, 4)
print(a)

def say():
    print('Hi')

say()

def sub(a, b):
    return a - b

result = sub(a=7, b=3)
print(result)

result = sub(b=5, a=3)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result = result + i
    return result

result = add_many(1, 2, 3)
print(result)

result = add_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(result)

def add_mul(choice, *args):
    if choice == "add":
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i
    return result

result = add_mul('add', 1, 2, 3, 4, 5)
print(result)

result = add_mul('mul', 1, 2, 3, 4, 5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

print_kwargs(name='홍길동', age=25, city='서울', job='개발자')

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1)

print_kwargs(name='foo', age=3)

print_kwargs(name='홍길동', age=25, city='서울', job='개발자')

def add_and_mul(a, b):
    return a+b, a*b

result = add_and_mul(3, 4)

result1, result2 = add_and_mul(3, 4)

def add_and_mul(a, b):
    return a+b
    return a*b

result = add_and_mul(2, 3)
print(result)

def add_and_mul(a, b):
    return a+b

def say_nick(nick):
    if nick == "바보":
        return
    print(f"나의 별명은 {nick}입니다.")

say_nick('야호')
say_nick('바보')

def say_myself(name, age, man=True):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)

say_myself("박응용", 27, True)


say_myself("박응선", 27, False)

# default2.py
def say_myself(name, man=True, age):
    print(f"나의 이름은 {name}입니다.")
    print(f"나이는 {age}살입니다.")
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("박응용", 27)

a = 1
def vartest(a):
    a = a +1

vartest(a)
print(a)


a = 1
def vartest(a):
    a = a + 1
    return a

a = vartest(a)
print(a)

a = 1
def vartest():
    global a
    a = a + 1

vartest()
print(a)

def change_list(my_list):
    my_list.append(4)

a = [1, 2, 3]
change_list(a)
print(a)

add = lambda a, b: a+b
result = add(3, 4)
print(result)

def add(a, b):
    return a+b

result = add(3, 4)
print(result)

def add(a, b):
    """
    두 숫자를 더하는 함수

    Parameters:
    a (int, float): 첫 번째 숫자
    b (int, float): 두 번째 숫자

    Returns:
    int, float: 두 숫자의 합
    """
    return a + b

print(add.__doc__)