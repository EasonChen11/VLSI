ans = []
m1,m2=input("Enter the mismatch percentage: ").split()
Mismatch=[float(m1),float(m2)]
with open("and2_tt.txt","r") as f:
    clock=0
    for line in f:
        if clock==1:
            clock=0
            continue
        width,trise,tfall,mismatch=line.split()
        mm=float(mismatch)
        if mm>=Mismatch[0] and mm<=Mismatch[1]:
            ans.append((width,mismatch))
        clock=1
with open("ans.txt","w") as f:
    for i in ans:
        f.write(i[0]+"\t"+i[1]+"\n")