from random import randint
from random import randrange
def randomGraph():
	V=randint(0,1000)+2
	E=randint(0,V**2)+V-1
	print V,E
	x = 0
	while (x<E):
			u = randrange(V)
			v = randrange(V)
			while (u==v):
				u = randrange(V)
				v = randrange(V)
			print u+1,randrange(10)+1,v+1
			x = x+1
t= 1000
print t
while (t):
	randomGraph()
	t-=1