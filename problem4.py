def numberToStringList(n):
    return list(str(n))

def isPalindrome(p):
    numberList = numberToStringList(p)
    begin = 0
    end = len(numberList) - 1
    while end > begin:
        if not(numberList[begin] == numberList[end]):
            return False
        end = end - 1
        begin = begin + 1
    return True 

def calculate():
    maxPalindrome = 0;
    for i in range(100, 1000):
        for j in range(i, 1000):
            if (isPalindrome(i*j) and i*j > maxPalindrome):
                maxPalindrome = i*j;
    return maxPalindrome;

print calculate();