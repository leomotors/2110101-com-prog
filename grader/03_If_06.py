p = int(input())

print(18 if p <= 100 else 22 if p <= 250 else 28 if p <=
      500 else 38 if p <= 1000 else 58 if p <= 2000 else "Reject")
