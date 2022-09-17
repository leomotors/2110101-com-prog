numbers = tuple(int(k) for k in input().split(" "))
k = int(input())

consec = 1
current = numbers[0]
sum_of_consec = 0

for i in range(1, len(numbers) + 1):
    if not i >= len(numbers) and numbers[i] == current:
        consec += 1
    else:
        if consec >= k:
            sum_of_consec += current * consec
        consec = 1

        if i < len(numbers):
            current = numbers[i]

print(sum(numbers) - sum_of_consec)
