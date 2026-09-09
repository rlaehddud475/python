while True:
    n=int(input("n 입력: "))
    for i in range(1, n+1):
        if i%3==0 and i%5==0:
            print("3과 5의 공배수")
        elif i%3==0:
            print("3의 배수")
        elif i%5==0:
            print("5의 배수")
        else:
            print(i)

    cont=input("계속하시겠습니까? (y/n): ")
    if cont == 'n':
        print("프로그램을 종료합니다.")
        break