V='\nKey:\n'
U=False
T=print
M=input
L=range
E=''
C=len
B=int
def N(number):
	A=number
	try:A=B(A)
	except:A=64
	if A<=0 or A>64:A=64
	C=J[A-1];return C
def G(character):
	A=character
	if A==E:A=' '
	B=J.find(A)+1
	if B==0:B=64
	return B
def O(value,min=1,max=64):
	A=value;A=A%max
	while A<min:A=max
	return A
def H(number,shift):A=number+B(shift);C=O(A);return C
def I(decimal):
	A=decimal;A-=1;D=format(A,'#08b');B=0;C=E
	for F in D:
		B+=1
		if B>2:C+=F
	return C
def P(binary):format='0b'+binary;A=B(format,2);return A+1
def D(text,shift,yn=True):
	list=[]
	for A in text:
		if yn:list.append(I(H(G(A),shift)))
		else:list.append(I(G(A)))
	return list
def Q(list,shift):
	A=E
	for B in list:A+=N(H(P(B),-shift))
	return A
def F(key):
	A=E
	for C in D(key,0,U):A+=C
	return B(A)%64
def R(key,length):
	A=length;list=D(key,0,U)*(round(A/C(key))+1)
	for B in L(C(list)-A):list.pop()
	return list
def S(one,two):
	A=one
	for D in L(C(A)):
		I=A[D];J=two[D];F=E;G=[B(A)for A in I];K=[B(A)for A in J]
		for H in L(C(G)):F+=str(G[H]^K[H])
		A[D]=F
	return A
J='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 .'
K=M('\nMessage:\n')
A=M(V)
while C(A)<4:T('Key must be more than 3 characters long.');A=M(V)
T('\n'+Q(S(D(K,F(A)),R(A,C(D(K,F(A))))),F(A)))