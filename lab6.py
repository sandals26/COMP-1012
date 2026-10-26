def sumList(theList):
    return sum(theList)
def max(firstNum, secondNum):
    if firstNum > secondNum:
        return firstNum
    else:
        return secondNum
def fib(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        return fib(num-1) + fib(num-2)
    # fib num = num previous + num previous previous
def fibbonaci(num):
    if num == 0:
        return 0
    elif num == 1:
        return 1
    else:
        fibNums = [0,1]
        for i in range(1,num):
            fibNums.append(fibNums[i]+fibNums[i-1])
        return fibNums[num]
fibNum = int(input("Num fib sequence: "))
print(fib(fibNum))
print(fibbonaci(fibNum))