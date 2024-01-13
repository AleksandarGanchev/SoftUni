from collections import deque

orders = deque(int(x) for x in input().split(", "))
employees = [int(x) for x in input().split(", ")]

total_pizzas = 0
while orders and employees:
    first_order = orders.popleft()

    if 0 < first_order <= 10:
        last_employee = employees.pop()

        if first_order > last_employee:
            orders.appendleft(first_order - last_employee)
            total_pizzas += last_employee
        else:
            total_pizzas += first_order

if not orders:
    print("All orders are successfully completed!")
    print(f"Total pizzas made: {total_pizzas}")
    print(f"Employees: {', '.join([str(x) for x in employees])}")

if not employees:
    print("Not all orders are completed.")
    print(f"Orders left: {', '.join([str(x) for x in orders])}")
