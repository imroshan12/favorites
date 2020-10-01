def gcd(a1, b1):
    if a1 < b1:
        a1, b1 = b1, a1
    if a1 % b1 == 0:
        return b1
    else:
        return a1%b1

def numberOfFactors(x):
    result = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            result += 1
            if x // i != i:
                result += 1
        i += 1
    return result
