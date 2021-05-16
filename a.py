
a1,a2,a3 = map(int,input().split())
if((a3-a2) == (a2-a1)):
    print("Yes")
elif((a2-a1) == (a1-a3)):
    print("Yes")
elif((a1-a3) == (a3-a2)):
    print("Yes")
else:
    print("No")