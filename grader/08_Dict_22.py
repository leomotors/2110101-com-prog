aitims = {}

N = int(input())

for i in range(N):
    aitim, price = input().split(" ")

    aitims[aitim] = int(price)

M = int(input())

sales = {}
sales_total = 0

for i in range(M):
    aitim, quant = input().split(" ")
    quant = int(quant)

    if aitim in aitims:
        money = aitims[aitim] * quant

        if aitim in sales:
            sales[aitim] += money
        else:
            sales[aitim] = money

        sales_total += money

if sales_total == 0:
    print("No ice cream sales")
else:
    print("Total ice cream sales:", float(sales_total))

    top_sales = sorted(
        list(
            filter(
                lambda x: sales[x] == max(sales.values()),
                sales.keys())))

    print("Top sales:", ", ".join(top_sales))
