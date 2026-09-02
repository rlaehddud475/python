a = 1
b = "python"
c = [1, 2, 3]

print(a)
print(b)
print(c)

# 올바른 변수명 예시
name = "홍길동"
age = 25
user_name = "gildong"
userName = "gildong"  # 카멜 케이스
_private = "비공개"
count1 = 10

# 잘못된 변수명 예시
# 1name = "홍길동"  # 숫자로 시작 (오류)
# user-name = "홍길동"  # 하이픈 사용 (오류)
# if = 10  # 예약어 사용 (오류)

print(name)
print(age)
print(user_name)
print(userName)
print(_private)
print(count1)

# 좋은 예
student_name = "김철수"
total_score = 95
user_age = 20

# 피해야 할 예
# a = "김철수"  # 의미 불명확
# studentNameFromKorea = "김철수"  # 너무 긴 이름

print(student_name)
print(total_score)
print(user_age)

a = [1, 2, 3]
print(id(a))

a = [1, 2, 3]
b = a

print(id(a))
print(id(b))

print(a is b)

a[1] = 4
print(a)
print(b)

a = [1, 2, 3]
b = a[:]
a[1] = 4
print(a)
print(b)

from copy import copy

a = [1, 2, 3]
b = copy(a)
print(b is a)

# 리스트 자료형의 자체 함수인 copy 함수 사용하기
a = [1, 2, 3]
b = a.copy()
print(b is a)

a, b = ('python', 'life')
print(a)
print(b)

(a, b) = 'python', 'life'
print(a)
print(b)

[a, b] = ['python', 'life']
print(a)
print(b)

a = b = 'python'
print(a)
print(b)

a = 3
b = 5
a, b = b, a
print(a)
print(b)