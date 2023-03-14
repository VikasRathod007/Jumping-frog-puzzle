def swap(x, y):
    x, y = y, x
    return x, y


def iseven(n):
    if n % 2 == 0:
        return True
    else:
        return False


def array(n):
    r = ["R"] * n
    b = ["B"] * n
    s = ["_"]
    arr = b + s + r
    return arr


def move(n):
    return (n + 1) * (n + 1) - 1


def part1(arr, n):

    arr[n], arr[n - 1] = swap(arr[n], arr[n - 1])  # hardcodded 1st move
    print(arr)
    print()
    c1 = n + 1  # counter odd
    odd_counter = 0
    even_counter = 0
    c2 = n  # counter for even
    for i in range(2, n + 1):  # main for loop
        if iseven(i) == True:  # condition for 1st step
            for j in range(0, i):  # inner for loop
                if j == i - 1:
                    c1 -= 2
                    arr[c1 + 1], arr[c1] = swap(arr[c1 + 1], arr[c1])
                    print(arr)
                    print()

                else:

                    if j == 0 and i > 2:
                        if i > 4:
                            odd_counter += 2

                        c1 = c1 - (i - 2) - odd_counter

                    arr[c1], arr[c1 - 2] = swap(arr[c1], arr[c1 - 2])
                    print(arr)
                    c1 += 2

        else:  # for odd
            for j in range(0, i):  # inner for loop
                if j == i - 1:
                    c2 += 2
                    arr[c2 - 1], arr[c2] = swap(arr[c2 - 1], arr[c2])
                    print(arr)

                    print()

                else:

                    if j == 0 and i > 3:
                        if i > 5:
                            even_counter += 4
                        c2 += 4 + even_counter

                    arr[c2], arr[c2 + 2] = swap(arr[c2], arr[c2 + 2])
                    print(arr)
                    c2 -= 2


def part2(arr, n):

    if iseven(n) == True:
        for i in range(len(arr) - 1, 0, -2):
            arr[i], arr[i - 2] = swap(arr[i], arr[i - 2])
            print(arr)
        print()
    else:
        for i in range(0, len(arr) - 1, 2):
            arr[i], arr[i + 2] = swap(arr[i], arr[i + 2])
            print(arr)
        print()

def part3(arr, n):
    c1 = 0  # Even
    c2 = len(arr) - 2  # Odd
    even_counter = 0
    odd_counter = len(arr) - 2
    var1 = 0
    var2 = 0
    if iseven(n) == True:

        for i in range(n, 0, -1):
            if iseven(i) == True:
                if i < n:
                    even_counter += 2
                    # print("Even",even_counter)
                    c1 = even_counter

                for j in range(0, i - 1):
                    if j == 0:
                        arr[c1], arr[c1 + 1] = swap(arr[c1], arr[c1 + 1])
                        print(arr)
                        c1 += 1
                        # print(c1)
                    arr[c1 + 2], arr[c1] = swap(arr[c1 + 2], arr[c1])
                    print(arr)
                    c1 += 2
                    # print(c1)

                print()
            else:
                if i < n - 1:
                    odd_counter -= 2
                    # print("odd",odd_counter)
                    c2 = odd_counter
                for j in range(0, i - 1):
                    if j == 0:
                        arr[c2 - 1], arr[c2] = swap(arr[c2 - 1], arr[c2])
                        print(arr)
                        c2 -= 1
                        # print(c2)
                    arr[c2 - 2], arr[c2] = swap(arr[c2 - 2], arr[c2])
                    c2 -= 2
                    print(arr)
                    # print(c2)
                print()
        arr[n], arr[n + 1] = swap(arr[n], arr[n + 1])
        print(arr)
    else:
        ev_co=2
        od_co=len(arr)-1
        c3 = 2
        c4 = len(arr) - 1
        o_co = 1
        e_co = len(arr) - 1
        for i in range(n, 0, -1):
            if iseven(i) == True:
                
                if i<n-2:
                    ev_co+=2
                    c3=ev_co
                for j in range(1, i, +1):
                    #print(j)
                    if j == 1:
                        # print(j)
                        arr[c3], arr[c3 - 1] = swap(arr[c3], arr[c3 - 1])

                        #print("c3",c3)
                        print(arr)
                        # c3 += 1
                    arr[c3], arr[c3 + 2] = swap(arr[c3], arr[c3 + 2])
                    print(arr)
                    c3 += 2
                    
                print()
            else:

                #print(i)
                if i<n-1:
                    od_co-=2
                    c4=od_co
                for j in range(1, i, +1):
                    #print(j)
                    
                    if j == 1:

                        arr[c4], arr[c4 - 1] = swap(arr[c4], arr[c4 - 1])
                        
                        #print("c4",c4)
                        print(arr)
                        c4 -= 1
                    arr[c4], arr[c4 - 2] = swap(arr[c4], arr[c4 - 2])
                    #print(c4)
                    print(arr)
                    c4 -= 2
                print()
            if i==0 or i==1:
                arr[n],arr[n+1]=swap(arr[n],arr[n+1])
                print(arr)

def moves(arr, n):
    part1(arr, n)
    part2(arr, n)
    part3(arr, n)
    print(f"To moves {n} no of frogs it will take {move(n)} moves")


n = int(input("Enter numbers of frogs:"))

arr = array(n)
print(arr)
print("")
moves(arr, n)
