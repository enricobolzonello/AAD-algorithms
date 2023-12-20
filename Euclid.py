import math

def Euclid(a,b):
    if b==0:
        return a
    return Euclid(b, a%b)

def ExtendedEuclid(a,b):
    if b==0:
	    return (a, (1,0))
    temp = ExtendedEuclid(b,a%b)
    x = temp[1][0]
    y = temp[1][1]
    return (temp[0], (y, x - math.floor(a/b)*y))

if __name__ == "__main__":
    print(Euclid(210, 45))
    print(ExtendedEuclid(24, 16))