
#Anzahl permutationen von rrrrrrrrrruuuuuuuuuu
#n!/k1!k2!...kn!

def fac(n):
    if n == 1:
        return 1
    return n * fac(n-1)

def solve(n):
    return fac(2 * n)/(fac(n)*fac(n))

print solve(2)
print solve(20)