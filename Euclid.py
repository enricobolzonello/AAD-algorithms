def Euclid(a,b):
    if b==0:
        return a
    return Euclid(b, a%b)

if __name__ == "__main__":
    print(Euclid(210, 45))