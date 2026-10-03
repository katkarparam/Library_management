employees = [
    {"name": "Rahul", "salary": 45000},
    {"name": "Amit", "salary": 65000},
    {"name": "Priya", "salary": 75000},
    {"name": "Neha", "salary": 40000}
]

for employee in employees:
    if employee["salary"] > 50000:
        print(employee["name"], employee["salary"])