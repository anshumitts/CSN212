import numpy as np
import math as m	
import cv2 as cv2
import time
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

uper = 960
lowr = 1280
x_min = lowr
y_min = uper
point = None
x_0 = lowr
x_max = -1
p0=None
A = None
B = None
def draw_hull(hull,pts,string,keys):
	image = np.zeros((uper+10,lowr+10,3),np.uint8)
	if(hull):
		n = len(hull)
		for i in range(n):
			cv2.line(image,(hull[i].x+5,uper-hull[i].y+5),(hull[(i+1)%n].x+5,uper-hull[(i+1)%n].y+5),(0,0,255),2)
	for pt in pts:
		cv2.circle(image,(pt.x+5,uper-pt.y+5), 4, (np.random.randint(150)+100,np.random.randint(150)+100,0), -1)
	for key in keys:
		cv2.circle(image,(key.x+5,uper-key.y+5), 4, (255,255,255), -1)
	cv2.imwrite(str(string)+'.png',image)


class points(object):
	"""docstring for point"""
	def __init__(self, x,y):
		self.x = x
		self.y = y
		self.giftwrap()
		self.Graham_scan()
		self.quickHul()
	def giftwrap(self):
		global x_min,point
		if self.x<x_min:
			point = self
			x_min=self.x

	def Graham_scan(self):
		global y_min,p0,x_0
		if self.y < y_min:
			p0 = self
			y_min=self.y
		else:
			if self.y == y_min:
				if self.x<x_0:
					p0 = self
					x_0 = self.x
	def quickHul(self):
		global x_min,x_max,point,A,B
		A=point
		if self.x>x_max:
			B = self
			x_max = self.x



def orientation(p,q,r):
	val = (q.y - p.y) * (r.x - q.x) -(q.x - p.x) * (r.y - q.y)
	if val == 0: 
		return 0
	return 1 if val > 0 else 2

def distance(p1,p2):
	return ((p1.x-p2.x)**2)+((p1.y-p2.y)**2)

def compare(p1,p2):
	global p0
	val = orientation(p0,p1,p2)
	if val==0:
		return -1 if distance(p0,p2)> distance(p0,p1) else 1
	return -1 if val==2 else 1
def line_para(a,b):
	return (a.x-b.x),(b.y-a.y),(b.x*a.y-a.x*b.y),m.sqrt((a.x-b.x)*(a.x-b.x)+(b.y-a.y)*(b.y-a.y))

def giftwarp(pts):
	hull = []
	n = len(pts)
	k = pts.index(point)
	p = point
	hull.append(p)
	while True:
		q=pts[(k+1)%n]
		for r in pts:
			if(orientation(p,r,q)==2):
				q = r
		if(point == q):
			break
		else:
			p = q
			hull.append(p)
			k = pts.index(p)
	return hull

def Graham_scan(pts):
	k = pts.index(p0)
	(pts[0],pts[k])=(pts[k],pts[0]) 
	temp = pts[1:] 
	temp.sort(compare)
	pts[1:]=temp
	n = len(pts)
	temp_pts = []
	temp_pts.append(pts[0])
	for i in xrange(1,n):
		while i<n-1 and orientation(p0,pts[i],pts[i+1]) == 0:
			i+=1
		temp_pts.append(pts[i])
	m=len(temp_pts)
	hull=[]
	hull.append(temp_pts[0])
	hull.append(temp_pts[1])
	hull.append(temp_pts[2])
	for k in xrange(3,m):
		try:
			while orientation(hull[-2],hull[-1],temp_pts[k])!=2:
				hull=hull[:-1]
		except:
			print hull,temp_pts[k]
		hull.append(temp_pts[k])
	return hull

def findHull(S,hull,A,B,ref):
	if(len(S)==1):
		hull.append(S[0])
		return hull
	if ref==None:
		return hull
	hull.append(ref)
	maxx = 0
	minn = 0
	a,b,c,d=line_para(A,ref)
	S1=[]
	S1_max=None
	S2=[]
	S2_max=None
	for pt in S:
		dist = (a*pt.y+b*pt.x+c)/d
		if dist>0:
			S1.append(pt)
			if dist>maxx:
				S1_max=pt
				maxx=dist
		else:
			S2.append(pt)
			if dist<minn:
				S2_max=pt
				minn=dist
	dist = (a*B.y + b*B.x +c)/d
	if dist>0:
		if(len(S2)>0):
			hull = findHull(S2,hull,A,ref,S2_max)
	else:
		if (len(S1)>0):
			hull = findHull(S1,hull,A,ref,S1_max)
	maxx = 0
	minn = 0
	a,b,c,d=line_para(B,ref)
	S1=[]
	S1_max=None
	S2=[]
	S2_max=None
	for pt in S:
		dist = (a*pt.y+b*pt.x+c)/d
		if dist>0:
			S1.append(pt)
			if dist>maxx:
				S1_max=pt
				maxx=dist
		else:
			S2.append(pt)
			if dist<minn:
				S2_max=pt
				minn=dist
	dist = (a*A.y + b*A.x +c)/d
	if dist>0:
		if(len(S2)>0):
			hull = findHull(S2,hull,B,ref,S2_max)
	else:
		if (len(S1)>0):
			hull = findHull(S1,hull,B,ref,S1_max)
	return hull


def quickHul(pts):
	global A,B
	maxx = 0
	minn = 0
	hull=[]
	hull.append(A)
	hull.append(B)
	a,b,c,d=line_para(A,B)
	S=pts[:]
	S.remove(A)
	S.remove(B)
	S1=[]
	S1_max=None
	S2=[]
	S2_max=None
	for pt in S:
		dist = (a*pt.y+b*pt.x+c)/d
		if dist>0:
			S1.append(pt)
			if dist>maxx:
				S1_max=pt
				maxx=dist
		else:
			S2.append(pt)
			if dist<minn:
				S2_max=pt
				minn=dist
	hull = findHull(S1,hull,A,B,S1_max)
	hull = findHull(S2,hull,A,B,S2_max)
	hull.sort(compare)
	return hull

tame = []
def main():
	global x_min,y_min,point,x_0,x_max,p0,A,B
	ks = [100,1000,2000,5000,10000]
	xAxis = [x+1 for x in range(5)]
	for k in ks:
		x_min = lowr
		y_min = uper
		point = None
		x_0 = lowr
		x_max = -1
		p0 = None
		A = None
		B = None
		q = 3 
		pts = [points(np.random.randint(lowr,size=1)+1,np.random.randint(uper,size=1)+1) for x in range(k)]
		t0=time.time()
		draw_hull(giftwarp(pts),pts,'giftwrap'+str(k),[point])
		tame.append(time.time()-t0)
		t0=time.time()
		draw_hull(Graham_scan(pts),pts,'grahm'+str(k),[p0])
		tame.append(time.time()-t0)
		t0=time.time()
		draw_hull(quickHul(pts),pts,'Quick'+str(k),[A,B])
		tame.append(time.time()-t0)

	fig = plt.figure()
	ax = fig.add_subplot(111)
	ax.plot( ks,tame[0::3], '.b-', linewidth=2.0)
	ax.plot( ks,tame[1::3], '.r-', linewidth=2.0)
	ax.plot( ks,tame[2::3], '.g-', linewidth=2.0)
	patch1 = mpatches.Patch(color='red', label='Grahm Search')
	patch2 = mpatches.Patch(color='blue', label='Gift Wrap')
	patch3 = mpatches.Patch(color='green', label='Quick Hull')
	plt.legend(handles=[patch2,patch1,patch3])
	ax.set_xlabel('N')
	ax.set_ylabel('Time')
	plt.show()
	pass
main()