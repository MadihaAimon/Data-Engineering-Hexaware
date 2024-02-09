def while_loop():
    i = 1
    while i < 6:
        print(i)
        if i == 3:
            break
    i += 1


# pattern
def for_loop(n):
    for i in range(0, n):

        for j in range(0, i + 1):
            print("* ", end="")

        # ending line after each row
        print("\r")


# break
def break_loop():
    for i in range(5):
        if i == 3:
            break
        print(i)


# continue
def continue_loop():
    for i in range(5):
        if i == 3:
            continue
        print(i)


# lambda
def lambda_function():
    ans = lambda i: i + 10
    print(ans(5))


# string
def string_python():
    a = " Hello, World! "
    print(len(a))
    print(a.upper())
    print(a.lower())
    print(a.title())
    print(a.capitalize())
    print(a.count("H"))
    print(a.find("W"))



n = 5
for_loop(n)
while_loop()
break_loop()
continue_loop()