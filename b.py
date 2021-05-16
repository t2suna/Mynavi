N = int(input())
i = 0
S_A = ""
T_A = 0
T_A2 = -1
while(i<N):
    Temp = input()
    S,T = Temp.split()[0],int(Temp.split()[1])
    i+=1
    if(T>T_A):
        S_A2 = S_A
        T_A2 = T_A
        S_A = S
        T_A = T

    elif(T>T_A2):
        S_A2 = S
        T_A2 = T

print(S_A2)