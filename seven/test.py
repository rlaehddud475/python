#단 크기
width=14
#전체 크기
total=width*8
# total에 값에서 3을뺸걸 기준으로 가운데정렬하고 = 으로 채움 center(전체크기, 채울문자)
print("구구단".center(total - 3, "="))
print()
for i in range(2, 10):
    #단별로 위에 가운데 정렬하게 하는것(이것은 단별로 크기가 나누기때문에 width-1로 전체 크기를 설정함)
    title = f"={i}단="
    print(title.center(width-1), end="")
print()
for j in range(1, 10):
    for i in range(2, 10):
      #단별로 곱셈 식 과 결과를 출력하는데, 결과값을 2자리로 맞추고 가운데 정렬함
      result=f"{i} * {j} = {i * j:2d}"
      print(result.center(width), end="")
    print()