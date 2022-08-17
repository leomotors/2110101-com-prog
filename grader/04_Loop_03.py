import sys


key = input()
answer = input()

if len(key) != len(answer):
    print("Incomplete answer")
    sys.exit(0)

score = 0

for k, a in zip(key, answer):
    if k == a:
        score += 1

print(score)
