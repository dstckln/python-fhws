import math

def pq(p, q):
    x1 = -p/2 + math.sqrt(math.pow(p/2,2) - q)
    x2 = -p/2 - math.sqrt(math.pow(p/2,2) - q)
    print(x1)
    print(x2)

if __name__ == "__main__":
    p = float(input("p: "))
    q = float(input("q: "))
    pq(p,q)
