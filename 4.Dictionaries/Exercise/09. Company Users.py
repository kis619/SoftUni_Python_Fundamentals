info = input()
companies_data = {}
while not info == "End":
    company, employee_id = info.split(" -> ")

    if company not in companies_data:
        companies_data[company] = []

    if employee_id not in companies_data[company]:
        companies_data[company].append(employee_id)

    info = input()


company_data_sorted = sorted(companies_data.items())
for company, employees in company_data_sorted:
    print(company)
    for employee in employees:
        print(f"-- {employee}")

