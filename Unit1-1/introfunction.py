#check for a number in a range
# num = int(input("input a number: "))
def rangecheck(num):  #this is called a function declaration
    min = 0
    max = 100
    for i in range(min, max):
          # print(i)
          # if num in range(0,100):
        if num > min and num < max:
            print(num)
            break
        else:
            print(f"Number {num} not in range {min} and {max}.")
            # exit()
            break


# Once I have declared/created a function, I need to make a FUNCTION CALL
rangecheck(140)
rangecheck(20)
for i in range(51):
    a = i
    b = i * 10
    rangecheck(a)
    rangecheck(b)
    a += i
    b -= i
