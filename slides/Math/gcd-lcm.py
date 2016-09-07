import fractions
print(fractions.gcd(20,8))

def lcm(a,b):
    return b*a/fractions.gcd(b,a)
print(lcm(20,8))
