def ex1():
    r = float(input("Enter circle radius? "))
    area_circle = 3.14 * r * r
    print("Circle area = " + str(area_circle))

def ex2():
    c = float(input("Enter the temperature in Celsius? "))
    f = (c * 1.8) + 32
    print(str(c) + " (C)=" + str(f) + " (F)")

def ex3():
    n = int(input("Enter a number? "))
    prime = True
    for i in range(2, n): 
        if n % i == 0:
            prime = False
            break
    
    if prime == True:
        print(str(n) + " is a prime number")
    else:
        print(str(n) + " is a NOT prime number")

def ex4():
    num = int(input("Enter a number? "))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    
    if sum == num:
        print(str(num) + " is a perfect number")
    else:
        print(str(num) + " is a NOT perfect number")

def ex5():
    color_list = ["Blue", "Yellow", "Black", "Red", "Green", "White"]
    my_color = input("What is your favorite color? ")
    found = False
    for i in range(len(color_list)):
        if color_list[i] == my_color:
            print("Your colod is at index " + str(i) + " in my list")
            found = True
    
    if found == False:
        print("Sorry, I could not find your color")

def ex6():
    print("range1 | " + str(list(range(7))).replace("[", "").replace("]", ""))
    print("range2 | " + str(list(range(1, 11, 3))).replace("[", "").replace("]", ""))
    print("range3 | " + str(list(range(5, 0, -1))).replace("[", "").replace("]", ""))
    print("range4 | " + str(list(range(6, -3, -2))).replace("[", "").replace("]", ""))

def ex7(s):
    new_str = ""
    for char in s:
        if char != "$":
            new_str = new_str + char
    return new_str

def ex8(I):
    result = []
    for x in I:
        if x % 2 == 0:
            result.append(x)
    return result

def ex9(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def ex10(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def ex11(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return d

def ex12(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end="")
        print()

def ex1():
    r = float(input("Enter circle radius? "))
    area_circle = 3.14 * r * r
    print("Circle area = " + str(area_circle))

def ex2():
    c = float(input("Enter the temperature in Celsius? "))
    f = (c * 1.8) + 32
    print(str(c) + " (C)=" + str(f) + " (F)")

def ex3():
    n = int(input("Enter a number? "))
    prime = True
    for i in range(2, n): 
        if n % i == 0:
            prime = False
            break
    
    if prime == True:
        print(str(n) + " is a prime number")
    else:
        print(str(n) + " is a NOT prime number")

def ex4():
    num = int(input("Enter a number? "))
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum = sum + i
    
    if sum == num:
        print(str(num) + " is a perfect number")
    else:
        print(str(num) + " is a NOT perfect number")

def ex5():
    color_list = ["Blue", "Yellow", "Black", "Red", "Green", "White"]
    my_color = input("What is your favorite color? ")
    found = False
    for i in range(len(color_list)):
        if color_list[i] == my_color:
            print("Your colod is at index " + str(i) + " in my list")
            found = True
    
    if found == False:
        print("Sorry, I could not find your color")

def ex6():
    print("range1 | " + str(list(range(7))).replace("[", "").replace("]", ""))
    print("range2 | " + str(list(range(1, 11, 3))).replace("[", "").replace("]", ""))
    print("range3 | " + str(list(range(5, 0, -1))).replace("[", "").replace("]", ""))
    print("range4 | " + str(list(range(6, -3, -2))).replace("[", "").replace("]", ""))

def ex7(s):
    new_str = ""
    for char in s:
        if char != "$":
            new_str = new_str + char
    return new_str

def ex8(I):
    result = []
    for x in I:
        if x % 2 == 0:
            result.append(x)
    return result

def ex9(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

def ex10(n):
    divs = []
    for i in range(1, n + 1):
        if n % i == 0:
            divs.append(i)
    return divs

def ex11(x1, y1, x2, y2):
    d = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5
    return d

def ex12(m, n):
    for i in range(m):
        for j in range(n):
            print("*", end="")
        print()
ex3()