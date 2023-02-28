#Coded By Subhadeep Mandal
'''
4
CDEF:MNOP:UVWX
BDGK:PTYF:TUYC
DFH:FHD:MOQ
CEG:IJM:NPR
'''
for _ in range(int(input())):
    s=input()
    arr=s.split(":")
    l=len(arr[0])
    val=[0]*l
    for i in range(l):
        val[i] = ord(arr[1][i]) - ord(arr[0][i])
	#print("Displacement = ",val)
    s+=":"
    for i in range(l):
        s+=chr(((ord(arr[2][i])-65 + val[i])%26)+65)
    print(s)