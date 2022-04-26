def vytvor_sachovnicu(r, s):
    sachovnica = (r+4)*[""]
    for i in range (r+4):
        sachovnica[i] = (s+4)*[True]
    for i in range(s+4):
        sachovnica[0][i]=False
        sachovnica[1][i]=False
        sachovnica[r+2][i]=False
        sachovnica[r+3][i]=False
    for i in range(r+4):
        sachovnica[i][0]=False
        sachovnica[i][1]=False
        sachovnica[i][s+2]=False
        sachovnica[i][s+3]=False
    return sachovnica

k= False
def rekurzia (sach, s1, s2, p, final): 
    global k
    if sach[s1][s2] == False:
        return
    else:
        sach[s1][s2] = False
    if p == final:
        k=True
    if k == False:
        rekurzia (sach, s1-2, s2+1, p+1, final)
        rekurzia (sach, s1-2, s2-1, p+1, final)
        rekurzia (sach, s1+2, s2+1, p+1, final)
        rekurzia (sach, s1+2, s2-1, p+1, final)
        rekurzia (sach, s1+1, s2+2, p+1, final)
        rekurzia (sach, s1+1, s2-2, p+1, final)
        rekurzia (sach, s1-1, s2+2, p+1, final)
        rekurzia (sach, s1-1, s2-2, p+1, final)
        sach[s1][s2]=True
    
vstup= input().split()
r= int(vstup[0])
s = int(vstup[1])
start0 = int(vstup[2])
start1 = int(vstup[3])

sachovnica = vytvor_sachovnicu(r,s)

rekurzia(sachovnica, start0+1, start1+1, 1, r*s)
if k == True:
    print("ANO")
else: 
    print("NE")

