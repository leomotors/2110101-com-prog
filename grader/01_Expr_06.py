from datetime import timedelta


def ඞ():
    return int(input())


sh = ඞ()
sm = ඞ()
ss = ඞ()

eh = ඞ()
em = ඞ()
es = ඞ()

start = timedelta(hours=sh, minutes=sm, seconds=ss)
end = timedelta(hours=eh, minutes=em, seconds=es)

if start < end:
    start += timedelta(days=1)

timediff = end - start

print("{}:{}:{}".format(timediff.seconds // 3600 %
      60, timediff.seconds // 60 % 60, timediff.seconds % 60))
