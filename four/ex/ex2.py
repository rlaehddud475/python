def avg_number(*args):
    result = 0
    for i in args:
        result+=i
    return result / len(args)

print(avg_number(1,2))
print(avg_number(1,2,3,4,5))