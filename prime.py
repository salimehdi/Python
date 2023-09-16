def prime (a):
    for i in range(2,a):
        if (a % i == 0):
            return False

    return True
num = int(input())
print(prime(num))
