import math
l=list(map(int,input().split()))
d=(l[1]*l[1])-(4*l[0]*l[2])
if d>0:
  r1=(-l[1]+math.sqrt(d))/(2*l[0])
  r2=(-l[1]-math.sqrt(d))/(2*l[0])
  print("%.2f"%r1)
  print("%.2f"%r2)
elif d==0:
  r=(-l[1])/(2*l[0])
  print("%.2f"%r)
  print("%.2f"%r)
elif d<0:
  r=r=(-l[1])/(2*l[0])
  i=math.sqrt(-d)/(2*l[0])
  print("%.2f+i%.2f"%(r,i))
  print("%.2f-i%.2f"%(r,i))
