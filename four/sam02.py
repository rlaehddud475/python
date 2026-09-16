a = input()
a

number = input("숫자를 입력하세요: ")

number = input("숫자를 입력하세요: ")
print(number)
type(number)

a = input()
b = input()
a + b

age = input("나이를 입력하세요: ")
age = int(age)
print(age + 1)

height = input("키를 입력하세요(cm): ")
height = float(height)
print(height / 100)

age = int(input("나이를 입력하세요: "))
print(type(age))
a = 123
print(a)
a = "Python"
print(a)
a = [1, 2, 3]
print(a)

print("life" "is" "too short")
print("life"+"is"+"too short")

print("life", "is", "too short")

print("2025", "08", "17", sep="-")
print("점프", "투", "파이썬", sep=" TO ")

for i in range(10):
    print(i, end=' ')

print("=== 간단한 계산기 ===")

num1 = float(input("첫 번째 숫자를 입력하세요: "))
num2 = float(input("두 번째 숫자를 입력하세요: "))

print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("0으로 나눌 수 없습니다.")