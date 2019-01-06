#!/usr/bin/python3
import random
def checkinput(q):
	if len(q) != 4: return False
	try:
		c=[int(x) for x in q]
		if min(c)<0 or max(c)>5: return False
	except: return False
	return True
def check(guess, secr):
	c=sum([int( int(guess[x] ) == int(secr[x]) ) for x in range(4)])
	d=sum([min(secr.count(x), guess.count(x)) for x in range(6)])
	print('#'*c+'*'*(d-c)); return c
secret = [random.randint(0,5) for x in range(4)]; inp=''
for x in range(10):
	while checkinput(inp) == False: inp = input(str(x+1)+"/10> ")
	cor = check([int(x) for x in inp], secret); inp=''
	if cor == 4: print("YOU WIN!"); break;
	elif x == 9: print("You lose :(")
print("Answer:", ''.join([str(x) for x in secret]))
