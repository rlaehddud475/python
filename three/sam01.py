money = True
if money:
    print("택시를 타고 가라")
else:
    print("걸어 가라")

# money = True
# if money:
#     print("택시를")
# print("타고")
#     print("가라")
# money = True
# if money:
#     print("택시를")
#     print("타고")
#         print("가라")
x = 3
y = 2
print(x > y)
money = 2000
if money >= 3000:
    print("택시를 타고 가라")
else:
    print("걸어가라")
money = 2000
card = True
if money >= 3000 or card:
    print("택시를 타고 가라")
else:
    print("걸어가라")

pocket = ['paper', 'cellphone', 'money']
if 'money' in pocket:
    print("택시를 타고 가라")
else:
    print("걸어라")

pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket:
    pass
else:
    print("카드를 꺼내라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어가라")

pocket = ['paper', 'cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라")
elif card:
    print("택시를 타고가라")
else:
    print("걸어가라")

    pocket = ['paper', 'money', 'cellphone']
if 'money' in pocket: pass
else: print("카드를 꺼내라")

grade = 'B'
match grade:
    case 'A':
        print("탁월한 성적입니다.")
    case 'B':
        print("우수한 성적입니다.")
    case 'C':
        print("보통입니다.")
    case _:
        print("노력이 필요합니다.")

grade = "B"
match grade:
    case "A" | "B" | "C":
        print("합격입니다.")
    case _:
        print("불합격입니다.")

score = 85
result = "합격" if score >= 60 else "불합격"
print(result)

age = 19
status = "성인" if age >= 18 else "미성년"
print(status)

temperature = 25
weather = "따뜻함" if temperature > 20 else "추움"
print(weather)

money = 1500
transportation = "버스" if money >= 1000 else "도보"
print(transportation)
age =int(input("나이를 입력하세요: "))
time=int(input("시간을 입력하세요: "))
if age<7:
     price = 0
elif age>7 and 18>age:
     price = 5000
elif age>=19:
    price = 10000
    if time>18:
        price = int(price * 0.7)

print(f"{int(price)}원")