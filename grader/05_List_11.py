missing_degits = []
search = input()

for i in range(10):
    if str(i) not in search:
        missing_degits.append(str(i))

missing_degits.sort()

print(",".join(missing_degits) if len(missing_degits) else "None")
