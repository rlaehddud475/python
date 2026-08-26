a = "20230331Rainy"
date = a[:8]
weather = a[8:]
year = a[:4]
print(year)
print(date)
print(weather)

print("I eat %d apples." % 3)
print("I eat %s apples." % "five")
number = 3
print("I eat %d apples." % number)
number = 10
day = "three"
print("I ate %d apples. so I was sick for %s days." % (number, day))

print("I have %s apples" % 3)
print("rate is %s" % 3.234)

print("{0:=^10}".format("hi"))
print("{0:!<10}".format("hi"))