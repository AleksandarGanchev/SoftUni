company_data = {}

command = input()
while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_data:
        company_data[company_name] = [employee_id]

    else:
        if employee_id not in company_data[company_name]:
            company_data[company_name].append(employee_id)

    command = input()


for company_name, employees_id in company_data.items():
    print(f"{company_name}")
    for employee_id in employees_id:
        print(f"-- {employee_id}")
