n = int(input())

tickets = []
next_ticket = 0
calling = 0
calling_order_were_there_since = 0

total_time_used = 0
total_customer_served = 0

for k in range(n):
    c = input().split()

    if c[0] == 'reset':
        next_ticket = int(c[1])
    elif c[0] == 'new':
        tickets.append((next_ticket, int(c[1])))
        print("ticket", next_ticket)
        next_ticket += 1
    elif c[0] == 'next':
        calling, calling_order_were_there_since = tickets[0]
        tickets = tickets[1:]
        print("call", calling)
    elif c[0] == 'order':
        time_used = int(c[1]) - calling_order_were_there_since
        print("qtime", calling, time_used)
        total_time_used += time_used
        total_customer_served += 1
    elif c[0] == 'avg_qtime':
        print("avg_qtime", total_time_used / total_customer_served)
