primes = [2, 3, 5, 7]


def isPrime(x):
    for p in primes:
        if x % p == 0:
            return False
        if p * p >= x:
            return True
    return True


i = 9
while i <= 10 ** 6:
    if isPrime(i):
        primes.append(i)

    i += 2


def factor(N):  # N เป็ นจ ำนวนเต็มบวกมำกกว่ำ 1
    answers = []

    for p in primes:
        if N == 1:
            break

        count = 0
        while N % p == 0:
            N /= p
            count += 1

        if count > 0:
            answers.append([p, count])

    return answers


exec(input().strip())  # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
