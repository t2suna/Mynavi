S = input()
s = list(S)
o_count,x_count,E_count = 0,0,0
for i in s:
    if(i == "o"):
        o_count += 1
    if(i == "x"):
        x_count += 1
    if(i == "?"):
        E_count += 1

if(o_count > 4 or x_count == 10):
    print(0)
elif(o_count == 4):
    print(4*3*2)
elif(o_count == 3):
    print(4*3*(2*(E_count)+3))
elif(o_count == 2):
    print((2 + E_count)**4 - ((1 + E_count)**4*2 - (E_count)**4 ))
elif(o_count == 1):
    print((1 + E_count)**4 - (E_count)**4)
elif(o_count == 0):
    print((E_count)**4)