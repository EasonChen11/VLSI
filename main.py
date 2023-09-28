m1,m2=input("Enter the mismatch percentage: ").split()
Mismatch=[float(m1),float(m2)]
def readfile(filename):
    ans = []
    with open(filename,"r") as f:
        clock=0
        for line in f:
            if clock==1:
                clock=0
                continue
            width,trise,tfall,mismatch=line.split()
            mm=float(mismatch)
            if Mismatch[0]<=mm<=Mismatch[1]:
                ans.append((width,mismatch))
            clock=1
    return ans


def compare(param, param1, param2):
    ans=[]
    for i in param:
        for j in param1:
            for k in param2:
                if i[0]==j[0]==k[0]:
                    ans.append((i[0],i[1],j[1],k[1]))
    return ans

x=compare(readfile("and2_mt0.txt"),readfile("and2_mt1.txt"),readfile("and2_mt2.txt"))
print(x)
with open("ans.txt","w") as F:
    for i in compare(readfile("and2_mt0.txt"),readfile("and2_mt1.txt"),readfile("and2_mt2.txt")):
        F.write(i[0]+"\t"+i[1]+"\t"+i[2]+"\t"+i[3]+ "\n")