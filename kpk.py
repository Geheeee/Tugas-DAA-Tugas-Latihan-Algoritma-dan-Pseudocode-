def gcd(a, b):
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

a = 3
b = 4
lcm_value = lcm(a, b)
print("KPK dari", a, "dan", b, "adalah", lcm_value)
