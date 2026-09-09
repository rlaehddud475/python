num=[]
while True:
    n=int(input("숫자 입력: "))

    if n==0:
        break
    num.append(n)

pos_count=0
neg_count=0
even_count=0
odd_count=0

for i in num:

    if i>0:
        pos_count+=1
    elif i<0:
        neg_count+=1
    if i%2==0:
        even_count+=1
    else:
        odd_count+=1
total=pos_count+neg_count+even_count+odd_count
print(f"양수 개수: {pos_count}개")
print(f"음수 개수: {neg_count}개")
print(f"짝수 개수: {even_count}개")
print(f"홀수 개수: {odd_count}개")
print(f"총합: {total}")