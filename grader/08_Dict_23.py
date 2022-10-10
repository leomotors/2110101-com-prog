phone_book = {}

N = int(input())

for i in range(N):
    name, surname, phone = input().split(" ")
    phone_book[name + " " + surname] = phone
    phone_book[phone] = name + " " + surname

M = int(input())

for i in range(M):
    token = input()
    print(token, "-->", phone_book.get(token, "Not found"))
