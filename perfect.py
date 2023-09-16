def checkPerfect (a):
    per = 0
    for i in range(1,a):
        if (a%i == 0 ):
           per+=i
    if (per == a):
        return True
    else :
        return False


        
print ("Enter a number :")
num = int(input())
print(checkPerfect(num))


