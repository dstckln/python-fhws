import math

def main():
    r = 5
    print("kreisflaeche: " + str(math.pi * math.pow(r, 2)))
    print("kreisumfang: " + str(2 * math.pi * r))

    print("kugelvolumen: " + str(4/3 * math.pi * math.pow(r, 3)))

if __name__ == "__main__":
    main()         
    
