ญ='S'
ฌ='C'
ซ=' '
ฉ=len
ช=input
from functools import reduce as ง
ก=ช().split(ซ)
จ=tuple(filter(lambda x:not(not ฉ(x))and x in[ฌ,ญ],(ก for ก in ช())))
ข=ฉ(ก)//2
for ค in จ:
 if ค==ฌ:ก=ก[ข:]+ก[:ข]
 elif ค==ญ:ก=ง(lambda p,c:[*p,c[0],c[1]],zip(ก[:ข],ก[ข:]),[])
print(ซ.join(ก))
